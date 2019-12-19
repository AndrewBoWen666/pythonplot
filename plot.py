#import pandas as pd 

import matplotlib.pyplot as plt

#import numpy as np

#定义文件读取函数

#def reda_data(file_path):
 #   column_names = ['flighttime','VehicleLatitude','VehicleLongtitude','Altitude','Velocitym1','Velocitym2','Velocitym3','pitch','roll','yaw']
  #  data = pd.read_csv(file_path,header = None, names = colum_names)
   # return data

def error(agr1,agr2):
    error = [1] * 10 
    error[0]=float(agr1[0])
    #print(agr1[8],agr2[8])
    for i in range (9):
        error[i+1] = float(agr1[i+1]) - float(agr2[i+1])
    return error

def simple_scatter_plot(x,y1,y2,y3,fig_no):
    plt.figure(fig_no)
    plt.scatter(x,y1,label="Pitch",color="red",lw=0.2)
    plt.scatter(x,y2,label="Roll",color = "blue",lw=0.2)
    plt.scatter(x,y3,label="Yaw",color="green",lw=0.2)
    plt.xlabel('Flight Time')
    plt.ylabel('Error(degree)')
    plt.title('Error Plot')
    plt.ylim(-360,360)
    #plt.xlim(0,480)
    plt.legend()

file1 = open('Simalignresult.txt')
file2 = open('SimAirTrack.txt')
flighttime   = [1] * 4800
VLatitude_e  = [1] * 4800
VLongtitude_e= [1] * 4800
Altitude_e   = [1] * 4800
Velocity1_e  = [1] * 4800
Velocity2_e  = [1] * 4800
Velocity3_e  = [1] * 4800
Pitch_e      = [1] * 4800
Roll_e       = [1] * 4800
Yaw_e        = [1] * 4800
for i in range(4800):
    data1 = file1.readline()
    for j in range(9):
        data2=file2.readline()
    data2 = file2.readline()
    d1    = data1.split()
    d2    = data2.split()
    plt_error = error(d1,d2)
    flighttime[i]   = plt_error[0]
    VLatitude_e[i]  = plt_error[1]
    VLongtitude_e[i]= plt_error[2]
    Altitude_e[i]   = plt_error[3]
    Velocity1_e[i]  = plt_error[4]
    Velocity2_e[i]  = plt_error[5]
    Velocity3_e[i]  = plt_error[6]
    Pitch_e[i]      = plt_error[7]
    Roll_e[i]       = plt_error[8]
    Yaw_e[i]        = plt_error[9]
    for k in range(9):
        data1=file1.readline()
#print(Roll_e)
x = flighttime
y1 = Pitch_e
y2 = Roll_e
y3 = Yaw_e
figure_no = 1 
simple_scatter_plot(x,y1,y2,y3,figure_no)
plt.show()


