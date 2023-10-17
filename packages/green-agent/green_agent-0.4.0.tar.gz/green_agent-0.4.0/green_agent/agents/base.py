from copy import deepcopy
from dataclasses import dataclass
import typing as T


@dataclass
class Message:
    # eg. OpenAI "role" ("system", "user", "assistant", "function")
    # or Vertex/Google "author" ("user" or "bot")
    role: T.Literal["user", "assistant", "function"]
    # actual message content
    content: str
    # either provided user name (eg. for abuse tracking etc.)
    # or the called function if any was called 
    name: str | None = None


@dataclass
class Conversation:
    messages: list[Message]
    # eg. OpenAI "system prompt" or Vertex/Google "context"
    context_prompt: str | None = None
    # list of ("input", "output") pairs
    examples: list[tuple[str, str]] | None = None


class Agent:
    conversation: Conversation = None

    def ask(
        self, text: str, *, skip_history=False, **params
    ) -> str:
        raise NotImplementedError

    def clone(self) -> "Agent":
        return deepcopy(self)
