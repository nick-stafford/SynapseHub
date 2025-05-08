"""
Integration Orchestrator - Central hub for managing system connections
Handles routing, transformation, and sync operations
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Callable
from datetime import datetime
import asyncio
import logging

logger = logging.getLogger(__name__)

@dataclass
class SyncEvent:
    id: str
    source_system: str
    target_system: str
    event_type: str
    payload: dict
    timestamp: datetime
    status: str  # "pending", "processing", "completed", "failed"

@dataclass
class Connection:
    source: str
    target: str
    sync_type: str  # "unidirectional", "bidirectional"
    transform_fn: Optional[Callable] = None
    filters: Optional[dict] = None
    enabled: bool = True

class IntegrationOrchestrator:
    """Central orchestrator for all system integrations"""

    def __init__(self):
        self.connections: Dict[str, Connection] = {}
        self.connectors: Dict[str, 'BaseConnector'] = {}
        self.event_queue: asyncio.Queue = asyncio.Queue()
        self.sync_history: List[SyncEvent] = []

    def register_connector(self, name: str, connector: 'BaseConnector'):
        """Register a system connector"""
        self.connectors[name] = connector
        logger.info(f"Registered connector: {name}")

    def create_connection(
        self,
        source: str,
        target: str,
        sync_type: str = "unidirectional",
        transform_fn: Optional[Callable] = None
    ) -> str:
        """Create a connection between two systems"""
        conn_id = f"{source}_{target}"
        self.connections[conn_id] = Connection(
            source=source,
            target=target,
            sync_type=sync_type,
            transform_fn=transform_fn
        )
        return conn_id

    async def process_event(self, event: SyncEvent):
        """Process a sync event through the pipeline"""
        try:
            event.status = "processing"

            # Get connection config
            conn_id = f"{event.source_system}_{event.target_system}"
            connection = self.connections.get(conn_id)

            if not connection or not connection.enabled:
                logger.warning(f"No active connection found: {conn_id}")
                return

            # Apply transformation if defined
            payload = event.payload
            if connection.transform_fn:
                payload = connection.transform_fn(payload)

            # Get target connector and send
            target_connector = self.connectors.get(event.target_system)
            if target_connector:
                await target_connector.send(payload)
                event.status = "completed"
            else:
                event.status = "failed"

            self.sync_history.append(event)

        except Exception as e:
            logger.error(f"Event processing failed: {e}")
            event.status = "failed"

    async def run(self):
        """Main event processing loop"""
        while True:
            event = await self.event_queue.get()
            await self.process_event(event)

    def get_stats(self) -> dict:
        """Get orchestration statistics"""
        completed = len([e for e in self.sync_history if e.status == "completed"])
        failed = len([e for e in self.sync_history if e.status == "failed"])

        return {
            "total_connections": len(self.connections),
            "active_connectors": len(self.connectors),
            "events_processed": len(self.sync_history),
            "success_rate": completed / max(len(self.sync_history), 1),
            "failed_events": failed,
        }
