"""
Core analysis engine for coverage calculation
"""
# ↑ File-level docstring
# Matlab: Yeh file course aur exam ke darmiyan coverage calculate karegi


from typing import List, Dict, Tuple
# ↑ Type hinting ke liye import
# Python ko aur human ko clarity milti hai ke functions kya return kar rahe hain


from utils import TextProcessor, SimilarityCalculator
# ↑ Apne banaye hue helper tools import kiye
# TextProcessor → topics & questions nikalta hai
# SimilarityCalculator → AI se similarity calculate karta hai


class CoverageAnalyzer:
    """Main coverage analysis engine"""
    # ↑ Yeh class poore system ka boss hai
    
    
    def __init__(self, threshold: float = 0.5, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the analyzer
        
        Args:
            threshold: Minimum similarity to consider topic covered
            model_name: AI model name
        """
        # ↑ Constructor (jab object banega tab chalega)
        
        self.threshold = threshold
        # ↑ Similarity threshold save ki
        # Agar similarity >= threshold → topic covered
        
        self.text_processor = TextProcessor()
        # ↑ TextProcessor ka object banaya
        # Is se topics aur questions extract honge
        
        self.similarity_calculator = SimilarityCalculator(model_name)
        # ↑ AI similarity calculator ka object banaya
        # Is ke andar AI model load hota hai
        
        
    def analyze_coverage(self, course_content: str, exam_paper: str) -> Dict:
        """
        Analyze coverage between course and exam
        
        Args:
            course_content: Course material text
            exam_paper: Exam questions text
            
        Returns:
            Comprehensive analysis results
        """
        # ↑ Main function jo poora analysis karta hai
        # Course + exam input → detailed report output
        
        
        print("\n" + "="*60)
        # ↑ Console formatting ke liye
        
        print("🚀 STARTING COVERAGE ANALYSIS")
        # ↑ User ko bataya ke analysis start ho gaya
        
        print("="*60 + "\n")
        
        
        # Step 1: Extract topics and questions
        print("📝 Step 1: Extracting topics and questions...")
        # ↑ Step 1 ka heading
        
        topics = self.text_processor.extract_topics(course_content)
        # ↑ Course content se topics nikale
        
        questions = self.text_processor.extract_questions(exam_paper)
        # ↑ Exam paper se questions nikale
        
        print(f"   ✅ Found {len(topics)} course topics")
        # ↑ Kitne topics mile
        
        print(f"   ✅ Found {len(questions)} exam questions\n")
        # ↑ Kitne questions mile
        
        
        # Step 2: Calculate embeddings
        print("🤖 Step 2: Converting to AI embeddings...")
        # ↑ Step 2 ka heading
        
        question_embeddings = self.similarity_calculator.get_embeddings(questions)
        # ↑ Exam questions ko AI embeddings (numbers) mein convert kiya
        
        print("   ✅ Embeddings generated\n")
        # ↑ Confirmation
        
        
        # Step 3: Analyze each topic
        print("📊 Step 3: Analyzing topic coverage...")
        # ↑ Step 3 ka heading
        
        covered_topics = []
        # ↑ Covered topics ki list
        
        not_covered_topics = []
        # ↑ Not covered topics ki list
        
        detailed_matches = []
        # ↑ Har topic ka detailed result
        
        
        for i, topic in enumerate(topics):
            # ↑ Har topic pe loop
            
            best_q_idx, similarity = self.similarity_calculator.find_best_match(
                topic, questions, question_embeddings
            )
            # ↑ AI se poocha:
            # "Is topic ke liye kaunsa question sab se zyada similar hai?"
            
            
            match_info = {
                "topic": topic,
                # ↑ Topic ka naam
                
                "best_match_question": questions[best_q_idx],
                # ↑ Best matching exam question
                
                "similarity": round(similarity, 4),
                # ↑ Similarity score (4 decimal tak)
                
                "covered": similarity >= self.threshold
                # ↑ True / False → covered ya nahi
            }
            
            
            detailed_matches.append(match_info)
            # ↑ Har topic ka record save kar liya
            
            
            if similarity >= self.threshold:
                # ↑ Agar similarity threshold se zyada hai
                
                covered_topics.append(match_info)
                # ↑ Covered list mein daal do
                
                status = "✅"
                # ↑ Status emoji
                
            else:
                # ↑ Agar similarity kam hai
                
                not_covered_topics.append(match_info)
                # ↑ Not covered list mein daal do
                
                status = "❌"
                # ↑ Status emoji
            
            
            print(f"   {status} Topic {i+1}: {topic[:50]}... → {similarity:.2f}")
            # ↑ Har topic ka live result console pe show
        
        
        # Step 4: Calculate statistics
        print("\n📈 Step 4: Calculating statistics...")
        # ↑ Step 4 ka heading
        
        total_topics = len(topics)
        # ↑ Total topics
        
        covered_count = len(covered_topics)
        # ↑ Covered topics count
        
        coverage_percentage = (covered_count / total_topics * 100) if total_topics > 0 else 0
        # ↑ Coverage percentage calculate ki
        # Divide by zero se bachne ke liye check
        
        
        # Compile results
        results = {
            "summary": {
                "total_topics": total_topics,
                "total_questions": len(questions),
                "covered_topics": covered_count,
                "not_covered_topics": len(not_covered_topics),
                "coverage_percentage": round(coverage_percentage, 2),
                "threshold_used": self.threshold
            },
            # ↑ Short summary section
            
            "covered_topics": covered_topics,
            # ↑ Covered topics ka detail
            
            "not_covered_topics": not_covered_topics,
            # ↑ Not covered topics ka detail
            
            "all_matches": detailed_matches,
            # ↑ Har topic ka full analysis
            
            "topics_list": topics,
            # ↑ Raw topics list
            
            "questions_list": questions
            # ↑ Raw questions list
        }
        
        
        print(f"   ✅ Coverage: {coverage_percentage:.1f}%\n")
        # ↑ Final percentage show
        
        print("="*60)
        print("✨ ANALYSIS COMPLETE!")
        print("="*60 + "\n")
        # ↑ End message
        
        return results
        # ↑ Poora result return
        
        
    def get_recommendations(self, results: Dict) -> List[str]:
        """
        Generate recommendations based on analysis
        
        Args:
            results: Analysis results
            
        Returns:
            List of recommendations
        """
        # ↑ Analysis ke baad suggestions dene wala function
        
        recommendations = []
        # ↑ Empty list for recommendations
        
        coverage = results["summary"]["coverage_percentage"]
        # ↑ Coverage percentage nikali
        
        not_covered = results["not_covered_topics"]
        # ↑ Not covered topics nikale
        
        
        # Overall assessment
        if coverage >= 80:
            recommendations.append("✅ Excellent coverage! Exam is well-aligned with course.")
            # ↑ Bohat acha alignment
            
        elif coverage >= 60:
            recommendations.append("⚠️ Good coverage, but some topics need attention.")
            # ↑ Theek hai, thori kami hai
            
        else:
            recommendations.append("❌ Poor coverage. Significant gaps between course and exam.")
            # ↑ Coverage weak hai
        
        
        # Specific recommendations
        if not_covered:
            # ↑ Agar missing topics hain
            
            recommendations.append(f"\n📌 {len(not_covered)} topics are not covered in exam:")
            # ↑ Count show
            
            for item in not_covered[:5]:
                # ↑ Sirf top 5 topics
                
                recommendations.append(f"   • {item['topic']}")
                # ↑ Topic ka naam
            
            
            recommendations.append("\n💡 Suggestions:")
            recommendations.append("   1. Add questions covering the missing topics")
            recommendations.append("   2. Review if these topics are essential for assessment")
            recommendations.append("   3. Consider adjusting course content if topics aren't critical")
        
        
        # Threshold suggestions
        if coverage < 50:
            # ↑ Agar coverage bohat kam hai
            
            recommendations.append(f"\n🎚️ Note: Current threshold is {results['summary']['threshold_used']}")
            recommendations.append("   Consider lowering threshold if topics are related but not exact matches")
        
        
        return recommendations
        # ↑ Final recommendations return
