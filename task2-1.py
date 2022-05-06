import pandas as pd
import matplotlib.pyplot as plt
i=0
fig=plt.figure()
robot_d=pd.read_csv('robot_data.csv')
ax=fig.add_subplot()
ax.hist(robot_d.loc[:,"Distance"],bins=80,range=(0,8),color=('b'));
d_len1=len(robot_d.loc[:,"Distance"])
while i<1:
    d_len2=len(robot_d.loc[:,"Distance"])
    robot_d=pd.read_csv('robot_data.csv')
    if d_len2>d_len1:
        ax.hist(robot_d.loc[:,"Distance"],bins=80,range=(0,8),color=('b'));
        d_len1=d_len2
    plt.pause(0.1)
