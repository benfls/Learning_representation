from gensim.models import Word2Vec

# Charger le modèle
model = Word2Vec.load("word2vec_fr.model")

# Trouver les mots les plus proches de "intelligence"
print(model.wv.most_similar("intelligence"))

# Tester une relation sémantique : Roi - Homme + Femme ≈ Reine
print(model.wv.most_similar(positive=["roi", "femme"], negative=["homme"]))
