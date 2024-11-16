import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Agent:
    def __init__(self, name):
        self.name = name

    def propose_solution(self, iteration):
        try:
            proposal = f"Proposal from {self.name} at iteration {iteration}"
            logging.info(f"{self.name} proposed: {proposal}")
            return proposal
        except Exception as e:
            logging.error(f"Error in proposing solution: {e}")
            return None

    def respond_to_feedback(self, feedback, iteration):
        try:
            response = f"Response from {self.name} to feedback at iteration {iteration}"
            logging.info(f"{self.name} responded: {response}")
            return response
        except Exception as e:
            logging.error(f"Error in responding to feedback: {e}")
            return None

class Evaluator:
    def __init__(self):
        pass

    def evaluate_proposals(self, proposals, iteration):
        try:
            feedback = {}
            for agent_name, proposal in proposals.items():
                feedback[agent_name] = f"Feedback for {agent_name} at iteration {iteration}"
                logging.info(f"Evaluator feedback to {agent_name}: {feedback[agent_name]}")
            return feedback
        except Exception as e:
            logging.error(f"Error in evaluating proposals: {e}")
            return {}

def main():
    agents = [Agent("Agent1"), Agent("Agent2"), Agent("Agent3")]
    evaluator = Evaluator()
    num_iterations = 4

    for iteration in range(1, num_iterations + 1):
        logging.info(f"Iteration {iteration} - Proposals")
        proposals = {agent.name: agent.propose_solution(iteration) for agent in agents}
        for agent_name, proposal in proposals.items():
            if proposal:
                print(f"{agent_name}: {proposal}")

        logging.info(f"Iteration {iteration} - Responses")
        feedback = evaluator.evaluate_proposals(proposals, iteration)
        for agent_name, fb in feedback.items():
            if fb:
                print(f"Evaluator to {agent_name}: {fb}")
                agent = next(a for a in agents if a.name == agent_name)
                response = agent.respond_to_feedback(fb, iteration)
                if response:
                    print(f"{agent_name}: {response}")

if __name__ == "__main__":
    main()