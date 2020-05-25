import pickle
import spacy

spc = spacy.load("en_core_web_md")

# pickle
f = open('spacy.pckl', 'wb')
pickle.dump(spc, f)
f.close()
