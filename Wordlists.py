class Wordlists:

    def __init__(self):
        self.nouns = [line.rstrip('\n') for line in open('nounlist.txt', 'rU')]
        self.verbs = [line.rstrip('\n') for line in open('verblist.txt', 'rU')]
        self.adjectives = [line.rstrip('\n') for line in open('adjlist.txt', 'rU')]
        self.adverbs = [line.rstrip('\n') for line in open('adverbs.txt', 'rU')]
        self.conjunctions = [line.rstrip('\n') for line in open('conjunctions.txt', 'rU')]
        self.prepositions = [line.rstrip('\n') for line in open('prepositions.txt', 'rU')]
        self.questions = [line.rstrip('\n') for line in open('questions.txt', 'rU')]
        self.qualifiers = [line.rstrip('\n') for line in open('qualifiers.txt', 'rU')]
