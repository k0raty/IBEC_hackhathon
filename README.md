# Multi-Agent System for Code Correction

## Overview

This project implements a multi-agent system for correcting code using a reinforcement learning (RL) approach. The system consists of debugger agents that propose corrections to the code, an optimizer agent that optimizes the code, a compiler agent that compiles the code, and an integrator agent that ensures the code is unique and not previously seen. The goal is to reach a Nash equilibrium where the code is correctly compiled and optimized.

## Features

### Classes

1. **DebuggerAgent**:
   - Proposes corrections to the code using a Hugging Face model.
   - Ensures that each agent does not propose the same code again by keeping track of proposed corrections.

2. **OptimizerAgent**:
   - Optimizes the code using a Hugging Face model.
   - Ensures that the code is optimized for performance and readability.

3. **CompilerAgent**:
   - Compiles the code to check for syntax errors.
   - Ensures that the code compiles successfully.

4. **IntegratorAgent**:
   - Integrates the code by ensuring it is unique and not previously seen.
   - Modifies the code if necessary to ensure uniqueness.

### Game Theory Concept

The system uses a game theory concept where agents compete to propose the best correction. The integrator agent communicates the best correction back to the agents, and the process continues until a Nash equilibrium is reached, where the code is correctly compiled and optimized.

### Avoiding Local Optimum

To avoid falling into a local optimum, the system includes an exploration mechanism. With a certain probability, the system accepts corrections that may temporarily decrease the score, allowing it to explore new possibilities and escape local optima.

### Plotting

The system visualizes the overall score evolution and the codes found at each iteration. It also plots the communication between agents for the last 3 iterations in separate subplots for proposals and responses. This helps in understanding the interactions and the progress of the system.

## File Structure

- `debugger_agent.py`: Script for the DebuggerAgent class.
- `optimizer_agent.py`: Script for the OptimizerAgent class.
- `compiler_agent.py`: Script for the CompilerAgent class.
- `integrator_agent.py`: Script for the IntegratorAgent class.
- `main.py`: Main function to run the code correction process.
- `plotting.py`: Script for plotting the score evolution and communication graphs.

## Usage

1. Run the main function to start the code correction process.
2. The plotting function will visualize the score evolution and communication graphs.

## Requirements

- Python 3.x
- matplotlib
- networkx
- transformers
- langchain_huggingface

## Installation

```sh
pip install matplotlib networkx transformers langchain_huggingface
