from datetime import datetime
from dataclasses import dataclass

@dataclass
class StandardError:
    status: int
    error: str
    message: str
    path: str
    timestamp: str = None

    def __post_init__(self):
        self.timestamp = datetime.utcnow().isoformat() + "Z"

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "status": self.status,
            "error": self.error,
            "message": self.message,
            "path": self.path
        }