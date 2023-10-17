from dataclasses import dataclass
from typing import Optional
from src.chat import create_chat
from src.jsonschema import invoke
from src.logging import log
import openai
import os
import requests
import traceback

def trunc(content, max_length):
        if len(content) > max_length:
            return content[:max_length] + "..."
        else:
            return content

@dataclass
class TextMessage:
    role: str
    content: str

    @staticmethod
    def user(content):
        return TextMessage("user", content)

    @staticmethod
    def system(content):
        return TextMessage("system", content)

    @staticmethod
    def assistant(content):
        return TextMessage("assistant", content)

    def obj(self):
        return { "role": self.role, "content": self.content }

    def verboseString(self):
        if self.role == "assistant":
            arrow = "<"
        else:
            arrow = ">"
        return f'{self.role} text{arrow} {self.content}' + "\n -- end --\n"

    def debugString(self):
        if self.role == "assistant":
            arrow = "<"
        else:
            arrow = ">"
        return f'{self.role} text{arrow} {trunc(self.content, 100)}'

@dataclass
class FunctionCallMessage:
    call_name: str
    call_args: str

    def formatted(self):
        formatted_args = self.call_args.replace("\n", "")
        return f'{self.call_name}({formatted_args})'

    def obj(self):
        return {
            "role": "assistant",
            "content": None,
            "function_call": {
                "name": self.call_name,
                "arguments": self.call_args
                }
            }

    def verboseString(self):
        return f'assistant < {self.call_name}({self.call_args})' + "\n -- end --\n"

    def debugString(self):
        return f'assistant < {self.call_name}({trunc(self.call_args, 100)})'

@dataclass
class FunctionResult:
    call_name: str
    content: str

    def __repr__(self):
        short = trunc(self.content, 40)
        return f'FunctionResult({self.call_name}, {short})'

    def obj(self):
        return {
                "role": "function",
                "name": self.call_name,
                "content": self.content
                }
    def verboseString(self):
        return f'function result > {self.call_name} -> {self.content}' + "\n -- end --\n"

    def debugString(self):
        return f'function result > {self.call_name} -> {trunc(self.content, 100)}'

@dataclass
class CompletedCall:
    call: FunctionCallMessage
    result: FunctionResult

class Conversation:
    def __init__(self, model, instructions, functions=[]):
        self.model = model
        self.functions = functions
        self.messages = [TextMessage.system(instructions)]
        self.completed_calls = []

    def send(self, message):
        log("-----------------------------------------------------")
        self.messages.append(message)
        log("\n".join([m.verboseString() for m in self.messages]))

        response = create_chat(list(map(lambda x: x.obj(), self.messages)), 0, self.functions, self.model, False, False)
        choice = response['choices'][0]
        if choice.finish_reason == "function_call":
            try:
                call_name = choice.message.function_call.name
                call_args = choice.message.function_call.arguments
                function_call = FunctionCallMessage(call_name, call_args)
                self.messages.append(function_call)
                log(f'Response: {function_call.verboseString()}')
                output = invoke(self.functions, call_name, call_args)
                fr = FunctionResult(call_name, output)
                self.completed_calls.append(CompletedCall(function_call, fr))
                return self.send(fr)
            except Exception as e:
                log(f'Exception {e}')
                log(traceback.format_exc())
                return self.send(TextMessage.system(str(e)))
        if choice.finish_reason != "stop":
            log(f'Stop with error: {choice.finish_reason}')
            raise Exception(choice.finish_reason)

        response_message = choice["message"]
        if "content" in response_message:
            response = TextMessage(response_message["role"], response_message["content"])
        else:
            log(f'No content in response {response_message}')
            raise Exception("No content in response")
        self.messages.append(response)
        log(f'Response: {response.verboseString()}')
        return response.content

