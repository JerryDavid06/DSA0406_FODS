import numpy as np

student_scores = np.array([
    [80, 75, 85, 70],
    [90, 85, 80, 75],
    [70, 80, 90, 85],
    [85, 90, 75, 80]
])

averages = np.mean(student_scores, axis=0)
subjects = ["Math", "Science", "English", "History"]

print("Subject averages:", averages)
print("Highest average:", subjects[np.argmax(averages)])
