from dataclasses import dataclass
from enum import Enum


class MessageType(Enum):
    info: str = 'info'  # mess type for get condition of auto answering
    action: str = 'action'  # mess type to do some action (for example: update smth)


@dataclass
class MessageContent:
    body: str
    type: str
