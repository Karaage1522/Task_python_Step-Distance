import pandas as pd
robot_d=pd.read_csv('robot_data.csv')
print(robot_d.loc[:,"Distance"])
