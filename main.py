import logging
from debugger_agent import DebuggerAgent
from optimizer_agent import OptimizerAgent
from compiler_agent import CompilerAgent
from integrator_agent import IntegratorAgent
from plotting import plot_results

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize agents
debugger_agent = DebuggerAgent(name="DebuggerAgent")
optimizer_agent = OptimizerAgent(name="OptimizerAgent")
compiler_agent = CompilerAgent(name="CompilerAgent")
integrator_agent = IntegratorAgent(name="IntegratorAgent")

# Example file path to be corrected
file_path = "sample_code.py"  # Replace with the path to your file

# RL Loop
best_score = 0
best_code = ""
nash_equilibrium_reached = False
iterations = 0
max_iterations = 100  # Set a maximum number of iterations for the loop
previous_codes = set()
previous_best_score = 0  # Initialize previous_best_score

# Lists to store scores and codes for plotting
scores = []
codes = []
exploration_iterations = []  # Store iterations where exploration occurs

# Exploration probability
exploration_probability = 0.1

# Initialize lists to store communication graphs for each iteration
proposal_graphs = []
response_graphs = []

while not nash_equilibrium_reached and iterations < max_iterations:
    iterations += 1
    logging.debug(f"Iteration {iterations}")

    # Debugger Agent
    debugged_code = debugger_agent.debug_code(file_path)

    # Optimizer Agent
    optimized_code = optimizer_agent.optimize_code(file_path)

    # Compiler Agent
    compilation_successful = compiler_agent.compile_code(file_path)

    # Integrator Agent
    integrated_code = integrator_agent.integrate_code(debugged_code)

    # Evaluate the code
    if compilation_successful:
        best_score = 1
        best_code = integrated_code
    else:
        best_score = 0

    logging.debug(f"Best Code: {best_code}, Best Score: {best_score}")

    # Add the best code to the set of previous codes to avoid
    previous_codes.add(best_code)

    # Store the score and code for plotting
    scores.append(best_score)
    codes.append(best_code)

    # Create new communication graphs for the current iteration
    proposal_graph = nx.DiGraph()
    response_graph = nx.DiGraph()

    # Add nodes for each agent
    proposal_graph.add_node("DebuggerAgent")
    proposal_graph.add_node("OptimizerAgent")
    proposal_graph.add_node("CompilerAgent")
    proposal_graph.add_node("IntegratorAgent")
    response_graph.add_node("DebuggerAgent")
    response_graph.add_node("OptimizerAgent")
    response_graph.add_node("CompilerAgent")
    response_graph.add_node("IntegratorAgent")

    # Add edges for communication between agents for the current iteration
    proposal_graph.add_edge("DebuggerAgent", "IntegratorAgent", label=f"Debugged Code - Iter {iterations} - Score {best_score:.2f}")
    response_graph.add_edge("IntegratorAgent", "DebuggerAgent", label=f"Integrated Code - Iter {iterations} - Score {best_score:.2f}")

    # Store the communication graphs for the current iteration
    proposal_graphs.append(proposal_graph)
    response_graphs.append(response_graph)

    # Check for Nash equilibrium
    if best_score == 1:
        nash_equilibrium_reached = True
        logging.debug("Nash equilibrium reached. The code is correct.")
    elif best_score > previous_best_score:
        logging.debug("System is evolving. Overall score increased.")

    previous_best_score = best_score

# Final output
logging.debug("Final Code:")
logging.debug(f"{best_code}")
logging.debug(f"Final Score: {best_score}")

# Plot the results
plot_results(scores, codes, exploration_iterations, proposal_graphs, response_graphs)
