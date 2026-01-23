# 🎓 Course–Exam Coverage Analyzer (AI-Powered)

An **AI-powered semantic analysis system** that evaluates how well an exam paper covers the topics taught in a course.
This project uses **Natural Language Processing (NLP)** and **Sentence-BERT embeddings** to measure semantic similarity between course topics and exam questions.

---

## 🚀 Project Overview

In traditional systems, course–exam alignment is checked manually, which is:

* Time-consuming
* Subjective
* Error-prone

This project automates the process using **Artificial Intelligence**, providing:

* Coverage percentage
* Covered vs. non-covered topics
* Best matching exam questions
* Actionable recommendations
* Reports in **JSON, HTML, and Console formats**

---

## 🧠 Key Features

✅ Intelligent topic extraction from course material
✅ Smart question extraction from exam papers
✅ AI-based semantic similarity (not just keyword matching)
✅ Coverage analysis with adjustable threshold
✅ Beautiful HTML report generation
✅ JSON report for further processing
✅ Console summary for quick review

---

## 🛠️ Technologies Used

* **Python 3.8+**
* **Sentence-Transformers (Sentence-BERT)**
* **Regular Expressions (Regex)**
* **Cosine Similarity**
* **HTML & CSS** (for reports)

---

## 📂 Project Structure

```
coverage-analyzer/
│
├── data/
│   ├── course_content.txt       # Course syllabus/material
│   └── exam_paper.txt           # Exam questions
│
├── output/
│   ├── report.json              # Machine-readable report
│   └── report.html              # Visual HTML report
│
├── utils.py                     # Text extraction & similarity logic
├── analyzer.py                  # Core coverage analysis engine
├── report_generator.py          # Report generation (JSON, HTML, Console)
├── main.py                      # Main application entry point
└── README.md                    # Project documentation
```

---

## ⚙️ How the System Works (High Level)

1. **Text Processing**

   * Extracts topics from course content
   * Extracts questions from exam paper

2. **Embedding Generation**

   * Converts text into AI embeddings using Sentence-BERT

3. **Similarity Analysis**

   * Uses cosine similarity to find best matching questions for each topic

4. **Coverage Decision**

   * If similarity ≥ threshold → topic is covered
   * Otherwise → topic is not covered

5. **Report Generation**

   * JSON (data)
   * HTML (visual)
   * Console output

---

## 📊 Coverage Threshold

The similarity **threshold** determines whether a topic is considered covered.

```python
threshold = 0.5
```

* Higher threshold → stricter matching
* Lower threshold → more flexible matching

You can adjust this value in `main.py`.

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install sentence-transformers
```

---

### 2️⃣ Run the Application

```bash
python main.py
```

---

### 3️⃣ Output Generated

After execution:

* 📄 `output/report.json`
* 🌐 `output/report.html` (open in browser)
* 🖥️ Console summary

---

## 📈 Sample Output

* **Coverage Percentage:** 70%
* **Covered Topics:** Loops, Functions, Exception Handling
* **Not Covered Topics:** File Handling, Web Scraping
* **Recommendations:** Add questions or revise assessment design

---

## 💡 Recommendations Engine

The system automatically:

* Evaluates overall exam quality
* Identifies missing topics
* Suggests improvements
* Advises on threshold adjustment

---

## 🎯 Use Cases

* Universities & Colleges
* Teachers & Course Designers
* Examination Boards
* Academic Quality Assurance
* EdTech Platforms

---

## 📌 Future Enhancements

* GUI or Web Interface
* Support for PDFs & DOCX files
* Bloom’s Taxonomy analysis
* Question difficulty estimation
* Multi-language support

---

## 👩‍💻 Author

**Nosaiba**
Computer Science Undergraduate
Aspiring Web Developer & AI Enthusiast

---

## 🏁 Conclusion

This project demonstrates the practical use of **AI and NLP** in the education domain, ensuring fair, aligned, and effective assessment systems.

> *“Good exams don’t just test students — they reflect the course.”* ✨

---

⭐ If you found this project useful, feel free to star the repository!
