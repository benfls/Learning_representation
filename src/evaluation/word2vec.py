from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt

# Charger le modèle
model = Word2Vec.load("src\models\word2vec\word2vec_fr.model")

# Tester les mots les plus proches
print(model.wv.most_similar("plantes"))
print(model.wv.most_similar(positive=["roi", "femme"], negative=["homme"]))

# Récupérer la liste des mots du vocabulaire
words = list(model.wv.index_to_key)

# Extraire les vecteurs correspondants
word_vectors = np.array([model.wv[word] for word in words])
from sklearn.manifold import TSNE
# Réduire à 2D avec t-SNE (lent sur un grand vocabulaire)
tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=5000)
word_vectors_tsne = tsne.fit_transform(word_vectors[:150])  # On prend les 300 premiers mots

# Tracer le graphique
plt.figure(figsize=(12, 8))
plt.scatter(word_vectors_tsne[:, 0], word_vectors_tsne[:, 1], alpha=0.5)

# Ajouter les étiquettes des mots
for i, word in enumerate(words[:150]):  
    plt.annotate(word, (word_vectors_tsne[i, 0], word_vectors_tsne[i, 1]), fontsize=9, alpha=0.7)

plt.title("Visualisation Word2Vec avec t-SNE")
plt.show()
