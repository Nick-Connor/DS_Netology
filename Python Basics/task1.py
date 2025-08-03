# Input
phrase_1 = "How much easier would it be to write programs if it weren't for the customers"
phrase_2 = "640Kb should be enough for any task. Bill Gates (according to legend)"

# Determining the number of characters in phrase 1 and phrase 2
print("In phrase 1", len(phrase_1), "characters")
print("In phrase 2", len(phrase_2), "characters")

# Checking conditions
if len(phrase_1) > len(phrase_2):
    print ("Phrase 1 is longer than phrase 2")
elif len(phrase_1) < len(phrase_2):
    print("Phrase 2 is longer than phrase 1")
else:
    print("Phrases of equal length")