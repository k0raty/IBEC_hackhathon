class EvaluatorAgent:
    def evaluate_permutation(self, word, correct_word):
        # Evaluate the permutation based on similarity and positional distance to the correct word
        similarity = sum(a == b for a, b in zip(word, correct_word)) / len(correct_word)
        positional_distance = sum(abs(word.index(a) - correct_word.index(b)) for a, b in zip(word, correct_word)) / len(correct_word)
        score = similarity - (positional_distance / len(correct_word))
        return score
