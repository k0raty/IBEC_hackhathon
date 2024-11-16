
### debugger_agent.py

import random

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
