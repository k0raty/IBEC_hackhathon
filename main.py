import random
import logging
from debugger_agent import DebuggerAgent
from evaluator_agent import EvaluatorAgent
from plotting import plot_results
import networkx as nx

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize agents
debugger_agents = [DebuggerAgent(name) for name in ["Agent1", "Agent2", "Agent3"]]
evaluator_agent = EvaluatorAgent()

# Example word to be corrected
word = "hleol"
correct_word = "hello"

# RL Loop
best_score = 0
best_word = word
nash_equilibrium_reached = False
iterations = 0
max_iterations = 100  # Set a maximum number of iterations for the loop
previous_permutations = set()
previous_best_score = 0  # Initialize previous_best_score

# Lists to store scores and words for plotting
scores = []
words = []
exploration_iterations = []  # Store iterations where exploration occurs

# Exploration probability
exploration_probability = 0.1

# Initialize lists to store communication graphs for each iteration
proposal_graphs = []
response_graphs = []

while not nash_equilibrium_reached and iterations < max_iterations:
    iterations += 1
    logging.debug(f"Iteration {iterations}")

    # Debugger Agents
    proposed_permutations = [agent.propose_permutation(best_word) for agent in debugger_agents]

    # Evaluator Agent
    scores_iter = [evaluator_agent.evaluate_permutation(perm, correct_word) for perm in proposed_permutations]

    # Log each proposed permutation and its score
    for perm, score in zip(proposed_permutations, scores_iter):
        logging.debug(f"Proposed Word: {perm}, Score: {score}")

    # Select the best permutation based on the score
    best_score_index = max(range(len(scores_iter)), key=lambda i: scores_iter[i])
    best_word_candidate = proposed_permutations[best_score_index]
    best_score_candidate = scores_iter[best_score_index]

    # Exploration mechanism
    if random.random() < exploration_probability:
        logging.debug("Exploring a new permutation.")
        best_word = best_word_candidate
        best_score = best_score_candidate
        exploration_iterations.append(iterations)  # Record the exploration iteration
    else:
        # Accept only improving permutations
        if best_score_candidate >= best_score:
            best_word = best_word_candidate
            best_score = best_score_candidate

    logging.debug(f"Best Word: {best_word}, Best Score: {best_score}")

    # Add the best word to the set of previous permutations to avoid
    previous_permutations.add(best_word)

    # Store the score and word for plotting
    scores.append(best_score)
    words.append(best_word)

    # Create new communication graphs for the current iteration
    proposal_graph = nx.DiGraph()
    response_graph = nx.DiGraph()

    # Add nodes for each agent
    for agent in debugger_agents:
        proposal_graph.add_node(agent.name)
        response_graph.add_node(agent.name)
    proposal_graph.add_node("Evaluator")
    response_graph.add_node("Evaluator")

    # Add edges for communication between agents for the current iteration
    for i, agent in enumerate(debugger_agents):
        proposal_graph.add_edge(agent.name, "Evaluator", label=f"{proposed_permutations[i]} - Iter {iterations} - Score {scores_iter[i]:.2f}")
        response_graph.add_edge("Evaluator", agent.name, label=f"{best_word} - Iter {iterations} - Score {best_score:.2f}")

    # Store the communication graphs for the current iteration
    proposal_graphs.append(proposal_graph)
    response_graphs.append(response_graph)

    # Check for Nash equilibrium
    if best_score == 1:
        nash_equilibrium_reached = True
        logging.debug("Nash equilibrium reached. The word is correct.")
    elif best_score > previous_best_score:
        logging.debug("System is evolving. Overall score increased.")

    previous_best_score = best_score

# Final output
logging.debug("Final Word:")
logging.debug(f"{best_word}")
logging.debug(f"Final Score: {best_score}")

# Plot the results
plot_results(scores, words, exploration_iterations, proposal_graphs, response_graphs)
