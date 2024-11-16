from langchain_huggingface import HuggingFacePipeline  # Use the updated class
from transformers import pipeline

# Load a Hugging Face model and tokenizer
generator = pipeline('text-generation', model='gpt2')

# Set max_length and max_new_tokens to handle long inputs
generator.model.config.max_length = 1024  # Increase max_length
generator.model.config.max_new_tokens = 200  # Generate more tokens if necessary

# Create the LLM with the updated pipeline
llm = HuggingFacePipeline(pipeline=generator)

def get_code_from_file(file_path):
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


def debug_code(file_path):
    """
    Debugs the code in the given Python file using a Hugging Face model.
    
    :param file_path: Path to the Python file to be debugged.
    :return: The corrected code.
    """
    # Step 1: Read the code from the file
    code = get_code_from_file(file_path)
    if not code:
        return "Failed to read the file. Please check the file path."

    # Step 2: Send the code to the HuggingFace model for debugging
    prompt = f"Here is a Python code with errors:\n{code}\n\nFix it."

    # Use the HuggingFace model to generate the corrected code
    corrected_code = llm.invoke(prompt)  # Use .invoke() instead of .__call__()

    return corrected_code


# Example Usage
if __name__ == "__main__":
    # Define the file path of the code you want to debug (e.g., "sample.py")
    file_path = "sample_code.py"  # Replace with the path to your file

    # Call the function to debug the code
    corrected_code = debug_code(file_path)

    # Print the corrected code
    print("\nCorrected Code:\n")
    print(corrected_code)