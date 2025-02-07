from datasets import load_dataset

# Charger le dataset Hugging Face (nécessite d'être authentifié)
dataset = load_dataset("bigscience-data/roots_fr_wikipedia", split="train")

# Sauvegarde du texte des articles
output_file = "./wikipedia_fr.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for article in dataset:
        text = article.get("text", "").strip()  # Récupère le texte propre
        if text:  # Évite les textes vides
            f.write(text + "\n\n")  # Ajoute un saut de ligne entre articles

print(f"✅ Dataset sauvegardé dans {output_file}")

