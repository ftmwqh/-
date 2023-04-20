import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['Microsoft YaHei']#中文字体
# 自定义函数 指定的拟合形式
def func(x, a, b, c):
    return a/np.sqrt((x+c)**2+b**2)


# 定义x、y散点坐标
x = [5,10,15,20,25, 30,35, 40,45, 50,55, 60,65, 70,75,80,85,90,95,100]
#x = np.array(x)
num = [680.95,690.48,688.1,683.34,676.19,659.52,654.76,642.87,616.67
    ,602.08,589.58,574.97,566.06,540.33,530.28,514.28,498.24,485.71,467.77,458.92]
y = np.array(num)
y=y**2

# 非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]
c = popt[2]

yvals = func(x, a, b, c)  # 拟合y值
r2=r2_score(y,yvals)
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数c:', c)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
print('拟合度R2:',r2)
# 绘图
plot1 = plt.plot(x, y, 's', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel(r'$f/Hz$')
plt.ylabel(r'$U^2/mV^2$')
plt.legend(loc=1)  # 指定legend的位置右上角
plt.title('curve_fit')
plt.show()


# 自定义函数 e指数形式
def func(x, a, b):
    return a*x**2+b


# 定义x、y散点坐标
x = [50,100,150,200,250, 300,350, 400,450, 500]
x = np.array(x)
x=x*683.3/2000
num = [43.3,74.1,92.2,131,148,163,171,177,224,309]
y = np.array(num)

# 非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
# 获取popt里面是拟合系数
print(popt)
a = popt[0]
b = popt[1]

yvals = func(x, a, b)  # 拟合y值
r2=r2_score(y,yvals)
print('popt:', popt)
print('系数a:', a)
print('系数b:', b)
print('系数pcov:', pcov)
print('系数yvals:', yvals)
print('拟合度R2:',r2)
# 绘图
plot1 = plt.plot(x, y, 's', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel(r'$B/nT $')
plt.ylabel(r'灵敏度$/fT/\sqrt{Hz}$')
plt.legend(loc=4)  # 指定legend的位置右上角
plt.title('curve_fit')
plt.show()