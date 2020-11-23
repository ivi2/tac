"""Playing with word2vec model"""

#%%
from gensim.models import Word2Vec
from pprint import pprint

model = Word2Vec.load("../data/bulletins.model")

word1 = "maladie"
pprint(model.wv[word1])

#%%
word2 = "marché"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
word2 = "judiciaire"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
pprint(model.wv.most_similar("orphelines", topn=3))

#%%
pprint(model.wv.most_similar("villes"))

#%%
pprint(model.wv.most_similar(positive=['nivelles', 'france'], negative=['belgique']))
