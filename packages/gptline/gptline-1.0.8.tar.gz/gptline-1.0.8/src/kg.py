from src.db import ChatDB
from src.convo import Conversation, TextMessage
from src.logging import log
import traceback

INSTRUCTIONS = """
Your job is to extract objects and their relationships from a conversation in order to build a knowledge graph. The objects you extract will be the nodes in the graph. The graph has a node for each concept (for example, a person, an activity, or a thing) and edges between nodes that describe their relationship. For exmaple, if Alice is writing a Python program, there would be an "Alice" node and a "Python" node with an edge connecting them labeled "programs in". There can be additional edges between objects that are present in the conversation that do not include the user.

Your job is to come up with a list of nodes and edges.

The conversation will be between a user and an assistant and it will be formatted as:

user: [message from user]
assistant: [message from assistant]

There may be many messages between the user and the assistant.

You should respond with a list of node->edge->node with one edge per line. For example:

Alice->programs in->Python
Alice->writes->Computer programs
Python->produces->Error

Note that the assistant is a language model and should not be included in any of the nodes.

The labels on nodes should make sense out of context. Ensure you include enough information in each node's label that it makes sense without reading the original conversation.
"""

CHECKPOINT_NAME = "kg_chat_id"

class KnowledgeGraphBuilder:
    def __init__(self, model, chat_id, messages):
        self.model = model
        self.chat_id = chat_id
        self.messages = messages

    def build(self, db: ChatDB):
        lines = []
        for message in self.messages:
            role = message["role"]
            content = message["content"]

            if role == "system" or role == "function" or "function_call" in message:
                continue

            lines.append(f'{role}: {content}')
        transcript = "\n".join(lines)

        try:
            c = Conversation(self.model, INSTRUCTIONS)
            print(f'Start on transcript of length {len(transcript)}')
            response = c.send(TextMessage.user(transcript))
            print("Have response from llm")
            edges = response.split("\n")
            for edge in edges:
                parts = edge.split("->")
                if len(parts) != 3:
                    print(f'Bad part in {edge}')
                    continue
                try:
                    lhs = db.add_node(parts[0])
                    relationship = parts[1]
                    rhs = db.add_node(parts[2])
                    db.add_edge(lhs, rhs, relationship, self.chat_id, f'{parts[0].lower()} {relationship} {parts[2].lower()}')
                except Exception as e:
                    print(self.messages)
                    print("YIELDS EDGES:")
                    print(edges)
                    log(e)
                    log(traceback.format_exc(e))
            print("Done")
        except Exception as e:
            print(str(e))


def process(model, db):
    checkpoint = db.get_checkpoint(CHECKPOINT_NAME)
    chat_id = db.get_chat_after_id(checkpoint)
    if chat_id is None:
        return False
    kgb = KnowledgeGraphBuilder(model, chat_id, db.get_messages(chat_id))
    kgb.build(db)
    db.set_checkpoint(CHECKPOINT_NAME, chat_id)
    return True


