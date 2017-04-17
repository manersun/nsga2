#coding=utf-8
from function import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

excel1 = 'z_last_data.xls'
excel2 = 'zDHEW_data.xls'
excel3 = 'zhiliangquanzhong.xls'

picture_type=3   #3画TCQ的3D图,21画Tc图,22画TQ,23画QC
popSize = 100#初始种群大小
times = 10 #杂交次数
pc = 0.9 #交叉概率Q
pm = 0.1 #变异概率
results = []  # 保存每次种群的
#Tn正常工期Lcn工人预计花费Lq工人工作质量Mc材料花费Mq材料质量Ac设备花费Aq设备质量
Tn, Lcn, Lqmin, Mcmin, Mqmin, Acmin, Aqmin, Ecmin, Eqmin, Epmin, Lqmax, Mcmax, Mqmax, Acmax, Aqmax, Ecmax, Eqmax, Epmax, allinfo = gainData(excel1)
DHEws = gainDHEw(excel2)
QWTi,LWTi,MWTi,EWTi,AWTi = gainData2(excel3)#质量权重信息，分别是工序，工人，材料，设备，管理
chromlength = len(allinfo) #总的工序数
matri = gainMatri(excel1,chromlength)#邻接矩阵
Tnsum = 0
kepPathNodes_Tn = getKeyPathNodes(matri, Tn)
keyPath_Tn = getkeyPaths(kepPathNodes_Tn,matri)
keyPath_Tn_base = keyPath_Tn[0]
keyPath_Tn_base.insert(0, 1)
for tn in range(0, len(Tn)):
    if tn+1 in keyPath_Tn_base:
        Tnsum += Tn[tn]
allP=[];TcInfo=[];Lcc=[];Tc=[];Qcsum=0;Tcsum=0;Ccsum=0;Cnsum=0
Tns_all_info=[]
for i in range(0,len(DHEws)):
    p = gainP(DHEws[i])
    allP.append(p)
for i in range(0, chromlength):
    minTcInfo = min_Tc(allinfo[i][3],DHEws,Epmax[i]) #第一个数是取第几个D，H取到的Tc,第二个数是Tc的值,第三个是取到这个Tc时每周的,第四个是相应的D H  Ew
    TcInfo.append(minTcInfo)
    Tc.append(minTcInfo[1])
insertAllP(excel2, allP)
insertAllTc(excel1, TcInfo)
for i in range(0, chromlength):
    Lcci = gainMaxCc(TcInfo[i][2],Lcn[i],allP)    ###########此处有问题。。。如何计算Cc
    Lcc.append(Lcci)
for i in range(0, chromlength):
    Qcsum += QWTi[i]*(LWTi[i]*Lqmin[i]+MWTi[i]*Mqmin[i]+AWTi[i]*Aqmin[i]+EWTi[i]*Eqmin[i])
kepPathNodes_Tc = getKeyPathNodes(matri, Tc)
keyPath_Tc = getkeyPaths(kepPathNodes_Tc,matri)
keyPath_Tc_base = keyPath_Tc[0]
keyPath_Tc_base.insert(0, 1)
for tc in range(0, len(Tn)):
    if tc+1 in keyPath_Tc_base:
        Tcsum += Tc[tc]
