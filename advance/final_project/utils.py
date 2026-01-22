"""
Utility functions - IMPROVED EXTRACTION
Ye file text processing aur AI similarity calculate karne ke liye hai
"""

# Regular expressions ke liye
import re

# AI sentence embeddings aur cosine similarity ke liye
from sentence_transformers import SentenceTransformer, util


class TextProcessor:
    """
    Course content aur exam paper se
    topics aur questions extract karne wali class
    """

    def extract_topics(self, text):
        """
        Course content se topics nikalta hai
        """

        # Debug: poore text ki length
        print(f"   [DEBUG] Total text length: {len(text)} characters")

        topics = []  # Final topics list
        lines = text.strip().split('\n')  # Text ko line by line tod do

        # Debug: total lines
        print(f"   [DEBUG] Total lines: {len(lines)}")

        # Har line ko process karo
        for line in lines:
            line = line.strip()  # Extra spaces hatao

            # Empty ya bohot choti line skip
            if not line or len(line) < 5:
                continue

            # Agar line ALL CAPS ho ya ":" par end ho to skip (headers)
            if line.isupper() or line.endswith(':'):
                continue

            # Pattern 1: "Module 1: Topic" / "Week 2 - Topic"
            match = re.match(
                r'^(Module|Week|Chapter|Unit|Topic|Lecture)\s+\d+[:\-\s]+(.+)$',
                line,
                re.IGNORECASE
            )
            if match:
                topic = match.group(2).strip()
                if len(topic) > 5:
                    topics.append(topic)
                    continue

            # Pattern 2: "1. Topic" / "1) Topic"
            match = re.match(r'^[\d]+[\.\)]\s+(.+)$', line)
            if match:
                topic = match.group(1).strip()
                if len(topic) > 5:
                    topics.append(topic)
                    continue

            # Pattern 3: "- Topic" / "* Topic"
            match = re.match(r'^[\-\*•]\s+(.+)$', line)
            if match:
                topic = match.group(1).strip()
                if len(topic) > 5:
                    topics.append(topic)
                    continue

            # Pattern 4: Normal lines (possible topic sentences)
            if 10 <= len(line) <= 200:
                # Kuch useless keywords skip karo
                skip_keywords = [
                    'time:', 'marks:', 'section',
                    'examination', 'total', 'page'
                ]

                # Agar skip keyword nahi mila to topic maan lo
                if not any(kw in line.lower() for kw in skip_keywords):
                    topics.append(line)

        # Debug: kitne topics niklay
        print(f"   [DEBUG] Extracted {len(topics)} topics")

        # Debug: pehle 3 topics dikhao
        if topics:
            print(f"   [DEBUG] First topics: {topics[:3]}")

        # Max 50 topics return karo
        return topics[:50]

    def extract_questions(self, text):
        """
        Exam paper se questions extract karta hai
        """

        # Debug
        print(f"   [DEBUG] Extracting questions from {len(text)} chars...")

        questions = []

        # Method 1: Lines jin me "?" ho
        for match in re.findall(r'[^\n.!?]{10,}\?', text):
            q = match.strip()
            if len(q) > 10:
                questions.append(q + '?')

        # Method 2: Numbered questions (Q1., 1., Q2)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()

            match = re.match(r'^[Qq]?[\d]+[\.\):\-]\s*(.+)$', line)
            if match:
                question_text = match.group(1).strip()
                if len(question_text) > 15:
                    questions.append(question_text)

        # Method 3: Question keywords se start hone wali lines
        question_keywords = [
            'what', 'how', 'why', 'explain', 'define',
            'write', 'describe', 'compare', 'discuss',
            'list', 'give'
        ]

        for line in lines:
            line = line.strip()

            if len(line) < 15:
                continue

            if any(line.lower().startswith(kw) for kw in question_keywords):
                questions.append(line)

        # Duplicate questions remove karo
        unique = []
        seen = set()

        for q in questions:
            q_clean = q[:100].lower()  # First 100 chars compare
            if q_clean not in seen:
                seen.add(q_clean)
                unique.append(q)

        # Debug
        print(f"   [DEBUG] Extracted {len(unique)} questions")

        # Max 50 questions return
        return unique[:50]


class SimilarityCalculator:
    """
    AI model use karke topic aur question
    ke darmiyan similarity calculate karta hai
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        # Model load hone ka message
        print(f"Loading AI model: {model_name}...")

        # SentenceTransformer model load
        self.model = SentenceTransformer(model_name)

        print("Model loaded successfully! ✅")

    def get_embeddings(self, texts):
        """
        Text list ko AI embeddings me convert karta hai
        """
        return self.model.encode(texts, convert_to_tensor=True)

    def find_best_match(self, topic, questions, question_embeddings=None):
        """
        Har topic ke liye sab se milta julta question dhoondta hai
        """

        # Topic ka embedding banao
        topic_embedding = self.model.encode(
            topic,
            convert_to_tensor=True
        )

        # Agar questions ke embeddings nahi mile
        if question_embeddings is None:
            question_embeddings = self.get_embeddings(questions)

        # Cosine similarity calculate karo
        similarities = util.cos_sim(
            topic_embedding,
            question_embeddings
        )

        # Sab se zyada similarity ka index
        max_idx = similarities.argmax().item()

        # Us index ka score
        max_score = float(similarities[0][max_idx])

        # Index + score return
        return max_idx, max_score
