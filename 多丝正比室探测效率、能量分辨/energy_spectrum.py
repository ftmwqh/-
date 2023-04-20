import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
def pic(filename1):#绘制随机行走各平均值与期望对比
    f1=open(filename1,'r')
    lines1 = f1.readlines()
    m = len(lines1)
    print('height=', m)
    n = len(lines1[1].split(' '))
    print('width=', n)
    y=np.zeros(1024,dtype=float)
    x=np.arange(0,1024,1)

    i = 0#读取x模拟值
    for line in lines1:
        if i==1024:
            break
        y[i]=line
        print(line,i)
        i+=1

    print(x)
    fig=plt.figure()
    ax1=fig.add_subplot(111)

    ax1.plot(x, y, linewidth=1)
    ax1.set_xlabel('道数')
    ax1.set_ylabel('N')
    ax1.set_title(r"$^{55}Fe $源 x 射线能谱图",y=-0.2)

    plt.show()

pic('wqh.txt')