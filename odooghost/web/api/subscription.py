import logging
import typing as t

import strawberry

from odooghost.context import ctx
from odooghost.utils.sync_to_async import sync_to_async_iterator

_logger = logging.getLogger("uvicorn")


def _watch_events():
    while True:
        try:
            events = ctx.docker.api.events(
                decode=True, filters=dict(label="odooghost=true")
            )
            for event in events:
                _logger.error(event)
                yield event
        except StopIteration:
            break
        finally:
            events.close()


@sync_to_async_iterator
def stream_events() -> t.Generator[dict, None, None]:
    yield from _watch_events()


@strawberry.type
class Event:
    id: str
    action: str
    image_from: str
    container_id: str
    container_name: str
    stack_name: str
    service_name: str


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def events(self) -> t.AsyncGenerator[Event, None]:
        _logger.error("e")
        async for e in stream_events():
            if e.get("Type", False) == "container":
                yield Event(
                    id=e.get("id"),
                    action=e.get("Action"),
                    image_from=e.get("from"),
                    container_id=e.get("Actor").get("ID"),
                    container_name=e.get("Actor").get("Attributes").get("name"),
                    service_name=e.get("Actor")
                    .get("Attributes")
                    .get("odooghost_stack_type"),
                    stack_name=e.get("Actor")
                    .get("Attributes")
                    .get("odooghost_stackname"),
                )
