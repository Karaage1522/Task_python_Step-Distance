import pandas as pd
import matplotlib.pyplot as plt
robot_d=pd.read_csv('robot_data.csv')
print(robot_d.head(3))
print(robot_d.loc[:,"Distance"])
plt.hist(robot_d.loc[:,"Distance"],bins=80,range=(0,8));
plt.show()

