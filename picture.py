#coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# X = [1, 1, 2, 2]
# Y = [3, 4, 4, 3]
# Z = [1, 2, 1, 1]
# ax=plt.subplot(111,projection='3d') #创建一个三维的绘图工程
#
# #将数据点分成三部分画，在颜色上有区分度
# ax.scatter(X,Y,Z) #绘制数据点
# plt.show()
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# X = [1, 1, 2, 2]
# Y = [3, 4, 4, 3]
# Z = [1, 2, 1, 1]
# ax.plot_trisurf(X, Y, Z)
# plt.subplot
# plt.show()
# def getWorkDay(all_Info):
#     work_day_max = []
#     work_day_min = []
#     QNTi = []
#     DPKimin = []
#     DPKimax = []
#     LPRDmin = []
#     LPRDmax = []
#     DEKmin = []
#     DEKmax = []
#     for i in range(0, all_Info.__len__()):
#         QNTi.append(all_Info[i][3])
#         lprd = all_Info[i][4].split('-')
#         dek = all_Info[i][12].split('-')
#         dpki = all_Info[i][5].split('-')
#         LPRDmin.append(float(lprd[0]))
#         LPRDmax.append(float(lprd[1]))
#         DEKmin.append(float(dek[0]))
#         DEKmax.append(float(dek[1]))
#         DPKimin.append(float(dpki[0]))
#         DPKimax.append(float(dpki[1]))
#         temp_work_day_max = int(math.ceil(QNTi[i] / (LPRDmin[i] * DEKmin[i]*DPKimin[i])))
#         temp_work_day_min = int(math.ceil(QNTi[i] / (LPRDmax[i] * DEKmax[i]*DPKimax[i])))
#         work_day_min.append(temp_work_day_min)
#         work_day_max.append(temp_work_day_max)
#     return work_day_min, work_day_max
#
#     l = [x[2] for x in allinfo]
# # for i in range(0, work_day_max.__len__()):
# #    print "第----(%s)----道工序最短工期是：---(%s)---最长工期是：---(%s)---可加速天数是：---(%s)---" % (i+1,work_day_min[i],work_day_max[i],(work_day_max[i]-work_day_min[i]))
#
# for k in range(0, times):
#     obj_value = calobjValue(pop, popSize, chromlength, Tnsum, Tcsum, Cnsum, Ccsum, Qcsum,matri,Tn)
#     #fit_value = calfitValue(obj_value)
#     #results.append(best(pop, fit_value))  # best中第一个存Umax，第二个存取到这个Umax的所有信息
#     #pop = selection(pop, fit_value)  # 新种群复制
#     #pop = crossover(pop, pc)  # 交配
#     #pop = mutation(pop, pm, Tns_all_info)  # 变异
# maxUmax = 0;
# maxInfo = []
# for max in range(0, len(results)):
#     if (results[max][0] > maxUmax):
#         maxUmax = results[max][0]
#         maxInfo = results[max][1]



# pop = [1,2,3,4,5,6,7,8,9,10]
# fit_value=[0,9,1,2,3,0,3,1,0,0]
# for i in range(0, len(pop)):
#     if (fit_value[i] == 0):
#         for j in range(i+1, len(pop)):
#             if(fit_value[j] != 0):
#                 pop[i] = pop[j]
#                 break
#     else:
#         continue
# print pop
# X = [1, 1, 2, 2]
# Y = [3, 4, 4, 3]
# Z = [1, 2, 1, 1]
# ax=plt.subplot(111,projection='3d') #创建一个三维的绘图工程
#
# #将数据点分成三部分画，在颜色上有区分度
# ax.scatter(X,Y,Z,'markersize',80) #绘制数据点
# plt.show()



plt.figure(1)#创建图表1
#plt.figure(2)#创建图表2
ax1=plt.subplot(311)#在图表2中创建子图1
ax2=plt.subplot(312)#在图表2中创建子图2
ax3=plt.subplot(313)#在图表2中创建子图3
x=np.linspace(0,3,100)
i = 1
plt.figure(1)
plt.plot(x,np.exp(i*x/3))
plt.sca(ax1)
plt.plot(x,np.sin(i*x))
plt.sca(ax2)
plt.plot(x,np.cos(i*x))
plt.sca(ax3)
plt.show()














