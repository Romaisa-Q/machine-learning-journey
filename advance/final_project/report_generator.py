"""
Generate beautiful reports in multiple formats
"""
# ↑ File-level docstring
# Matlab: Yeh file analysis ke results ko reports mein convert karegi
# (JSON, HTML, aur Console output)


import json
# ↑ JSON file banane ke liye use hota hai


from typing import Dict
# ↑ Type hinting: batata hai ke function dictionary receive karega


from datetime import datetime
# ↑ Date & time add karne ke liye (report kab generate hui)


class ReportGenerator:
    """Generate analysis reports"""
    # ↑ Yeh class sirf reporting ke liye hai (no analysis logic)


    @staticmethod
    def generate_json_report(results: Dict, filename: str = "output/report.json"):
        """
        Generate JSON report
        
        Args:
            results: Analysis results
            filename: Output filename
        """
        # ↑ Static method → object banaye baghair call ho sakta hai
        # Example: ReportGenerator.generate_json_report(...)
        
        
        report = {
            "generated_at": datetime.now().isoformat(),
            # ↑ Current date-time (machine readable format)
            
            "analysis": results
            # ↑ Poora analysis result JSON mein daal diya
        }
        
        
        with open(filename, 'w', encoding='utf-8') as f:
            # ↑ File open ki write mode mein
            
            json.dump(report, f, indent=2, ensure_ascii=False)
            # ↑ Python dict → JSON file
            # indent=2 → pretty formatting
            # ensure_ascii=False → emojis & unicode allow
        
        
        print(f"📄 JSON report saved: {filename}")
        # ↑ Confirmation message
    
    
    @staticmethod
    def generate_html_report(results: Dict, recommendations: list, 
                            filename: str = "output/report.html"):
        """
        Generate beautiful HTML report
        
        Args:
            results: Analysis results
            recommendations: List of recommendations
            filename: Output filename
        """
        # ↑ HTML report generator
        
        
        summary = results["summary"]
        # ↑ Summary section nikaali
        
        covered = results["covered_topics"]
        # ↑ Covered topics list
        
        not_covered = results["not_covered_topics"]
        # ↑ Not covered topics list
        
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
"""
        # ↑ HTML document start
        # f-string use ki taake Python values inject ho saken
        
        # ⚠️ (CSS + HTML yahan mostly UI/Design hai)
        # Iska purpose: report ko visually beautiful banana
        # Logic nahi, sirf presentation
        
        # Coverage percentage, topic titles, similarity scores
        # dynamically inject ho rahe hain
        
        # Example:
        # {summary['coverage_percentage']} → real number
        # {item['topic']} → topic name
        
        # -------------------------
        # Covered topics section
        # -------------------------
        
        for item in covered:
            html += f"""
                <div class="topic-card">
                    <div class="topic-title">{item['topic']}</div>
                    <div class="topic-match">📝 Best Match: {item['best_match_question']}</div>
                    <div class="topic-match">
                        <span class="similarity-badge">Similarity: {item['similarity']:.2%}</span>
                    </div>
                </div>
"""
            # ↑ Har covered topic ka card HTML mein add ho raha hai
        
        
        html += """
            </div>
"""
        # ↑ Covered topics section close
        
        
        # -------------------------
        # Not covered topics section
        # -------------------------
        
        for item in not_covered:
            html += f"""
                <div class="topic-card not-covered">
                    <div class="topic-title">{item['topic']}</div>
                    <div class="topic-match">📝 Closest Match: {item['best_match_question']}</div>
                    <div class="topic-match">
                        <span class="similarity-badge" style="background: #dc3545;">Similarity: {item['similarity']:.2%}</span>
                    </div>
                </div>
"""
            # ↑ Not covered topics red style ke sath
        
        
        # -------------------------
        # Recommendations section
        # -------------------------
        
        for rec in recommendations:
            html += f"<li>{rec}</li>\n"
            # ↑ Har recommendation ek list item ban rahi hai
        
        
        html += """
</html>
"""
        # ↑ HTML document close
        
        
        with open(filename, 'w', encoding='utf-8') as f:
            # ↑ HTML file write
            
            f.write(html)
            # ↑ Poora HTML string file mein save
        
        
        print(f"🌐 HTML report saved: {filename}")
        # ↑ Confirmation
    
    
    @staticmethod
    def print_console_report(results: Dict, recommendations: list):
        """
        Print beautiful console report
        
        Args:
            results: Analysis results
            recommendations: List of recommendations
        """
        # ↑ Terminal / console output ke liye
        
        
        summary = results["summary"]
        # ↑ Summary nikaali
        
        
        print("\n" + "="*80)
        print("📊 COVERAGE ANALYSIS REPORT".center(80))
        print("="*80 + "\n")
        # ↑ Header formatting
        
        
        # Summary
        print("📈 SUMMARY:")
        print(f"   Total Topics: {summary['total_topics']}")
        print(f"   Total Questions: {summary['total_questions']}")
        print(f"   Covered Topics: {summary['covered_topics']}")
        print(f"   Not Covered: {summary['not_covered_topics']}")
        print(f"   Coverage: {summary['coverage_percentage']}%")
        # ↑ Basic stats print
        
        
        # Coverage bar
        bar_length = 50
        # ↑ Bar ki total length
        
        filled = int(bar_length * summary['coverage_percentage'] / 100)
        # ↑ Kitna bar fill karna hai
        
        bar = "█" * filled + "░" * (bar_length - filled)
        # ↑ ASCII progress bar
        
        print(f"\n   [{bar}] {summary['coverage_percentage']}%\n")
        # ↑ Visual coverage bar
        
        
        # Covered topics
        print("✅ COVERED TOPICS:")
        for item in results["covered_topics"]:
            print(f"   • {item['topic'][:60]}...")
            print(f"     Match: {item['best_match_question'][:60]}...")
            print(f"     Similarity: {item['similarity']:.2%}\n")
        # ↑ Covered topics details
        
        
        # Not covered topics
        if results["not_covered_topics"]:
            print("❌ NOT COVERED TOPICS:")
            for item in results["not_covered_topics"]:
                print(f"   • {item['topic'][:60]}...")
                print(f"     Closest: {item['best_match_question'][:60]}...")
                print(f"     Similarity: {item['similarity']:.2%}\n")
        
        
        # Recommendations
        print("💡 RECOMMENDATIONS:")
        for rec in recommendations:
            print(f"   {rec}")
        
        
        print("\n" + "="*80 + "\n")
        # ↑ End of report
