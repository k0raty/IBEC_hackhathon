import subprocess

class CompilerAgent:
    def __init__(self, name):
        self.name = name

    def compile_code(self, file_path):
        """
        Compiles the code in the given Python file.

        :param file_path: Path to the Python file to be compiled.
        :return: True if the code compiles successfully, False otherwise.
        """
        try:
            result = subprocess.run(['python', file_path], capture_output=True, text=True)
            if result.returncode == 0:
                return True
            else:
                print(f"Compilation error: {result.stderr}")
                return False
        except Exception as e:
            print(f"Error compiling file: {e}")
            return False

# Example Usage
if __name__ == "__main__":
    # Define the file path of the code you want to compile (e.g., "sample.py")
    file_path = "sample_code.py"  # Replace with the path to your file

    # Create a CompilerAgent instance
    compiler_agent = CompilerAgent(name="CompilerAgent")

    # Call the function to compile the code
    compilation_successful = compiler_agent.compile_code(file_path)

    # Print the result
    if compilation_successful:
        print("Compilation successful!")
    else:
        print("Compilation failed.")
