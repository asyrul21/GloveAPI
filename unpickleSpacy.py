import pickle
import spacy

# unpickle
f = open('spacy.pckl', 'rb')
loadedSpc = pickle.load(f)
f.close()

nlp = spacy.load(loadedSpc)

# wes = loadedSpc("hello there")

# for token in wes.tokens:
#     print(token.text)
