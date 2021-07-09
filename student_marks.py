import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('dark_background')


class students:
    def __init__(self, fname, lname, classes, physics, chemistry, maths):
        self.fname = fname
        self.lname = lname
        self.classes = classes
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths


student = np.array([students('Admin', 'strator', 12, 60, 60, 90),
                    students('Taylor', "stuart", 12, 65, 55, 90)])
print(student[0].chemistry)
sub = ['physics', 'chemistry', 'maths']
marks = [[student[0].physics, student[0].chemistry, student[0].maths],
         [student[1].physics, student[1].chemistry, student[1].maths]]

X = np.arange(len(sub))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.15, 0.8, 0.7])
ax.set_title("Score between Admin and Taylor stuart.")
ax.set_ylabel('Scores')
ax.set_xticks(X)
ax.set_xticklabels(sub)
ax.bar(X + 0.00, marks[0], color='b', width=0.25, label=student[0].fname)
ax.bar(X + 0.25, marks[1], color='g', width=0.25, label=student[1].fname)
plt.legend(loc='best')
plt.show()
