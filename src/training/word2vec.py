from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# Charger le corpus
with open("corpus_wikipedia_fr.txt", "r", encoding="utf-8") as f:
    sentences = [simple_preprocess(line) for line in f]

# Entraîner Word2Vec (Skip-gram)
model = Word2Vec(sentences=sentences, vector_size=100, window=5, min_count=5, sg=1, workers=4)

# Sauvegarde du modèle
model.save("word2vec_fr.model")

# Exemple d'utilisation
print(model.wv.most_similar("intelligence"))
