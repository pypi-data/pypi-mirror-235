import re
from typing import TYPE_CHECKING, Any, Callable, List, Optional, Sequence, Union, cast

from starlette.routing import Route as StarletteRoute
from starlette.routing import WebSocketRoute as StarletteWebSocketRoute
from starlette.routing import compile_path
from starlette.types import Receive, Scope, Send

from esmerald.routing.apis.base import View
from esmerald.routing.base import BaseInterceptorMixin
from esmerald.typing import Void, VoidType
from esmerald.utils.helpers import clean_string, is_class_and_subclass
from esmerald.utils.url import clean_path

if TYPE_CHECKING:  # pragma: no cover
    from openapi_schemas_pydantic.v3_1_0.security_scheme import SecurityScheme

    from esmerald.interceptors.types import Interceptor
    from esmerald.permissions.types import Permission
    from esmerald.routing.router import HTTPHandler, WebhookHandler, WebSocketHandler
    from esmerald.types import Dependencies, ExceptionHandlerMap, Middleware, ParentType


class Gateway(StarletteRoute, BaseInterceptorMixin):
    __slots__ = (
        "_interceptors",
        "path",
        "handler",
        "name",
        "include_in_schema",
        "parent",
        "dependencies",
        "middleware",
        "exception_handlers",
        "interceptors",
        "permissions",
        "deprecated",
    )

    def __init__(
        self,
        path: Optional[str] = None,
        *,
        handler: Union["HTTPHandler", View],
        name: Optional[str] = None,
        include_in_schema: bool = True,
        parent: Optional["ParentType"] = None,
        dependencies: Optional["Dependencies"] = None,
        middleware: Optional[Sequence["Middleware"]] = None,
        interceptors: Optional[Sequence["Interceptor"]] = None,
        permissions: Optional[Sequence["Permission"]] = None,
        exception_handlers: Optional["ExceptionHandlerMap"] = None,
        deprecated: Optional[bool] = None,
        is_from_router: bool = False,
        security: Optional[Sequence["SecurityScheme"]] = None,
    ) -> None:
        if not path:
            path = "/"
        if is_class_and_subclass(handler, View):
            handler = handler(parent=self)  # type: ignore

        if not is_from_router:
            self.path = clean_path(path + handler.path)
        else:
            self.path = clean_path(path)

        self.methods = getattr(handler, "http_methods", None)

        if not name:
            if not isinstance(handler, View):
                name = clean_string(handler.fn.__name__)
            else:
                name = clean_string(handler.__class__.__name__)

        super().__init__(
            path=self.path,
            endpoint=cast("Callable", handler),
            include_in_schema=include_in_schema,
            name=name,
            methods=cast("List[str]", self.methods),
        )
        """
        A "bridge" to a handler and router mapping functionality.
        Since the default Starlette Route endpoint does not understand the Esmerald handlers,
        the Gateway bridges both functionalities and adds an extra "flair" to be compliant with both class based views and decorated function views.
        """
        self._interceptors: Union[List["Interceptor"], "VoidType"] = Void
        self.name = name
        self.handler = handler
        self.dependencies = dependencies or {}
        self.interceptors: Sequence["Interceptor"] = interceptors or []
        self.permissions: Sequence["Permission"] = permissions or []
        self.middleware = middleware or []
        self.exception_handlers = exception_handlers or {}
        self.response_class = None
        self.response_cookies = None
        self.response_headers = None
        self.deprecated = deprecated
        self.parent = parent
        self.security = security
        (
            handler.path_regex,
            handler.path_format,
            handler.param_convertors,
        ) = compile_path(self.path)

        if not is_class_and_subclass(self.handler, View) and not isinstance(self.handler, View):
            self.handler.name = self.name
            self.handler.get_response_handler()

            if not handler.operation_id:
                handler.operation_id = self.generate_operation_id()

    async def handle(self, scope: "Scope", receive: "Receive", send: "Send") -> None:
        """
        Handles the interception of messages and calls from the API.
        """
        if self.get_interceptors():
            await self.intercept(scope, receive, send)

        await self.handler.handle(scope, receive, send)

    def generate_operation_id(self) -> str:
        """
        Generates an unique operation if for the handler
        """
        operation_id = self.name + self.handler.path_format
        operation_id = re.sub(r"\W", "_", operation_id)
        methods = list(self.handler.methods)

        assert self.handler.methods
        operation_id = f"{operation_id}_{methods[0].lower()}"
        return operation_id


