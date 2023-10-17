from copy import deepcopy
import typing as T

import openai

from .base import Agent, Conversation, Message


class OpenAIAgent(Agent):
    conversation: Conversation
    params: dict

    def __init__(
        self,
        context_prompt: str = "",
        *,
        conversation: Conversation | None = None,
        **params
    ):
        if conversation is not None:
            assert not context_prompt
        else:
            assert context_prompt is not None
            conversation = Conversation(context_prompt=context_prompt, messages=[])
        self.conversation = conversation
        self.params = params

    def ask(self, text: str, *, skip_history=False, **params) -> str:
        new_messages = deepcopy(self.conversation.messages)
        new_messages.append(Message("user", text))

        create_args = {
            **self.params,
            **params,
            "messages": self._make_api_messages(self.conversation.context_prompt, new_messages),
        }

        res = openai.ChatCompletion.create(**create_args)

        self.last_res_ = res
        out = self.last_res_.choices[0].message.content
        assert out is not None

        if not skip_history:
            new_messages.append(Message("assistant", out))
            self.conversation.messages = new_messages

        return out

    def asks(self, text: str, *, skip_history=False, **params) -> T.Iterable[str]:
        new_messages = deepcopy(self.conversation.messages)
        new_messages.append(Message("user", text))

        create_args = {
            **self.params,
            **params,
            "messages": self._make_api_messages(self.conversation.context_prompt, new_messages),
            "stream": True,
        }
        res = openai.ChatCompletion.create(**create_args)

        out = ""
        for res_chunk in res:
            self.last_res_ = res_chunk
            delta = res_chunk.choices[0].delta
            out += getattr(delta, "content", "")
            yield out

        if not skip_history:
            new_messages.append(Message("assistant", out))
            self.conversation.messages = new_messages

    def _make_api_messages(
        self, context_prompt: str, messages: list[Message]
    ) -> list[dict]:
        out = [{"role": "system", "content": context_prompt}]
        for m in messages:
            out.append(
                {
                    "role": m.role,
                    "content": m.content,
                }
            )
        return out
