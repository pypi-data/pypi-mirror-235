from typing import TYPE_CHECKING, Any, Dict, Optional, Type, Union

from esmerald.datastructures.base import ResponseContainer  # noqa
from esmerald.enums import MediaType
from esmerald.responses import JSONResponse  # noqa

if TYPE_CHECKING:  # pragma: no cover
    from esmerald.applications import Esmerald


class JSON(ResponseContainer[JSONResponse]):
    """
    Returns a wrapper of a JSONResponse.
    """

    content: Optional[Dict[str, Any]] = None
    status_code: Optional[int] = None
    media_type: str = "application/json"

    def __init__(
        self,
        content: Optional[Dict[str, Any]] = None,
        status_code: Optional[int] = None,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.content = content
        self.status_code = status_code
        self._media_type = self.media_type

    def to_response(
        self,
        headers: Dict[str, Any],
        media_type: Union["MediaType", str],
        status_code: int,
        app: Type["Esmerald"],
    ) -> JSONResponse:
        status = self.status_code or status_code

        return JSONResponse(
            content=self.content,
            headers=headers,
            status_code=status,
            media_type=media_type,
            background=self.background,
        )
