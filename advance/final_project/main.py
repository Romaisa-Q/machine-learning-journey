"""
Main application - Coverage Analyzer System
"""
import os
from analyzer import CoverageAnalyzer
from report_generator import ReportGenerator


def ensure_directories():
    """Create necessary directories"""
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)


def load_sample_data():
    """Create sample data if files don't exist"""
    course_content = """
1. Object Oriented Programming in Python
2. Loops and Iterations in Python
3. Functions and Parameters
4. Exception Handling and Error Management
5. File Handling and I/O Operations
6. Data Structures: Lists, Tuples, Dictionaries
7. Modules and Packages
8. Regular Expressions
9. Database Connectivity with Python
10. Web Scraping with BeautifulSoup
"""
    
    exam_paper = """
Q1. Explain the concept of inheritance in object-oriented programming with examples.

Q2. What is a for loop? Write a program to print numbers from 1 to 10.

Q3. How do you handle exceptions in Python? Explain try-except blocks.

Q4. Write a function to calculate the factorial of a number.

Q5. What are decorators in Python? Give an example.

Q6. Explain list comprehension with examples.

Q7. How to connect to a MySQL database using Python?
"""
    
    # Save to files
    with open("data/course_content.txt", "w", encoding="utf-8") as f:
        f.write(course_content)
    
    with open("data/exam_paper.txt", "w", encoding="utf-8") as f:
        f.write(exam_paper)
    
    print("✅ Sample data files created in 'data/' folder\n")


def main():
    """Main application logic"""
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     🎓 COURSE-EXAM COVERAGE ANALYZER 🎓                  ║
    ║                                                          ║
    ║     AI-Powered Semantic Analysis System                 ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # Setup
    ensure_directories()
    
    # Check if data files exist
    if not os.path.exists("data/course_content.txt"):
        print("📂 No data files found. Creating sample data...\n")
        load_sample_data()
    
    # Load data
    print("📖 Loading course content and exam paper...\n")
    
    with open("data/course_content.txt", "r", encoding="utf-8") as f:
        course_content = f.read()
    
    with open("data/exam_paper.txt", "r", encoding="utf-8") as f:
        exam_paper = f.read()
    
    # Initialize analyzer
    threshold = 0.5  # Adjust this based on requirements
    analyzer = CoverageAnalyzer(threshold=threshold)
    
    # Perform analysis
    results = analyzer.analyze_coverage(course_content, exam_paper)
    
    # Generate recommendations
    recommendations = analyzer.get_recommendations(results)
    
    # Generate reports
    print("📝 Generating reports...\n")
    
    report_gen = ReportGenerator()
    
    # JSON report
    report_gen.generate_json_report(results)
    
    # HTML report
    report_gen.generate_html_report(results, recommendations)
    
    # Console report
    report_gen.print_console_report(results, recommendations)
    
    print("✨ All reports generated successfully!")
    print(f"📁 Check 'output/' folder for:")
    print("   • report.json (Data)")
    print("   • report.html (Visual Report - Open in browser!)")
    print("\n🎉 Analysis complete! Thank you for using Coverage Analyzer!\n")


if __name__ == "__main__":
    main()