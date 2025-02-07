import re

# Charger le texte
input_file = "/../../data/wikipedia_fr.txt"
output_file = "/../../data/wikipedia_clean.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.readlines()

# Fonction de nettoyage du texte
def clean_text(text):
    text = text.lower()  # Convertir en minuscules
    text = re.sub(r"\s+", " ", text)  # Supprimer espaces multiples
    text = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ ]", "", text)  # Garder lettres et accents
    return text.strip()

# Nettoyer chaque ligne
cleaned_text = [clean_text(line) for line in text if line.strip()]

# Sauvegarde
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_text))

print(f"✅ Texte nettoyé et sauvegardé dans {output_file}")