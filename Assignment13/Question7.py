import matplotlib.pyplot as plt
subjects = ["Maths","Python","DBMS","AI","OS"]
sem1 = [78,82,75,80,77]
sem2 = [85,88,81,90,84]
plt.figure(figsize=(8,5))
plt.plot(subjects, sem1,
         marker='o',
         linestyle='--',
         label='Semester 1')
plt.plot(subjects, sem2,
         marker='s',
         linestyle='-',
         label='Semester 2')
plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()
plt.show()