Cnsum = sum(Lcn) + sum(Mcmin) + sum(Acmin) + sum(Ecmin);
Ccsum = sum(Lcc) + sum(Mcmax) + sum(Acmax) + sum(Ecmax)
pop = getPop(popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin)
picture_3D_Tsum = [];picture_3D_Csum = [];picture_3D_Qsum = [];
pictureTC_pareto_T=[];pictureTC_pareto_C=[]
pictureQC_pareto_Q=[];pictureQC_pareto_C=[]
pictureTQ_pareto_T=[];pictureTQ_pareto_Q=[]
new_realT_realC_realQ=[]
for time in range(0,times):
    pop_son = evolution(pop,pc,pm,popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin)
    print "第 %s 代种群进化完成==》第 %s 代子种群" % (time,time)
    pop.extend(pop_son)
    print "第 %s 代 父种群和第 %s 代子种群合并完成==>第 %s 代合并种群" % (time,time,time)
    realT_realC_realQ = pareto_front(pop,chromlength,matri,Tn,Lcn,Lqmin,Mcmin,Mqmin,Acmin,Aqmin,Ecmin,Eqmin,Epmin,Lqmax,Mcmax,Mqmax,Acmax,Aqmax,Ecmax,Eqmax,Epmax,QWTi,LWTi,MWTi,AWTi,EWTi,Tc)
    print "第 %s 代 合并种群，适应值计算完成" % (time)
    geti_TCQ_res, getiVal_TCQ_res = divided_TCQ(pop,realT_realC_realQ,len(pop))
    print "第 %s 代合并种群分层完成" % (time)
    pop,new_realT_realC_realQ = get_new_pop(geti_TCQ_res,getiVal_TCQ_res,popSize)
    print "第 %s 代种群生成" % (time + 1)
minT_index,minC_index,maxQ_index = findbest(pop,new_realT_realC_realQ)
print "最短时间方案："
for q in range(0,len(pop[0])):
    Mc = pop[minT_index][q][1];Ac = pop[minT_index][q][2];Ec = pop[minT_index][q][3];DHEw = pop[minT_index][q][0]
    realEp = (Epmax[q] - Epmin[q]) * ((Ec - Ecmin[q]) / (Ecmax[q] - Ecmin[q])) + Epmin[q]
    realTc, realTcs = gainTc(Tn[q], DHEw, realEp)
    realLc = 0
    P = gainP(DHEw)
    for k in range(0, 5):
        kk = (realTcs[k] / (1.0 * realTc)) * Lcn[q] * P[k] / realEp
        realLc += kk
    if (Tn[q] != Tc[q]):
        realLq = Lqmax[q] - ((Lqmax[q] - Lqmin[q]) / (Tn[q] - Tc[q])) * (realTc - Tc[q])
    else:
        realLq = 1
    realMq = ((Mqmax[q] - Mqmin[q]) * (Mc - Mcmin[q]) / (Mcmax[q] - Mcmin[q])) + Mqmin[q]
    realAq = ((Aqmax[q] - Aqmin[q]) * (Ac - Acmin[q]) / (Acmax[q] - Acmin[q])) + Aqmin[q]
    realEq = ((Eqmax[q] - Eqmin[q]) * (Ec - Ecmin[q]) / (Ecmax[q] - Ecmin[q])) + Eqmin[q]
    Q = (LWTi[q] * realLq + MWTi[q] * realMq + AWTi[q] * realAq + EWTi[q] * realEq)
    print "第 %s 道工序，预计%s天完成，预计人工花费%s $，建议%s天完成，需花人工费%s $,其中每周干 %s 天，每天 %s 小时，材料花费 %s $,管理花费 %s $,设备花费 %s $,本道工序完成质量 %s" %  \
          (q+1, Tn[q],Lcn[q],realTc,realLc,DHEw[0], DHEw[1],Mc,Ac,Ec,Q)
