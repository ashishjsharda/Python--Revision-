def high_scorers(student_scores):
    result=[]
    for student in student_scores:
        if student['score']>=70:
            result.append(student['name'])
            
    return result
   
print(high_scorers([{'name': 'Alice', 'score': 80}, {'name': 'Bob', 'score': 65}, {'name': 'Charlie', 'score': 75}]))
