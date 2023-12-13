import enum

import strawberry

from odooghost import stack
from strawberry.scalars import JSON


@strawberry.enum
class StackState(enum.Enum):
    STOPPED = "STOPPED"
    RUNNING = "RUNNING"
    RESTARTING = "RESTARTING"
    PAUSED = "PAUSED"


@strawberry.type
class Stack:
    name: str
    instance: strawberry.Private[stack.Stack]

    @strawberry.field
    def network_mode(self) -> str:
        return self.instance._config.network.mode
    
    @strawberry.field
    def odoo_version(self) -> float:
        return self.instance.get_service("odoo").config.version
    
    @strawberry.field
    def db_version(self) -> float:
        return self.instance.get_service("db").config.version
    
    @strawberry.field
    def services_count(self) -> int:
        return len(self.instance._config.services.__dict__.keys())
    
    @strawberry.field
    def containers(self) -> list[JSON]:
        wanted_container_field = ["name", "is_running", "is_paused", "is_restarting", "service", "id", "create_date", "started_at"]
        
        for container in self.instance.containers(stopped=True):
            final_dict = dict()
            for field in wanted_container_field:
                final_dict[field] = getattr(container, field)
            yield final_dict

    @strawberry.field
    def state(self) -> StackState:
        containers = self.instance.containers(stopped=True)
        if all(c.is_running for c in containers):
            return StackState.RUNNING
        if all(c.is_paused for c in containers):
            return StackState.PAUSED
        if any(c.is_restarting for c in containers):
            return StackState.RESTARTING
        return StackState.STOPPED

    @classmethod
    def from_instance(cls, instance: stack.Stack) -> "Stack":
        return cls(name=instance.name, instance=instance)
