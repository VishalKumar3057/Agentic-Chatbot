from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        # 1. Extract messages
        messages = state["messages"]
        # 2. Get response from LLM
        response = self.llm.invoke(messages)
        # 3. Return updated state
        return {"messages": response}
