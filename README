
### README.md

```markdown
# Multi-Agent System for Word Correction

## Overview

This project implements a multi-agent system for correcting words using a reinforcement learning (RL) approach. The system consists of debugger agents that propose permutations of a word and an evaluator agent that evaluates these permutations based on similarity and positional distance. The goal is to reach a Nash equilibrium where the word is correctly spelled.

## Features

### Classes

1. **DebuggerAgent**:
   - Proposes random permutations of the letters in a word.
   - Ensures that each agent does not propose the same word again by keeping track of proposed permutations.

2. **EvaluatorAgent**:
   - Evaluates the permutations based on similarity to the correct word and positional distance of letters.
   - Calculates a score that combines similarity and positional distance.

### Game Theory Concept

The system uses a game theory concept where agents compete to propose the best permutation. The evaluator agent communicates the best permutation back to the agents, and the process continues until a Nash equilibrium is reached, where the word is correctly spelled.

### Avoiding Local Optimum

To avoid falling into a local optimum, the system includes an exploration mechanism. With a certain probability, the system accepts permutations that may temporarily decrease the score, allowing it to explore new possibilities and escape local optima.

### Plotting

The system visualizes the overall score evolution and the words found at each iteration. It also plots the communication between agents for the last 3 iterations in separate subplots for proposals and responses. This helps in understanding the interactions and the progress of the system.

## Possible Extensions

### Code Correction

The current implementation can be extended to correct code instead of words. Each agent can propose corrections to a piece of code, and the evaluator agent can evaluate these corrections based on syntax correctness, logical errors, and performance improvements. The system can then iterate to find the best correction.

## File Structure

- `debugger_agent.py`: Script for the DebuggerAgent class.
- `evaluator_agent.py`: Script for the EvaluatorAgent class.
- `main.py`: Main function to run the word correction process.
- `plotting.py`: Script for plotting the score evolution and communication graphs.

## Usage

1. Run the main function to start the word correction process.
2. The plotting function will visualize the score evolution and communication graphs.

## Requirements

- Python 3.x
- matplotlib
- networkx

## Installation

```sh
pip install matplotlib networkx
