from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
from typing import Any, Dict, Optional, Tuple

class CustomConversationBufferMemory(ConversationBufferMemory):

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """Save context from this conversation to buffer."""
        input_str, output_str = self._get_input_output(inputs, outputs)
        self.chat_memory.add_user_message(input_str)
        self.chat_memory.add_ai_message(str(output_str))



class MemoryHelper:
    """
        Manages memory for agent. Takes in the promptflow managed memory and
        can reformat it for different arbitration method's memory classes
    """

    def __init__(self, history):
        self.history = history

    
    def use_history(self):
        if len(self.history) != 0:
            return True
        return False

    def as_langchain_memory(self):
        print(f"HELLLLOOOOOOOOOO")
        chat_history = ChatMessageHistory()
        for chat in self.history:
            inputs = chat["inputs"]
            input_str = ""
            for input_name in inputs.keys():
                if isinstance(inputs[input_name],str):
                    input_str += inputs[input_name]
            
            chat_history.add_user_message(input_str)
                
            outputs = chat["outputs"]
            output_str = ""
            for output_name in outputs.keys():
                if isinstance(outputs[output_name],str):
                    output_str += outputs[output_name]
            chat_history.add_ai_message(output_str)
        # TODO: Make memory_key a constant
        memory = CustomConversationBufferMemory(memory_key="chat_history", chat_memory=chat_history)
        return memory

    def as_semantic_kernel_memory(self):
        history_messages = []
        for chat in self.history:
            inputs = chat["inputs"]
            input_str = "User: "
            for input_name in inputs.keys():
                input_str += inputs[input_name]
            history_messages.append(
            input_str
            )
            
            outputs = chat["outputs"]
            output_str = "Bot: "
            for output_name in outputs.keys():
                output_str += outputs[output_name]
            history_messages.append(
                output_str
            )
        history_str = "\n".join(history_messages)
        return history_str

    def as_openai_function_memory(self):
        history_messages = []
        for chat in self.history:
            inputs = chat["inputs"]
            input_str = ""
            for input_name in inputs.keys():
                input_str += inputs[input_name]
            history_messages.append(
                {
                    "role": "user",
                    "content": input_str
                }
            )
            
            outputs = chat["outputs"]
            output_str = ""
            for output_name in outputs.keys():
                output_str += outputs[output_name]
            history_messages.append(
                {
                    "role": "assistant",
                    "content": output_str
                }
            )
        return history_messages
        