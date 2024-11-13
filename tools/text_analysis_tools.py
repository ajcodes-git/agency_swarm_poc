from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from groq import Groq

# Constants
MODEL_ID = "llama3-groq-70b-8192"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class TextInsightTool(BaseTool):
    """
    Analyzes input text using Groq's high-performance LLMs and produces human-readable insights.
    Utilizes the llama3-groq-70b model with Retrieval-Augmented Generation (RAG) for contextual accuracy.
    """

    text_input: str = Field(..., description="The text data or command output to analyze and generate insights from.")

    def run(self):
        """
        The run method processes the text input using Groq's model with RAG to generate insightful and human-readable summaries.
        """
        client = Groq(api_key=GROQ_API_KEY)
        
        # Set up messages with a system prompt to guide the model's response
        messages = [
            {"role": "system", "content": "You are a helpful assistant who generates clear, human-readable insights from technical or complex information, code, or terminal commands."},
            {"role": "user", "content": self.text_input}
        ]
        
        try:
            # Request completion from Groq model
            completion = client.chat.completions.create(
                messages=messages,
                model=MODEL_ID,
                temperature=0.5,  # Ensures balanced responses
                max_tokens=1024,  # Control output length for readability
                top_p=1,  # Full consideration for likelihood-weighted options
                stream=False
            )
            
            # Output response
            insight = completion.choices[0].message.content
            return insight

        except Exception as e:
            return f"An error occurred while processing the text: {e}"

# Test tool
if __name__ == "__main__":
    # Example usage with a sample text input
    text_input = "Sample log output: Connection to database failed at 14:32 due to timeout. Retry attempts exceeded limits."
    tool = TextInsightTool(text_input=text_input)
    print(tool.run())
