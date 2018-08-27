# DEPENDENCIES
import secrets
import math
import Wordlists
import Structures

# MACROS
w = Wordlists.Wordlists()
s = Structures.Structures()

# MAIN FUNCTION 
def welcome():

    # Print menu
    print("Welcome to the passSentence Generator.")
    print("Please choose your password strength:")
    print("[0] Basic Strength (~44 bits entropy)")
    print("[1] Extra Strength (~77 bits entropy)")
    print("[2] Cryptographic Strenth (~128 bits entropy)")

    # Get input
    char = raw_input(">> ")

    # Process input
    if int(char) == 0:
        genBasicSentence()
    elif int(char) == 1:
        genMediumSentence()
    elif int(char) == 2:
        genCryptoSentence()

# SUBFUNCTIONS
# Generates "simple structure" pass senstence ~44 bits entropy
def genBasicSentence():
    structure = secrets.choice(s.simple)
    sentence, punct = constructSentence(structure)
    print ">> " + sentence + punct

# Generates "complex structure" pass sentence ~77 bits entropy
def genMediumSentence():
    structure = secrets.choice(s.complex)
    sentence, punct = constructSentence(structure)
    print sentence + punct

# Generates simple + complex structure pass sentence ~128 bits entropy
def genCryptoSentence():
    structure1 = secrets.choice(s.simple)
    structure2 = secrets.choice(s.complex)
    part1, punct1 = constructSentence(structure1)
    part2, punct2 = constructSentence(structure2)
    connector = secrets.choice(w.conjunctions)
    sentence = part1 + ', ' + connector + ' ' + part2 + punct1
    print sentence

# Constructs sentence from input structure; returns tuple (sentence, punt)
def constructSentence(s):
    sentence = ""
    punct = '.'
    for i in range(len(s)):
        if s[i] == 'U':
            sentence += secrets.choice(w.questions)
            punct = '?'
        elif s[i] == 'N':
            sentence += secrets.choice(w.nouns)
        elif s[i] == 'V':
            sentence += secrets.choice(w.verbs)
        elif s[i] == 'A':
            sentence += secrets.choice(w.adjectives)
        elif s[i] == 'L':
            sentence += secrets.choice(w.adverbs)
        elif s[i] == 'C':
            sentence += secrets.choice(w.conjunctions)
        elif s[i] == 'P':
            sentence += secrets.choice(w.prepositions)
        elif s[i] == 'Q':
            sentence += secrets.choice(w.qualifiers)
        elif s[i] == ',':
            sentence += ','
        elif s[i] == '&':
            sentence += 'and'
        elif s[i] == 't':
            sentence += 'the'
        if i != len(s) - 1 and s[i+1] != ',':
            sentence += ' '
    return sentence, punct

# TEST FUNCTIONS
# Calculates (and returns) the number of possible sentences with input structure
def calcSentCombos(s):
    combs = 1
    for i in range(len(s)):
        if s[i] == 'N':
            entropy*= len(w.nouns)
        elif s[i] == 'V':
            combs *= len(w.verbs)
        elif s[i] == 'A':
            combs *= len(w.adjectives)
        elif s[i] == 'L':
            combs *= 1500
        elif s[i] == 'C':
            combs *= len(w.conjunctions)
        elif s[i] == 'P':
            combs *= len(w.prepositions)
        elif s[i] == 'U':
            combs *= len(w.questions)
        elif s[i] == 'Q':
            combs *= len(w.qualifiers)
    return combs

# Calculates (and returns) the bits of entropy over all simple structures using calcSentCombos
def calcBasicEntropy():
    combs = 0
    for i in range(len(s.simple)):
        entropy += (calcSentCombos(s.simple[i]))
    return math.log(combs, 2)

# Calculates (and returns) the bits of entropy over all complex structures using calcSentCombos
def calcMediumEntropy():
    entropy = 0
    for i in range(len(s.complex)):
        combs += (calcSentCombos(s.complex[i]))
    return math.log(combs, 2)

# Calculates (and returns) the bits of entropy over all simple + complex structures using calcSentCombos
def calcCryptoEntropy():
    combs = 0
    c = len(w.conjunctions)
    for i in range(len(s.simple)):
        for j in range(len(s.complex)):
            combs += (calcSentCombos(s.simple[i])*c*calcSentCombos(s.complex[j]))
    return math.log(combs, 2)

# Calculates (and returns) the bits of entropy over all test structures using calcSentCombos
def calcTestEntropy():
    combs = 0
    c = len(w.conjunctions)
    for i in range(len(s.testE)):
        for j in range(len(s.testE)):
            combs += (calcSentCombos(s.testE[i])*c*calcSentCombos(s.testE[j]))
    return math.log(combs, 2)

welcome()

# Testing calls
#print(calcBasicEntropy())
#print(calcMediumEntropy())
#print(calcCryptoEntropy())
#print(calcTestEntropy())
#print(len(w.adverbs))
