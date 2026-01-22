from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Course topics
course_topics = [
    "Object Oriented Programming in Python",
    "Loops in Python",
    "Functions in Python",
    "Exception Handling",
    "File Handling"
]

# Exam questions
exam_questions = [
    "Explain inheritance in Python",
    "What is a for loop?",
    "How do you handle errors in Python?"
]

# Convert to embeddings
topic_embeddings = model.encode(course_topics)
question_embeddings = model.encode(exam_questions)

threshold = 0.5  # similarity threshold

covered = []
not_covered = []

for i, topic in enumerate(course_topics):
    similarities = util.cos_sim(topic_embeddings[i], question_embeddings)
    max_similarity = similarities.max().item()

    if max_similarity >= threshold:
        covered.append((topic, round(max_similarity, 2)))
    else:
        not_covered.append((topic, round(max_similarity, 2)))

# Results
total_topics = len(course_topics)
covered_count = len(covered)
coverage_percentage = (covered_count / total_topics) * 100

print("Coverage Percentage:", round(coverage_percentage, 2), "%\n")

print("Covered Topics:")
for t in covered:
    print("-", t)

print("\nNot Covered Topics:")
for t in not_covered:
    print("-", t)

