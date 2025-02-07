from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# Charger le texte nettoyé
input_file = "/../../data/wikipedia_clean.txt"

with open(input_file, "r", encoding="utf-8") as f:
    sentences = [simple_preprocess(line) for line in f]

# Entraîner Word2Vec (Skip-gram) avec plusieurs workers
model = Word2Vec(sentences=sentences, vector_size=200, window=5, min_count=5, sg=1, workers=8)

# Sauvegarde du modèle
model.save("/../models/word2vec/word2vec_fr.model")

print("✅ Modèle entraîné et sauvegardé !")