print "预计总天数%s,总花费%s,总质量%s" % (new_realT_realC_realQ[minT_index][0],new_realT_realC_realQ[minT_index][1],new_realT_realC_realQ[minT_index][2])
print "最少花费方案："
for q in range(0,len(pop[0])):
    Mc = pop[minC_index][q][1];Ac = pop[minC_index][q][2];Ec = pop[minC_index][q][3];DHEw = pop[minC_index][q][0]
    realEp = (Epmax[q] - Epmin[q]) * ((Ec - Ecmin[q]) / (Ecmax[q] - Ecmin[q])) + Epmin[q]
    realTc, realTcs = gainTc(Tn[q], DHEw, realEp)
    realLc = 0
    P = gainP(DHEw)
    for k in range(0, 5):
        kk = (realTcs[k] / (1.0 * realTc)) * Lcn[q] * P[k] / realEp
        realLc += kk
    if (Tn[q] != Tc[q]):
        realLq = Lqmax[q] - ((Lqmax[q] - Lqmin[q]) / (Tn[q] - Tc[q])) * (realTc - Tc[q])
    else:
        realLq = 1
    realMq = ((Mqmax[q] - Mqmin[q]) * (Mc - Mcmin[q]) / (Mcmax[q] - Mcmin[q])) + Mqmin[q]
    realAq = ((Aqmax[q] - Aqmin[q]) * (Ac - Acmin[q]) / (Acmax[q] - Acmin[q])) + Aqmin[q]
    realEq = ((Eqmax[q] - Eqmin[q]) * (Ec - Ecmin[q]) / (Ecmax[q] - Ecmin[q])) + Eqmin[q]
    Q = (LWTi[q] * realLq + MWTi[q] * realMq + AWTi[q] * realAq + EWTi[q] * realEq)
    print "第 %s 道工序，预计%s天完成，预计人工花费%s $，建议%s天完成，需花人工费%s $,其中每周干 %s 天，每天 %s 小时，材料花费 %s $,管理花费 %s $,设备花费 %s $,本道工序完成质量 %s" %  \
          (q+1, Tn[q],Lcn[q],realTc,realLc,DHEw[0], DHEw[1],Mc,Ac,Ec,Q)
print "预计总天数%s,总花费%s,总质量%s" % (new_realT_realC_realQ[minC_index][0],new_realT_realC_realQ[minC_index][1],new_realT_realC_realQ[minC_index][2])
print "最高质量方案："
for q in range(0,len(pop[0])):
    Mc = pop[maxQ_index][q][1];Ac = pop[maxQ_index][q][2];Ec = pop[maxQ_index][q][3];DHEw = pop[maxQ_index][q][0]
    realEp = (Epmax[q] - Epmin[q]) * ((Ec - Ecmin[q]) / (Ecmax[q] - Ecmin[q])) + Epmin[q]
    realTc, realTcs = gainTc(Tn[q], DHEw, realEp)
    realLc = 0
    P = gainP(DHEw)
    for k in range(0, 5):
        kk = (realTcs[k] / (1.0 * realTc)) * Lcn[q] * P[k] / realEp
        realLc += kk
    if (Tn[q] != Tc[q]):
        realLq = Lqmax[q] - ((Lqmax[q] - Lqmin[q]) / (Tn[q] - Tc[q])) * (realTc - Tc[q])
    else:
        realLq = 1
    realMq = ((Mqmax[q] - Mqmin[q]) * (Mc - Mcmin[q]) / (Mcmax[q] - Mcmin[q])) + Mqmin[q]
    realAq = ((Aqmax[q] - Aqmin[q]) * (Ac - Acmin[q]) / (Acmax[q] - Acmin[q])) + Aqmin[q]
    realEq = ((Eqmax[q] - Eqmin[q]) * (Ec - Ecmin[q]) / (Ecmax[q] - Ecmin[q])) + Eqmin[q]
    Q = (LWTi[q] * realLq + MWTi[q] * realMq + AWTi[q] * realAq + EWTi[q] * realEq)
    print "第 %s 道工序，预计%s天完成，预计人工花费%s $，建议%s天完成，需花人工费%s $,其中每周干 %s 天，每天 %s 小时，材料花费 %s $,管理花费 %s $,设备花费 %s $,本道工序完成质量 %s" %  \
          (q+1, Tn[q],Lcn[q],realTc,realLc,DHEw[0], DHEw[1],Mc,Ac,Ec,Q)
print "预计总天数%s,总花费%s,总质量%s" % (new_realT_realC_realQ[maxQ_index][0],new_realT_realC_realQ[maxQ_index][1],new_realT_realC_realQ[maxQ_index][2])
#pareto_TC_pop,pareto_Tc_real = find_pareto(pop,new_realT_realC_realQ,Tc,Tn)

