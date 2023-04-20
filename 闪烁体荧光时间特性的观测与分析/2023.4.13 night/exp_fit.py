import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['Microsoft YaHei']#中文字体

def fit_tau(filename):
    t=np.zeros(1000)
    U=np.zeros(1000)

    with open(filename,"r") as csvfile:

        reader = csv.reader(csvfile)

        #这里不需要readlines
        i=0
        j=0
        for line in reader:
            if 1020>=i>=21:
                t[i-21]=float(line[0])
                if t[i-21]>0:
                    if j==0:
                        j=i-21
                U[i-21]=float(line[1])#读入CSV列数据
            i+=1

        t=t[j:-1]
        U=U[j:-1]

    #print(U)



    # 自定义函数 指定的拟合形式
    def func(t, tau,a):
        return a*np.exp(-t*tau)#!!!不能把tau放在分母，否则拟合出问题！！！

    # 非线性最小二乘法拟合
    popt, pcov = curve_fit(func, t, U)
    # 获取popt里面是拟合系数
    # print(popt)
    tau = popt[0]
    a = popt[1]

    yvals = func(t, tau,a)  # 拟合y值
    r2=r2_score(U,yvals)
    # print('popt:', popt)
    # print('系数a:', a)
    # print('系数tau:', tau)
    print('拟合度R2:',r2)
    # 绘图
    plot1 = plt.plot(t, U, 's', label='original values')
    plot2 = plt.plot(t, yvals, 'r', label='expfit values')
    plt.xlabel(r'$t/s$')
    plt.ylabel(r'$U/V$')
    plt.legend(loc=4)  # 指定legend的位置右上角
    plt.title('curve_fit')
    plt.show()

    return 1/tau

BGO=['BGO01.csv','BGO02.csv','BGO03.csv','BGO04.csv','BGO05.csv'
    ,'BGO06.csv','BGO07.csv','BGO05.csv','BGO02.csv','BGO10.csv']
NaI=['NaI01.csv','NaI02.csv','NaI03.csv','NaI04.csv','NaI05.csv'
    ,'NaI06.csv','NaI07.csv','NaI08.csv','NaI05.csv','NaI10.csv']


sum=0
for b in BGO:
    tau1=fit_tau(b)
    sum+=tau1
    print(b,tau1)
sum/=10
print("average BGO:",sum)

sum=0
for n in NaI:
    tau2=fit_tau(n)
    sum+=tau2
    print(n,tau2)
sum/=10
print("average NaI:",sum)