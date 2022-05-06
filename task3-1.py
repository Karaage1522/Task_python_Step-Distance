import pandas as pd
robot_d=pd.read_csv('robot_data.csv')
robot_d_ID=robot_d.groupby('ID')
