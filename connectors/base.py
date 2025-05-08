"""
Base Connector - Abstract base class for system connectors
All integration connectors inherit from this
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from datetime import datetime

@dataclass
class ConnectorConfig:
    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    base_url: Optional[str] = None
    oauth_token: Optional[str] = None
    refresh_token: Optional[str] = None
    webhook_secret: Optional[str] = None

class BaseConnector(ABC):
    """Abstract base class for all system connectors"""

    def __init__(self, config: ConnectorConfig):
        self.config = config
        self.connected = False
        self.last_sync: Optional[datetime] = None

    @abstractmethod
    async def connect(self) -> bool:
        """Establish connection to the external system"""
        pass

    @abstractmethod
    async def disconnect(self):
        """Close connection to the external system"""
        pass

    @abstractmethod
    async def send(self, payload: dict) -> dict:
        """Send data to the external system"""
        pass

    @abstractmethod
    async def receive(self) -> List[dict]:
        """Receive data from the external system"""
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if connection is healthy"""
        pass

    def get_status(self) -> dict:
        """Get connector status"""
        return {
            "connected": self.connected,
            "last_sync": self.last_sync.isoformat() if self.last_sync else None,
        }
