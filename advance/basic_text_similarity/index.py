# Basic Text Similarity (No AI)

def preprocess(text):
    # lowercase + split words
    text = text.lower()
    words = text.split()
    return set(words)

def similarity(text1, text2):
    words1 = preprocess(text1)
    words2 = preprocess(text2)

    common_words = words1.intersection(words2)
    total_words = words1.union(words2)

    similarity_percentage = (len(common_words) / len(total_words)) * 100
    return similarity_percentage


# ---- TEST ----
text_a = "Python supports object oriented programming"
text_b = "Python has object oriented programming concepts"

score = similarity(text_a, text_b)

print("Similarity:", round(score, 2), "%")
