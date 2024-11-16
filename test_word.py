import random
import logging
import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class DebuggerAgent:
    def __init__(self, name):
        self.name = name
        self.proposed_permutations = set()

    def propose_permutation(self, word):
        # Propose a random permutation of the letters in the word
        while True:
            perm = ''.join(random.sample(word, len(word)))
            if perm not in self.proposed_permutations:
                self.proposed_permutations.add(perm)
                return perm

class EvaluatorAgent:
    def evaluate_permutation(self, word, correct_word):
        # Evaluate the permutation based on similarity and positional distance to the correct word
        similarity = sum(a == b for a, b in zip(word, correct_word)) / len(correct_word)
        positional_distance = sum(abs(word.index(a) - correct_word.index(b)) for a, b in zip(word, correct_word)) / len(correct_word)
        score = similarity - (positional_distance / len(correct_word))
        return score

# Initialize agents
debugger_agents = [DebuggerAgent(name) for name in ["Agent1", "Agent2", "Agent3"]]
evaluator_agent = EvaluatorAgent()

# Example word to be corrected
word = "loehl"
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

# Plot the overall score evolution and words found at each iteration
plt.figure(figsize=(10, 5))
plt.plot(range(1, iterations + 1), scores, marker='o', linestyle='-', color='b', label='Score Evolution')

# Highlight exploration points in red
for idx in exploration_iterations:
    plt.plot(idx, scores[idx - 1], 'ro')  # Plot exploration points in red

plt.xlabel('Iteration')
plt.ylabel('Score')
plt.title('Overall Score Evolution')
plt.legend()

# Annotate the words found at each iteration
for i, word in enumerate(words):
    plt.annotate(word, (i + 1, scores[i]), textcoords="offset points", xytext=(0, 5), ha='center')

plt.show()

# Plot the communication graphs for the last 3 iterations
num_iterations = len(proposal_graphs)
start_index = max(0, num_iterations - 3)

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))

for i in range(start_index, num_iterations):
    row = i - start_index

    # Plot proposal graph
    pos = nx.spring_layout(proposal_graphs[i], k=0.5, iterations=50)
    labels = nx.get_edge_attributes(proposal_graphs[i], 'label')
    nx.draw(proposal_graphs[i], pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrows=True, ax=axes[row, 0])
    nx.draw_networkx_edge_labels(proposal_graphs[i], pos, edge_labels=labels, font_size=8, font_color='red', ax=axes[row, 0])
    axes[row, 0].set_title(f'Iteration {i + 1} - Proposals')

    # Plot response graph
    pos = nx.spring_layout(response_graphs[i], k=0.5, iterations=50)
    labels = nx.get_edge_attributes(response_graphs[i], 'label')
    nx.draw(response_graphs[i], pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrows=True, ax=axes[row, 1])
    nx.draw_networkx_edge_labels(response_graphs[i], pos, edge_labels=labels, font_size=8, font_color='red', ax=axes[row, 1])
    axes[row, 1].set_title(f'Iteration {i + 1} - Responses')

plt.tight_layout()
plt.show()
