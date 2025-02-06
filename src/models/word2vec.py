from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Download the punkt tokenizer for word tokenization
# Uncomment the line below if you haven't downloaded the punkt tokenizer
#nltk.download('punkt')

# Sample text data
text_data = [
    "This is the first sentence.",
    "Here is another sentence.",
    "Word2Vec is a great tool for learning word representations.",
    "We are creating word embeddings using Word2Vec."
]

# Tokenize the sentences into words
tokenized_data = [word_tokenize(sentence.lower()) for sentence in text_data]

# Create the Word2Vec model
model = Word2Vec(sentences=tokenized_data, vector_size=100, window=5, min_count=1, workers=4)

# Save the model
model.save("word2vec.model")

# Load the model
model = Word2Vec.load("word2vec.model")

# Get the vector for a specific word
word_vector = model.wv['word2vec']

print(word_vector)