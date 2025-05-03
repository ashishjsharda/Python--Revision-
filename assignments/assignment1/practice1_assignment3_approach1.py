def high_scorers(student_scores):
    """
    This function takes a list of student scores and returns a list of students who scored above 70.
    
    :param student_scores: List of tuples containing student names and their scores
    :return: List of students who scored above 70
    """
    return [student for student, score in student_scores if score > 70]

student= high_scorers([('Alice', 85), ('Bob', 65), ('Charlie', 90), ('David', 70)])
print(student)
