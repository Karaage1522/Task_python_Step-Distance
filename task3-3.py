import pandas as pd
import matplotlib.pyplot as plt
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
graph_step=[]
graph_distance=[]
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
i=0
while i <= 9:
    for j in dic_list[i].keys():
        graph_step.append(j)
    k=len(graph_step)
    l=0
    while l < k:
        graph_distance.append(dic_list[i][graph_step[l]])
        l+=1
    name="ID{}"
    label_name=name.format(i)
    plt.plot(graph_step,graph_distance,label=label_name)
    graph_step.clear()
    graph_distance.clear()
    if i==2:
        plt.legend()
        plt.show()
    elif i==5:
        plt.legend()
        plt.show()
    elif i==9:
        plt.legend()
        plt.show()
    i+=1
