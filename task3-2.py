import pandas as pd
i=0
dic0={1:0}
dic1={1:0}
dic2={1:0}
dic3={1:0}
dic4={1:0}
dic5={1:0}
dic6={1:0}
dic7={1:0}
dic8={1:0}
dic9={1:0}
dic_list=[dic0,dic1,dic2,dic3,dic4,dic5,dic6,dic7,dic8,dic9]
robot_d=pd.read_csv('robot_data.csv')
robot_d_ID=robot_d.groupby('ID')
while i <= 9:
    j=len(robot_d_ID["Step"].get_group(i))
    k=1
    while k <= j:
        l=robot_d_ID["Distance"].get_group(i).iloc[k-1]
        m=robot_d_ID["Step"].get_group(i).iloc[k-1]
        dic_list[i].update({m:l})
        k+=1
    i+=1
