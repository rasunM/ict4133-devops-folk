"""
Student Grade Calculator with Overly Complex Logic
WARNING: This code intentionally demonstrates BAD PRACTICES for educational purposes!
Cyclomatic Complexity: EXTREMELY HIGH (>15)
"""

def calculate_student_grade(score, attendance, assignments_completed, participation, 
                           extra_credit, late_submissions, group_project_score,
                           midterm_score, final_exam_score, is_honors_student):
    """
    Calculate final grade for a student based on multiple criteria.
    
    WARNING: This function has TERRIBLE cyclomatic complexity!
    It violates the Single Responsibility Principle and is unmaintainable.
    """
    
    final_grade = "F"
    
    # Nested if/else hell begins here!
    if score >= 90:
        if attendance >= 90:
            if assignments_completed >= 15:
                if participation >= 80:
                    if extra_credit > 0:
                        if late_submissions < 2:
                            if group_project_score >= 85:
                                if midterm_score >= 80:
                                    if final_exam_score >= 85:
                                        if is_honors_student:
                                            final_grade = "A+"
                                        else:
                                            final_grade = "A"
                                    else:
                                        if final_exam_score >= 75:
                                            final_grade = "A-"
                                        else:
                                            final_grade = "B+"
                                else:
                                    if midterm_score >= 70:
                                        final_grade = "B+"
                                    else:
                                        final_grade = "B"
                            else:
                                if group_project_score >= 75:
                                    final_grade = "B"
                                else:
                                    final_grade = "B-"
                        else:
                            if late_submissions < 4:
                                final_grade = "B-"
                            else:
                                final_grade = "C+"
                    else:
                        if late_submissions == 0:
                            final_grade = "A-"
                        else:
                            final_grade = "B+"
                else:
                    if participation >= 60:
                        final_grade = "B"
                    else:
                        final_grade = "B-"
            else:
                if assignments_completed >= 12:
                    final_grade = "B-"
                else:
                    final_grade = "C+"
        else:
            if attendance >= 75:
                final_grade = "B-"
            else:
                final_grade = "C"
    else:
        if score >= 80:
            if attendance >= 85:
                if assignments_completed >= 14:
                    final_grade = "B+"
                else:
                    final_grade = "B"
            else:
                if attendance >= 70:
                    final_grade = "B-"
                else:
                    final_grade = "C+"
        else:
            if score >= 70:
                if attendance >= 80:
                    if participation >= 70:
                        final_grade = "C+"
                    else:
                        final_grade = "C"
                else:
                    if attendance >= 60:
                        final_grade = "C"
                    else:
                        final_grade = "C-"
            else:
                if score >= 60:
                    if attendance >= 70:
                        final_grade = "D+"
                    else:
                        if attendance >= 50:
                            final_grade = "D"
                        else:
                            final_grade = "F"
                else:
                    if score >= 50:
                        if extra_credit > 5:
                            final_grade = "D"
                        else:
                            final_grade = "F"
                    else:
                        final_grade = "F"
    
    return final_grade


# Example usage
if __name__ == "__main__":
    # Test case 1: Excellent student
    grade = calculate_student_grade(
        score=95, 
        attendance=95, 
        assignments_completed=16,
        participation=90, 
        extra_credit=5, 
        late_submissions=0,
        group_project_score=90, 
        midterm_score=88, 
        final_exam_score=92,
        is_honors_student=True
    )
    print(f"Excellent student grade: {grade}")
    
    # Test case 2: Average student
    grade = calculate_student_grade(
        score=75, 
        attendance=80, 
        assignments_completed=13,
        participation=70, 
        extra_credit=0, 
        late_submissions=2,
        group_project_score=75, 
        midterm_score=72, 
        final_exam_score=78,
        is_honors_student=False
    )
    print(f"Average student grade: {grade}")