geti_TC_res, getiVal_TC_res = divided_TC(pop, new_realT_realC_realQ, len(pop))
pictureTC_pareto_T.extend(x[0] for x in getiVal_TC_res[0])
pictureTC_pareto_C.extend(x[1] for x in getiVal_TC_res[0])
fig1 = plt.figure('T_C')
plt.scatter(pictureTC_pareto_T, pictureTC_pareto_C)
plt.title('T_C_Pareto_Picture')
plt.xlabel('T/day')
plt.ylabel('C/$')


geti_TQ_res, getiVal_TQ_res = divided_TQ(pop, new_realT_realC_realQ, len(pop))
pictureTQ_pareto_T.extend(x[0] for x in getiVal_TQ_res[0])
pictureTQ_pareto_Q.extend(x[2] for x in getiVal_TQ_res[0])
fig2 = plt.figure('T_Q')
plt.scatter(pictureTQ_pareto_T, pictureTQ_pareto_Q)
plt.title('T_Q_Pareto_Picture')
plt.xlabel('T/day')
plt.ylabel('Q')


geti_QC_res, getiVal_QC_res = divided_QC(pop, realT_realC_realQ, len(pop))
pictureQC_pareto_Q.extend(x[2] for x in getiVal_QC_res[0])
pictureQC_pareto_C.extend(x[1] for x in getiVal_QC_res[0])
fig3 = plt.figure('Q_C')
plt.scatter(pictureQC_pareto_Q, pictureQC_pareto_C)
plt.title('Q_C_Pareto_Picture')
plt.xlabel('Q')
plt.ylabel('C/$')

