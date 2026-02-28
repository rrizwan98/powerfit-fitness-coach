"""
ChatKit Server with PowerFit Fitness Coach Integration
"""

from collections.abc import AsyncIterator

from agents import Runner
from chatkit.server import ChatKitServer
from chatkit.types import ThreadMetadata, ThreadStreamEvent, UserMessageItem
from chatkit.agents import AgentContext, simple_to_agent_input, stream_agent_response

from agents_config import fitness_coach
from store import InMemoryStore


class PowerFitChatKitServer(ChatKitServer[dict]):
    """ChatKit server for PowerFit fitness coaching."""

    def __init__(self, store: InMemoryStore):
        super().__init__(store)

    async def respond(
        self,
        thread: ThreadMetadata,
        input_user_message: UserMessageItem | None,
        context: dict,
    ) -> AsyncIterator[ThreadStreamEvent]:
        """
        Generate streaming response from the fitness coach agent.

        Args:
            thread: The conversation thread
            input_user_message: The user's message
            context: Request context

        Yields:
            Stream events for the ChatKit UI
        """
        # Load conversation history
        items_page = await self.store.load_thread_items(
            thread.id, after=None, limit=50, order="asc", context=context
        )

        # Convert ChatKit messages to agent input format
        agent_input = await simple_to_agent_input(items_page.data)

        # Create agent context with thread and store
        agent_context = AgentContext(
            thread=thread, store=self.store, request_context=context
        )

        # Run the fitness coach agent with streaming
        result = Runner.run_streamed(fitness_coach, agent_input, context=agent_context)

        # Stream the response back to ChatKit
        async for event in stream_agent_response(agent_context, result):
            yield event


# Initialize server with in-memory store
store = InMemoryStore()
server = PowerFitChatKitServer(store=store)
