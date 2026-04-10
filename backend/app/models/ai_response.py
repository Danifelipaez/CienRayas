from typing import Dict, Optional
from datetime import datetime

class AIResponse:
    def __init__(self, message: str, model: str, tokens_used: int = 0):
        self.message = message
        self.model = model
        self.tokens_used = tokens_used
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict:
        return {
            "message": self.message,
            "model": self.model,
            "tokens": self.tokens_used,
            "timestamp": self.timestamp.isoformat()
        }