picture_3D_Tsum.extend([x[0] for x in new_realT_realC_realQ])
picture_3D_Csum.extend([x[1] for x in new_realT_realC_realQ])
picture_3D_Qsum.extend([x[2] for x in new_realT_realC_realQ])
fig4 = plt.figure('T_C_Q')
ax=fig4.add_subplot(111,projection='3d') #创建一个三维的绘图工程
ax.set_title('T_C_Q_3D_Picture')
ax.scatter(picture_3D_Tsum,picture_3D_Csum,picture_3D_Qsum,'markersize',2) #绘制数据点
ax.set_xlabel('Time/day')
ax.set_ylabel('Cost/$')
ax.set_zlabel('Quality')
plt.show()
# if(picture_type==21):
#     for time in range(0,times):
#         pop_son = evolution(pop,pc,pm,popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin)
#         print "第 %s 代种群进化完成==》第 %s 代子种群" % (time, time)
#         pop.extend(pop_son)
#         print "第 %s 代 父种群和第 %s 代子种群合并完成==》第 %s 代合并种群" % (time, time,time)
#         realT_realC_realQ = pareto_front(pop,chromlength,matri,Tn,Lcn,Lqmin,Mcmin,Mqmin,Acmin,Aqmin,Ecmin,Eqmin,Epmin,Lqmax,Mcmax,Mqmax,Acmax,Aqmax,Ecmax,Eqmax,Epmax,QWTi,LWTi,MWTi,AWTi,EWTi,Tc)
#         print "第 %s 代 合并种群，适应值计算完成" % (time)
#         geti_TC_res, getiVal_TC_res = divided_TC(pop,realT_realC_realQ,len(pop))
#         print "第 %s 代合并种群分层完成" % (time)
#         pop,new_realT_realC_realQ = get_new_pop(geti_TC_res,getiVal_TC_res,popSize)
#         print "第 %s 代种群生成" % (time+1)
#     pictureTC_pareto_T.extend(x[0] for x in getiVal_TC_res[0])
#     pictureTC_pareto_C.extend(x[1] for x in getiVal_TC_res[0])
#     fig = plt.figure(figsize=(30,30))
#     plt.scatter(pictureTC_pareto_T, pictureTC_pareto_C)
#     plt.title('T_C_Pareto_Picture')
#     plt.xlabel('T/day')
#     plt.ylabel('C/$')
#     plt.show()
# if(picture_type==22): #TQ
#     for time in range(0,times):
#         pop_son = evolution(pop,pc,pm,popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin)
#         print "第 %s 代种群进化完成==》第 %s 代子种群" % (time, time)
#         pop.extend(pop_son)
#         print "第 %s 代 父种群和第 %s 代子种群合并完成==》第 %s 代合并种群" % (time, time,time)
#         realT_realC_realQ = pareto_front(pop,chromlength,matri,Tn,Lcn,Lqmin,Mcmin,Mqmin,Acmin,Aqmin,Ecmin,Eqmin,Epmin,Lqmax,Mcmax,Mqmax,Acmax,Aqmax,Ecmax,Eqmax,Epmax,QWTi,LWTi,MWTi,AWTi,EWTi,Tc)
#         print "第 %s 代 合并种群，适应值计算完成" % (time)
#         geti_TQ_res, getiVal_TQ_res = divided_TQ(pop, realT_realC_realQ, len(pop))
#         print "第 %s 代合并种群分层完成" % (time)
#         pop,new_realT_realC_realQ = get_new_pop(geti_TQ_res,getiVal_TQ_res,popSize)
#         print "第 %s 代种群生成" % (time+1)
#     pictureTQ_pareto_T.extend(x[0] for x in getiVal_TQ_res[0])
#     pictureTQ_pareto_Q.extend(x[2] for x in getiVal_TQ_res[0])
#     fig = plt.figure(figsize=(30,30))
#     plt.scatter(pictureTQ_pareto_T, pictureTQ_pareto_Q)
#     plt.title('T_Q_Pareto_Picture')
#     plt.xlabel('T/day')
#     plt.ylabel('Q')
#     plt.show()
# if(picture_type==23): #QC
#     for time in range(0,times):
#         pop_son = evolution(pop,pc,pm,popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin)
#         print "第 %s 代种群进化完成==》第 %s 代子种群" % (time, time)
#         pop.extend(pop_son)
#         print "第 %s 代 父种群和第 %s 代子种群合并完成==》第 %s 代合并种群" % (time, time,time)
#         realT_realC_realQ = pareto_front(pop,chromlength,matri,Tn,Lcn,Lqmin,Mcmin,Mqmin,Acmin,Aqmin,Ecmin,Eqmin,Epmin,Lqmax,Mcmax,Mqmax,Acmax,Aqmax,Ecmax,Eqmax,Epmax,QWTi,LWTi,MWTi,AWTi,EWTi,Tc)
#         print "第 %s 代 合并种群，适应值计算完成" % (time)
#         geti_QC_res, getiVal_QC_res = divided_QC(pop, realT_realC_realQ, len(pop))
#         print "第 %s 代合并种群分层完成" % (time)
#         pop,new_realT_realC_realQ = get_new_pop(geti_QC_res,getiVal_QC_res,popSize)
#         print "第 %s 代种群生成" % (time+1)
#     # for o in range(len(getiVal_QC_res)):
#     #     pictureQC_pareto_Q.extend(x[2] for x in getiVal_QC_res[o])
#     #     pictureQC_pareto_C.extend(x[1] for x in getiVal_QC_res[o])
#     pictureQC_pareto_Q.extend(x[2] for x in getiVal_QC_res[0])
#     pictureQC_pareto_C.extend(x[1] for x in getiVal_QC_res[0])
#     fig = plt.figure(figsize=(30,30))
#     plt.scatter(pictureQC_pareto_Q, pictureQC_pareto_C)
#     plt.title('Q_C_Pareto_Picture')
#     plt.xlabel('Q')
#     plt.ylabel('C/$')
#     plt.show()