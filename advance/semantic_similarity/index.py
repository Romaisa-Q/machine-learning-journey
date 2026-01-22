from sentence_transformers import SentenceTransformer, util

# Load pretrained model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
text_a = "Python supports object oriented programming"
text_b = "Python has object oriented programming concepts"

# Convert text to embeddings
embedding_a = model.encode(text_a)
embedding_b = model.encode(text_b)

# Calculate cosine similarity
similarity_score = util.cos_sim(embedding_a, embedding_b)

print("Semantic Similarity Score:", similarity_score.item())
