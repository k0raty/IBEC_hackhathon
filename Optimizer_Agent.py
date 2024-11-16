from langchain_huggingface import HuggingFacePipeline  # Use the updated class
from transformers import pipeline

# Load a Hugging Face model and tokenizer
generator = pipeline('text-generation', model='gpt2')

# Set max_length and max_new_tokens to handle long inputs
generator.model.config.max_length = 1024  # Increase max_length
generator.model.config.max_new_tokens = 200  # Generate more tokens if necessary

# Create the LLM with the updated pipeline
llm = HuggingFacePipeline(pipeline=generator)

class OptimizerAgent:
    def __init__(self, name):
        self.name = name

    def get_code_from_file(self, file_path):
        """
        Reads the content of a Python file.

        :param file_path: Path to the Python file.
        :return: The content of the file as a string.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def optimize_code(self, file_path):
        """
        Optimizes the code in the given Python file using a Hugging Face model.

        :param file_path: Path to the Python file to be optimized.
        :return: The optimized code.
        """
        # Step 1: Read the code from the file
        code = self.get_code_from_file(file_path)
        if not code:
            return "Failed to read the file. Please check the file path."

        # Step 2: Send the code to the Hugging Face model for optimization
        prompt = f"Here is a Python code that can be optimized:\n{code}\n\nOptimize it."

        # Use the Hugging Face model to generate the optimized code
        optimized_code = llm.invoke(prompt)  # Use .invoke() instead of .__call__()

        return optimized_code

# Example Usage
if __name__ == "__main__":
    # Define the file path of the code you want to optimize (e.g., "sample.py")
    file_path = "sample_code.py"  # Replace with the path to your file

    # Create an OptimizerAgent instance
    optimizer_agent = OptimizerAgent(name="OptimizerAgent")

    # Call the function to optimize the code
    optimized_code = optimizer_agent.optimize_code(file_path)

    # Print the optimized code
    print("\nOptimized Code:\n")
    print(optimized_code)
