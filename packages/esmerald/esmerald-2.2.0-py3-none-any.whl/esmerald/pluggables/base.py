from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Iterator, Optional

from esmerald.protocols.extension import ExtensionProtocol

if TYPE_CHECKING:  # pragma: no cover
    from esmerald.applications import Esmerald


class Pluggable:
    """
    The class object used to manage pluggables for esmerald.

    A pluggable is whatever adds extra level of functionality to
    your an Esmerald application and is used as support for your application.
    """

    def __init__(self, cls: "Extension", **options: Any):
        self.cls = cls
        self.options = options

    def __iter__(self) -> Iterator:
        iterator = (self.cls, self.options)
        return iter(iterator)

    def __repr__(self) -> str:  # pragma: no cover
        name = self.__class__.__name__
        options = [f"{key}={value!r}" for key, value in self.options.items()]
        args = ", ".join([self.__class__.__name__] + options)
        return f"{name}({args})"


class BaseExtension(ABC, ExtensionProtocol):  # pragma: no cover
    """
    The base for any Esmerald plugglable.
    """

    def __init__(self, app: Optional["Esmerald"] = None, **kwargs: Any):
        super().__init__(app, **kwargs)
        self.app = app

    @abstractmethod
    def extend(self, **kwargs: "Any") -> None:
        raise NotImplementedError("plug must be implemented by the subclasses.")


class Extension(BaseExtension):
    ...