class WebSocketGateway(StarletteWebSocketRoute, BaseInterceptorMixin):
    __slots__ = (
        "_interceptors",
        "path",
        "handler",
        "name",
        "dependencies",
        "middleware",
        "exception_handlers",
        "interceptors",
        "permissions",
        "parent",
        "security",
    )

    def __init__(
        self,
        path: Optional[str] = None,
        *,
        handler: Union["WebSocketHandler", View],
        name: Optional[str] = None,
        parent: Optional["ParentType"] = None,
        dependencies: Optional["Dependencies"] = None,
        middleware: Optional[Sequence["Middleware"]] = None,
        exception_handlers: Optional["ExceptionHandlerMap"] = None,
        interceptors: Optional[List["Interceptor"]] = None,
        permissions: Optional[List["Permission"]] = None,
    ) -> None:
        if not path:
            path = "/"
        if is_class_and_subclass(handler, View):
            handler = handler(parent=self)  # type: ignore
        self.path = clean_path(path + handler.path)

        if not name:
            if not isinstance(handler, View):
                name = clean_string(handler.fn.__name__)
            else:
                name = clean_string(handler.__class__.__name__)

        super().__init__(
            path=self.path,
            endpoint=cast("Callable", handler),
            name=name,
        )
        """
        A "bridge" to a handler and router mapping functionality.
        Since the default Starlette Route endpoint does not understand the Esmerald handlers,
        the Gateway bridges both functionalities and adds an extra "flair" to be compliant with both class based views and decorated function views.
        """
        self._interceptors: Union[List["Interceptor"], "VoidType"] = Void
        self.handler = handler
        self.dependencies = dependencies or {}
        self.interceptors = interceptors or []
        self.permissions = permissions or []
        self.middleware = middleware or []
        self.exception_handlers = exception_handlers or {}
        self.include_in_schema = False
        self.parent = parent
        (
            handler.path_regex,
            handler.path_format,
            handler.param_convertors,
        ) = compile_path(self.path)

    async def handle(self, scope: "Scope", receive: "Receive", send: "Send") -> None:
        """
        Handles the interception of messages and calls from the API.
        """
        if self.get_interceptors():
            await self.intercept(scope, receive, send)  # pragma: no cover

        await self.handler.handle(scope, receive, send)


class WebhookGateway(StarletteRoute, BaseInterceptorMixin):
    __slots__ = (
        "_interceptors",
        "path",
        "handler",
        "name",
        "include_in_schema",
        "parent",
        "dependencies",
        "middleware",
        "exception_handlers",
        "interceptors",
        "permissions",
    )

    def __init__(
        self,
        *,
        handler: Union["WebhookHandler", View],
        name: Optional[str] = None,
        include_in_schema: bool = True,
        parent: Optional["ParentType"] = None,
        deprecated: Optional[bool] = None,
        security: Optional[Sequence["SecurityScheme"]] = None,
    ) -> None:
        if is_class_and_subclass(handler, View):
            handler = handler(parent=self)  # type: ignore

        self.path = handler.path
        self.methods = getattr(handler, "http_methods", None)

        if not name:
            if not isinstance(handler, View):
                name = clean_string(handler.fn.__name__)
            else:
                name = clean_string(handler.__class__.__name__)

        self.endpoint = cast("Callable", handler)
        self.include_in_schema = include_in_schema

        self._interceptors: Union[List["Interceptor"], "VoidType"] = Void
        self.name = name
        self.handler = handler
        self.dependencies: Any = {}
        self.interceptors: Sequence["Interceptor"] = []
        self.permissions: Sequence["Permission"] = []
        self.middleware: Any = []
        self.exception_handlers: Any = {}
        self.response_class = None
        self.response_cookies = None
        self.response_headers = None
        self.deprecated = deprecated
        self.parent = parent
        self.security = security
        (
            handler.path_regex,
            handler.path_format,
            handler.param_convertors,
        ) = compile_path(self.path)

        if not is_class_and_subclass(self.handler, View) and not isinstance(self.handler, View):
            self.handler.name = self.name
            self.handler.get_response_handler()

            if not handler.operation_id:
                handler.operation_id = self.generate_operation_id()

    def generate_operation_id(self) -> str:
        """
        Generates an unique operation if for the handler
        """
        operation_id = self.name + self.handler.path_format
        operation_id = re.sub(r"\W", "_", operation_id)
        methods = list(self.handler.methods)

        assert self.handler.methods
        operation_id = f"{operation_id}_{methods[0].lower()}"
        return operation_id
