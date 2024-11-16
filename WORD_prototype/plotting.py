import matplotlib.pyplot as plt
import networkx as nx

def plot_results(scores, words, exploration_iterations, proposal_graphs, response_graphs):
    # Plot the overall score evolution and words found at each iteration
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='-', color='b', label='Score Evolution')

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
