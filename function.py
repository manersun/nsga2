#coding=utf-8
import xlrd
from numpy import zeros
from xlutils.copy import copy;
import os,math
import random

x=1.5;
def evolution(pop,pc,pm,popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin):
    pop_son = []
   # for i in range(popSize - 1):
    i = 0;
    while(i<popSize):
        if (random.random() < pc and i!=popSize-1):   #进行交叉
            cpoint = random.randint(0, chromlength-1)
            temp1 = [];
            temp2 = []
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i+1][cpoint:len(pop[i])])
            temp2.extend(pop[i+1][0:cpoint])
            temp2.extend(pop[i][cpoint:len(pop[i])])
            pop_son.append(temp1)
            pop_son.append(temp2)
            i += 2
        else: #进行变异
            temp3 = pop[i]
            mutapoint = random.randint(0, chromlength-1)
            rand_DH = random.randint(0, len(DHEws) - 1)
            rand_Mc = random.randint(Mcmin[mutapoint], Mcmax[mutapoint])
            rand_Ac = random.randint(Acmin[mutapoint], Acmax[mutapoint])
            rand_Ec = random.randint(Ecmin[mutapoint], Ecmax[mutapoint])
            temp3[mutapoint][0] = DHEws[rand_DH]
            temp3[mutapoint][1] = rand_Mc
            temp3[mutapoint][2] = rand_Ac
            temp3[mutapoint][3] = rand_Ec
            pop_son.append(temp3)
            i += 1
    return pop_son;
def divided_TCQ(newpop,new_realT_realC_realQ,length):
    pop = newpop[:]
    realT_realC_realQ = new_realT_realC_realQ[:]
    divided = 0;geti_res=[];getiVal_res=[]
    while(divided<length):
        popsize = length-divided
        geti_temp = [];getiVal_temp=[];divided_index=[];
        for i in range(popsize):
            np=0;
            currentVal = realT_realC_realQ[i]
            for j in range(popsize):
                loopVal = realT_realC_realQ[j]
                if(i == j): continue
                else:
                    if(currentVal[0]>loopVal[0] and currentVal[1]>=loopVal[1] and currentVal[2]<=loopVal[2])\
                            or (currentVal[0]>=loopVal[0] and currentVal[1]>loopVal[1] and currentVal[2]<=loopVal[2]) \
                            or (currentVal[0]>=loopVal[0] and currentVal[1]>=loopVal[1] and currentVal[2]<loopVal[2]):
                        np = 1;break;
                    else:
                        continue;
            if(np != 0):continue
            else:
                geti_temp.append(pop[i]);getiVal_temp.append(realT_realC_realQ[i]);divided_index.append(i)
                divided += 1
        for k in range(len(geti_temp)):
            #print "当前k值是 %s,当前pop大小为 %s，当前已分的元素个数是%s" %  (k,len(pop),divided)
            pop.remove(geti_temp[k]);realT_realC_realQ.remove(getiVal_temp[k])
        geti_res.append(geti_temp);getiVal_res.append(getiVal_temp)
    return geti_res,getiVal_res

def divided_TC(newpop,new_realT_realC_realQ,length):
    pop = newpop[:]
    realT_realC_realQ = new_realT_realC_realQ[:]
    divided = 0;geti_res=[];getiVal_res=[]
    while(divided<length):
        popsize = length-divided
        geti_temp = [];getiVal_temp=[];divided_index=[];
        for i in range(popsize):
            np=0;
            currentVal = realT_realC_realQ[i]
            for j in range(popsize):
                loopVal = realT_realC_realQ[j]
                if(i == j): continue
                else:
                    if(currentVal[0]>loopVal[0] and currentVal[1]>=loopVal[1]) or (currentVal[0]>=loopVal[0] and currentVal[1]>loopVal[1]):
                        np = 1;break;
                    else:
                        continue;
            if(np != 0):continue
            else:
                geti_temp.append(pop[i]);getiVal_temp.append(realT_realC_realQ[i]);divided_index.append(i)
                divided += 1
        for k in range(len(geti_temp)):
            #print "当前k值是 %s,当前pop大小为 %s，当前已分的元素个数是%s" %  (k,len(pop),divided)
            pop.remove(geti_temp[k]);realT_realC_realQ.remove(getiVal_temp[k])
        geti_res.append(geti_temp);getiVal_res.append(getiVal_temp)
    return geti_res,getiVal_res
def divided_TQ(newpop,new_realT_realC_realQ,length):
    pop = newpop[:]
    realT_realC_realQ = new_realT_realC_realQ[:]
    divided = 0;geti_res=[];getiVal_res=[]
    while(divided<length):
        popsize = length-divided
        geti_temp = [];getiVal_temp=[];divided_index=[];
        for i in range(popsize):
            np=0;
            currentVal = realT_realC_realQ[i]
            for j in range(popsize):
                loopVal = realT_realC_realQ[j]
                if(i == j): continue
                else:
                    if(currentVal[0]>loopVal[0] and currentVal[2]<=loopVal[2]) or (currentVal[0]>=loopVal[0] and currentVal[2]<loopVal[2]):
                        np = 1;break;Q
                    else:
                        continue;
            if(np != 0):continue
            else:
                geti_temp.append(pop[i]);getiVal_temp.append(realT_realC_realQ[i]);divided_index.append(i)
                divided += 1
        for k in range(len(geti_temp)):
            #print "当前k值是 %s,当前pop大小为 %s，当前已分的元素个数是%s" %  (k,len(pop),divided)
            pop.remove(geti_temp[k]);realT_realC_realQ.remove(getiVal_temp[k])
        geti_res.append(geti_temp);getiVal_res.append(getiVal_temp)
    return geti_res,getiVal_res
def divided_QC(newpop,new_realT_realC_realQ,length):
    pop = newpop[:]
    realT_realC_realQ = new_realT_realC_realQ[:]
    divided = 0;geti_res=[];getiVal_res=[]
    while(divided<length):
        popsize = length-divided
        geti_temp = [];getiVal_temp=[];divided_index=[];
        for i in range(popsize):
            np=0;
            currentVal = realT_realC_realQ[i]
            for j in range(popsize):
                loopVal = realT_realC_realQ[j]
                if(i == j): continue
                else:
                    if(currentVal[1]>loopVal[1] and currentVal[2]<=loopVal[2]) or (currentVal[1]>=loopVal[1] and currentVal[2]<loopVal[2]):
                        np = 1;break;Q
                    else:
                        continue;
            if(np != 0):continue
            else:
                geti_temp.append(pop[i]);getiVal_temp.append(realT_realC_realQ[i]);divided_index.append(i)
                divided += 1
        for k in range(len(geti_temp)):
            #print "当前k值是 %s,当前pop大小为 %s，当前已分的元素个数是%s" %  (k,len(pop),divided)
            pop.remove(geti_temp[k]);realT_realC_realQ.remove(getiVal_temp[k])
        geti_res.append(geti_temp);getiVal_res.append(getiVal_temp)
    return geti_res,getiVal_res
def find_pareto(pop,new_realT_realC_realQ,Tc,Tn):
    pareto_TC_pop = [];
    pareto_Tc_real = [];
    for k in range(100,sum(Tn)+1):
        min_Cc = 999999999;min_index = 0;ishave=False
        for l in range(len(new_realT_realC_realQ)):
            if(new_realT_realC_realQ[l][0]==k):
                ishave=True
                if (min_Cc > new_realT_realC_realQ[l][1]):
                    min_Cc = new_realT_realC_realQ[l][1];
                    min_index = l
        if(ishave):
            pareto_TC_pop.append(pop[min_index]);
            pareto_Tc_real.append(new_realT_realC_realQ[min_index])
    return pareto_TC_pop,pareto_Tc_real
#***************************
def get_new_pop(geti_res,getiVal_res,popSize):
    initsize=0;res=[];new_realT_realC_realQ=[]
    for i in range(len(geti_res)):
        count = initsize + len(geti_res[i])
        if((count)<popSize):
            initsize += len(geti_res[i])
            res.extend(geti_res[i])
            new_realT_realC_realQ.extend(getiVal_res[i])
        else:
            k = popSize - initsize
            res.extend(geti_res[i][0:k])
            new_realT_realC_realQ.extend(getiVal_res[i][0:k])
            break
    return res,new_realT_realC_realQ;
def calobjValue(pop, popSize, chromlength, Tnsum, Tcsum, Cnsum, Ccsum, Qcsum,matri,Tn,Lcn,Lqmin,Mcmin,Mqmin,Acmin,Aqmin,Lqmax,Mcmax,Mqmax,Acmax,Aqmax,QWTi,LWTi,MWTi,AWTi,Tc):
    obj_value = [];
    for i in range(0, popSize):  #遍历每一个个体
        Tsum = 0;Csum = 0;Qsum = 0;Umax = 0;realAllTc=[];Tsum=0;realAllLc=[];realAllLq=[];realAllMq=[];realAllAq=[]
        realAllMc=[];realAllAc=[]
        for j in range(0, chromlength):  #对个体进行评价
            realLc = 0;
            DHEw = pop[i][j][0];realMc = pop[i][j][1];realAc = pop[i][j][2]
            D = pop[i][j][0][0];H = pop[i][j][0][1];Ew = pop[i][j][0][2:]
            #计算Csum
            realTc,realTcs = gainTc(Tn[j],DHEw)
            realAllTc.append(realTc)
            P = gainP(DHEw)
            for k in range(0,5):
                kk = (realTcs[k]/(1.0*realTc))*Lcn[j]*P[k]
                realLc += kk
            realAllLc.append(realLc)
            #计算Qsum
            if(Tn[j] != Tc[j]):
                realLq = Lqmax[j] - ((Lqmax[j]-Lqmin[j])/(Tn[j]-Tc[j]))*(realTc-Tc[j])
            else:
                realLq = 1
            realMq = Mqmax[j] - ((Mqmax[j]-Mqmin[j])/(Mcmax[j]-Mcmin[j]))*(realMc-Mcmin[j])
            realAq = Aqmax[j] - ((Aqmax[j] - Aqmin[j]) / (Acmax[j] - Acmin[j])) * (realAc - Acmin[j])
            realAllLq.append(realLq)
            realAllMq.append(realMq)
            realAllAq.append(realAq)
            realAllMc.append(realMc)
            realAllAc.append(realAc)
        for q in range(0,chromlength):
            Qsum += QWTi[q] * (LWTi[q] * realAllLq[q] + MWTi[q] * realAllMq[q] + AWTi[q] * realAllAq[q])
        Csum = sum(realAllLc) + sum(realAllMc) + sum(realAllAc)
        keyPathNodes = getKeyPathNodes(matri,realAllTc)
        keyPaths = getkeyPaths(keyPathNodes,matri)
        keyPaths[0].insert(0, 1)
        keyPath = keyPaths[0]
        for key in range(1,len(realAllTc)):
            if key in keyPath:
                Tsum += realAllTc[key-1]
        Uc = gainUc(Cnsum,Ccsum,Csum)
        Ut = gainUt(Tnsum,Tcsum,Tsum)
        Uq = gainQc(Qcsum,Qsum)
        Umax = 0.3 * Ut + 0.4 * Uc + 0.3 * Uq
        Umax_info = []
        Umax_info.append(Umax)
        Umax_info.append(Tsum)
        Umax_info.append(Csum)
        Umax_info.append(Qsum)
        Umax_info.append(Tnsum)
        Umax_info.append(Tcsum)
        Umax_info.append(Cnsum)
        Umax_info.append(Ccsum)
        Umax_info.append(keyPath)
        obj_value.append(Umax_info)
    return obj_value
#****************************
def pareto_front(new_pop,chromlength,matri,Tn,Lcn,Lqmin,Mcmin,Mqmin,Acmin,Aqmin,Ecmin,Eqmin,Epmin,Lqmax,Mcmax,Mqmax,Acmax,Aqmax,Ecmax,Eqmax,Epmax,QWTi,LWTi,MWTi,AWTi,EWTi,Tc):
    popsize = len(new_pop);
    realT_realC_realQ = []
    for i in range(popsize):
        temp = [];realAllTc=[];Tsum=0;realAllLc=[];realAllLq=[];realAllMq=[];realAllAq=[];realAllEc=[];realAllEq=[];realAllEp=[];realAllMc=[];realAllAc=[]
        Qsum = 0;Tsum=0;Csum=0
        for j in range(chromlength):
            DHEw = new_pop[i][j][0];realMc = new_pop[i][j][1];realAc = new_pop[i][j][2];realEc=new_pop[i][j][3]
            realEp = (Epmax[j]-Epmin[j])*((realEc-Ecmin[j])/(Ecmax[j]-Ecmin[j]))+Epmin[j]
            realTc, realTcs = gainTc(Tn[j], DHEw,realEp)
            realAllTc.append(realTc)
            P = gainP(DHEw)
            realLc=0
            for k in range(0, 5):
                kk = (realTcs[k] / (1.0 * realTc)) * Lcn[j] * P[k]/realEp
                realLc += kk
            realAllLc.append(realLc)
            realAllMc.append(realMc)
            realAllAc.append(realAc)
            realAllEc.append(realEc)
            # 计算Qsum
            if (Tn[j] != Tc[j]):
                realLq = Lqmax[j] - ((Lqmax[j] - Lqmin[j]) / (Tn[j] - Tc[j])) * (realTc - Tc[j])
            else:
                realLq = 1
            realMq = ((Mqmax[j] - Mqmin[j])* (realMc - Mcmin[j]) / (Mcmax[j] - Mcmin[j])) + Mqmin[j]
            realAq = ((Aqmax[j] - Aqmin[j])* (realAc - Acmin[j]) / (Acmax[j] - Acmin[j])) + Aqmin[j]
            realEq = ((Eqmax[j] - Eqmin[j])* (realEc - Ecmin[j]) / (Ecmax[j] - Ecmin[j])) + Eqmin[j]
            realAllLq.append(realLq)
            realAllMq.append(realMq)
            realAllAq.append(realAq)
            realAllEq.append(realEq)
        for q in range(0, chromlength):
            Qsum += QWTi[q] * (LWTi[q] * realAllLq[q] + MWTi[q] * realAllMq[q] + AWTi[q] * realAllAq[q] + EWTi[q]*realAllEq[q])
            #Csum += realLc[q] + realMc[q] + realAc[q] + realEc[q]
        keyPathNodes = getKeyPathNodes(matri, realAllTc)
        keyPaths = getkeyPaths(keyPathNodes, matri)
        keyPaths[0].insert(0, 1)
        keyPath = keyPaths[0]
        for key in range(1, len(realAllTc)):
            if key in keyPath:
                Tsum += realAllTc[key - 1]
        Csum = sum(realAllLc) +  sum(realAllMc) +  sum(realAllAc) +  sum(realAllEc)
        temp.append(Tsum)
        temp.append(Csum)
        temp.append(Qsum)
        realT_realC_realQ.append(temp)
    return realT_realC_realQ;

def gainMatri(excel,chromlength):
    data = xlrd.open_workbook(excel)
    sheet_0 = data.sheet_by_index(0)
    total_nrow_0 = sheet_0.nrows
    gx = [];follow = [];tt = zeros([chromlength+2, chromlength+2]) # +1为了让工序数和数组坐标对应，0行0列不存值,再+1是为了表示21是end
    for i in range(3, total_nrow_0):
        gxi = int(sheet_0.cell(i, 1).value)
        followi = str(sheet_0.cell(i, 2).value)
        temps = followi.strip().split(',')
        for j in range(0, len(temps)):
            y = int(float(temps[j]))
            tt[gxi][y] = 1
    return tt
# 返回所有信息
def gainData(excel):
    allinfo = []
    Tn=[];Lc=[];Lqmin=[];Mcmin=[];Mqmin=[];Acmin=[];Aqmin=[];Lqmax=[];Mcmax=[];Mqmax=[];Acmax=[];Aqmax=[];Ecmin=[];Eqmin=[];Epmin=[];Ecmax=[];Eqmax=[];Epmax=[];
    data = xlrd.open_workbook(excel)
    sheet_0 = data.sheet_by_index(0)
    total_nrow_0 = sheet_0.nrows
    for i in range(3, total_nrow_0):
        Tn.append(int(sheet_0.cell(i, 3).value))
        Lc.append(float(sheet_0.cell(i, 4).value))
        Lq = sheet_0.cell(i, 5).value.split('-')
        Lqmin.append(float(Lq[0]));
        Lqmax.append(float(Lq[1]));
        Mc = sheet_0.cell(i, 6).value.split('-')
        Mcmin.append(float(Mc[0]));
        Mcmax.append(float(Mc[1]));
        Mq = sheet_0.cell(i, 7).value.split('-')
        Mqmin.append(float(Mq[0]));
        Mqmax.append(float(Mq[1]));
        Ac = sheet_0.cell(i, 8).value.split('-')
        Acmin.append(float(Ac[0]));
        Acmax.append(float(Ac[1]));
        Aq = sheet_0.cell(i, 9).value.split('-')
        Aqmin.append(float(Aq[0]));
        Aqmax.append(float(Aq[1]));
        Ec = sheet_0.cell(i, 10).value.split('-')
        Ecmin.append(float(Ec[0]));
        Ecmax.append(float(Ec[1]));
        Eq = sheet_0.cell(i, 11).value.split('-')
        Eqmin.append(float(Eq[0]));
        Eqmax.append(float(Eq[1]));
        Ep = sheet_0.cell(i, 12).value.split('-')
        Epmin.append(float(Ep[0]));
        Epmax.append(float(Ep[1]));
        allinfo.append(sheet_0.row_values(i, 0, 13))
    return Tn, Lc, Lqmin, Mcmin, Mqmin, Acmin, Aqmin, Ecmin, Eqmin, Epmin, Lqmax, Mcmax, Mqmax, Acmax, Aqmax, Ecmax, Eqmax, Epmax, allinfo
# 返回一个二维数组，存的是不同D，H，以及相对应Ew
def gainDHEw(excel):
    DHEwi=[[]]
    data = xlrd.open_workbook(excel)
    sheet = data.sheet_by_index(0)
    total_nrow = sheet.nrows
    for i in range(1, total_nrow):
        temp = []
        temp.append(int(math.ceil(sheet.cell(i, 0).value)))
        temp.append(int(math.ceil(sheet.cell(i, 1).value)))
        for j in range(0,5):
            temp.append(float('%.4f' % (sheet.cell(i, j+2).value)))
        DHEwi.append(temp)
    return DHEwi[1:]
def gainData2(excel):
    QWTi=[];LWTi=[];MWTi=[];AWTi=[];EWTi=[]
    data = xlrd.open_workbook(excel)
    sheet = data.sheet_by_index(0)
    total_nrow = sheet.nrows
    for i in range(3, total_nrow):
        QWTi.append(sheet.cell(i, 3).value)
        LWTi.append(sheet.cell(i, 4).value)
        MWTi.append(sheet.cell(i, 5).value)
        EWTi.append(sheet.cell(i, 6).value)
        AWTi.append(sheet.cell(i, 7).value)
    return QWTi,LWTi,MWTi,EWTi,AWTi
# 获取Tc
def gainP(DHEw):
    D = DHEw[0];H=DHEw[1];Ew=DHEw[2:len(DHEw)+1]
    p = [0]*5
    for i in range(0, 5):
        temp = (40+(D*H-40)*x)/(D*H*Ew[i])
        p[i] = float('%.4f' % temp)
    return p
#插入
def insertAllP(excel,allP):
    data = xlrd.open_workbook(excel)
    wb = copy(data)
    sheetw = wb.get_sheet(0)
    sheet = data.sheet_by_index(0)
    total_nrow = sheet.nrows
    for i in range(1, total_nrow):
        for j in range(7, 12):
            sheetw.write(i, j, allP[i-1][j-7])
    os.remove(excel)
    wb.save(excel)
def gainTc(Tn,DHEw,Ep):
    D = DHEw[0];H=DHEw[1];Ew=DHEw[2:]
    Tc = [0]*5;Tw=[0]*5
    Tw[0] = int(math.ceil((Tn * 8 - H * D * Ew[0]*Ep)))
    if(Tw[0]>=0):
        Tc[0] = D
        for i in range(1, 4):
            Tw[i] = int(math.ceil((Tw[i-1] - H*D*Ew[i]*Ep)))
            if(Tw[i]>=0):
                Tc[i] = D
                Tw[i+1] = int(math.ceil((Tw[i] - H*D*Ew[i+1]*Ep)))
            else:
                Tc[i] = int(math.ceil((Tw[i-1]/(H*Ew[i]*Ep))))
                return sum(Tc),Tc
    else:
        Tc[0] = int(math.ceil(((Tn * 8)/(H*Ew[0]*Ep))))
        return sum(Tc),Tc
    if(Tw[3]!=0 and Tw[4]>=0):
        Tc[4] = D
    elif(Tw[3]!=0 and Tw[4]<0):
        Tc[4] = int(math.ceil((Tw[3]/(H*Ew[4]*Ep))))
    else:
        Tc[4] = 0
    return sum(Tc),Tc
#插入
def insertAllTc(excel,TcInfo):
    data = xlrd.open_workbook(excel)
    wb = copy(data)
    sheetw = wb.get_sheet(0)
    sheet = data.sheet_by_index(0)
    total_nrow = sheet.nrows
    for i in range(3, total_nrow):
        sheetw.write(i, 13, TcInfo[i-3][1])
    os.remove(excel)
    wb.save(excel)
def min_Tc(Tn, DHEws, Ep):
    minTcInfo=[]
    minTcs = [0]*5
    minTc = 9999
    minIndex = 0
    minTc_DHEw = 0
    for i in range(0,len(DHEws)):
        sumTc, Tcs = gainTc(Tn, DHEws[i], Ep)
        if(sumTc<minTc and (Tcs[3]!=Tcs[4] or Tcs[3]==Tcs[4]==0)):
            for j in range(0, 5):
                minTcs[j] = Tcs[j]
            minTc = sumTc
            minIndex = i
            minTc_DHEw = DHEws[i]
    minTcInfo.append(minIndex)
    minTcInfo.append(minTc)
    minTcInfo.append(minTcs)
    minTcInfo.append(minTc_DHEw)
    return minTcInfo
def gainCc(Tc, Nc, P):
    Tcsum = sum(Tc);Cc = 0
    for i in range(0, 5):
        Cc += int(math.ceil((Tc[i]*P[i]*Nc)/Tcsum))
    return Cc
def gainMaxCc(Tc,Nc,allP):
    Tcsum = sum(Tc);maxCc=0
    for j in range(0,len(allP)):
        Cc = 0;
        for k in range(0, 5):
            Cc += int(math.ceil((Tc[k] * allP[j][k] * Nc) / Tcsum))
        if(Cc > maxCc):
            maxCc = Cc
    return maxCc
def gainRealLq(Lqmax,Lqmin,Tn,Tc,realTc):
    realLq = Lqmax-(Lqmax-Lqmin)/(Tn-Tc)*(realTc-Tc)
    return realLq
def gainRealMq(Mqmax,Mqmin,Mcmax,Mcmin,realMc):
    realMq = Mqmax-(Mqmax-Mqmin)/(Mcmax-Mcmin)*(realMc-Mcmin)
    return realMq
def gainRealAq(Aqmax,Aqmin,Acmax,Acmin,realAc):
    realAq = Aqmax-(Aqmax-Aqmin)/(Acmax-Acmin)*(realAc-Acmin)
    return realAq
def gainRealQc(QWTi,realLq,realMq,realAq,LWTi,MWTi,AWTi):
    return QWTi * (LWTi * realLq + MWTi * realMq + AWTi * realAq)

def getPop(popSize,chromlength,DHEws,Mcmax,Mcmin,Acmax,Acmin,Ecmax,Ecmin):
    pop = [[]]
    for i in range(0, popSize):
        temp_pop = []
        for j in range(0, chromlength):
            temp = []
            rand_DH = random.randint(0, len(DHEws)-1)  #随机数包括0和最大数
            rand_Mc = random.randint(Mcmin[j],Mcmax[j])
            rand_Ac = random.randint(Acmin[j],Acmax[j])
            rand_Ec = random.randint(Ecmin[j],Ecmax[j])
            temp.append(DHEws[rand_DH])
            temp.append(rand_Mc)
            temp.append(rand_Ac)
            temp.append(rand_Ec)
            temp_pop.append(temp)
        pop.append(temp_pop)
    return pop[1:]

def getKeyPathNodes(matri, Tc):   #Tc[0] 是第一道工序的天数，在矩阵中在行数的下标是1，第20道工序在Tc中是Tc[19] 在矩阵中是20
    ve=[];vl=[];keyPathNodes=[]
    for i in range(1, len(Tc)+1): #矩阵第0行全都是0
        for j in range(0, len(matri)):
            if(matri[i][j] != 0):
                matri[i][j] = Tc[i-1]
    ve = [0] * len(matri)
    vl = [0] * len(matri)
    ve[0] = 0
    for i in range(1, len(matri)):  # 列
        max = 0
        for j in range(0, i):  # 行
            if (matri[j][i] != 0):
                temp = int(ve[j] + matri[j][i])
                if (max < temp):
                    max = temp
        ve[i] = max
    vl[len(matri) - 1] = ve[len(matri) - 1]
    for i in range(0, len(matri)-1)[::-1]:
        min = 9999
        for j in range(i + 1, len(matri)):
            if (matri[i][j] != 0):
                temp = int(vl[j] - matri[i][j])
                if (min > temp):
                    min = temp
        vl[i] = min
    for i in range(1,len(matri)):
        if(ve[i]==vl[i]):
            keyPathNodes.append(i)
    return keyPathNodes

def initKeyPath(matri):
    keyPath = []
    for i in range(len(matri)):
        one = []
        if (matri[1][i] != 0):
            one.append(i)
            keyPath.append(one)
    return keyPath

def getkeyPaths(keyPathNodes, matri):
    keyPath = initKeyPath(matri)
    for j in range(0, len(keyPathNodes)):
        for k in range(0, len(keyPath)):
            list = keyPath[k]
            index = keyPathNodes[j]
            if(list[-1]==index):
                temp = keyPath[k]
                for q in range(index+1, len(matri)):
                    if(matri[index][q]!=0 and q in keyPathNodes):
                        keyPath[k].append(q)
    return keyPath
# 获取Ut
def gainUt(Tnsum, Tcsum, Tsum):
    Ut = 1-float((Tsum-Tcsum)**2)/(Tcsum-Tnsum)**2
    Ut = float('%.4f' % Ut)
    return Ut
# 获取Uc
def gainUc(Cnsum, Ccsum, Csum):
    Uc = 1-float((Csum-Cnsum)**2)/(Ccsum-Cnsum)**2
    Uc = float('%.4f' % Uc)
    return Uc
#获取Qc
def gainQc(Qcsum, Qsum):
    Uq = 1-float((Qsum-1)**2)/(Qcsum-1)**2
    Uq = float('%.4f' % Uq)
    return Uq
#淘汰函数 Umax低于0.5的淘汰
def calfitValue(obj_value):
    fit_value = []
    for i in range(0, len(obj_value)):
        if(obj_value[i]<0.5):
            fit_value.append(0)
        else:
            fit_value.append(obj_value[i])
    return fit_value
#选取最优个体
def best(pop, fit_value):
    best = []
    px = len(pop)
    best_individual = pop[0]
    best_fit = fit_value[0]
    best_individual_index=0
    for i in range(1, px):
        if (fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual = pop[i]
            best_individual_index = i
    best.append(best_fit)
    best.append(best_individual_index)
    best.append(best_individual)
    return best
# 计算累计概率
def cumsum(newfit_value):
    for i in range(len(newfit_value)-2, -1, -1):
        t=0;j=0
        while(j<=i):
            t += newfit_value[j]
            j += 1
        newfit_value[i] = t
    newfit_value[len(newfit_value)-1] = 1
    return newfit_value
def selection(pop, fit_value):
    for i in range(0, len(pop)):
        if (fit_value[i] == 0):
            for j in range(i + 1, len(pop)):
                if (fit_value[j] != 0):
                    pop[i] = pop[j]
                    break
        else:
            continue
    return pop
def selection2(pop, fit_value,best_indivdual):
    best_index = best_indivdual[1]
    for i in range(0, len(pop)):
        if(fit_value[i] == 0):
            pop[i] = pop[best_index]
    return pop
def selection1(pop, fit_value):
    newfit_value = []
    # 适应度总和
    total_fit = sum(fit_value)
    for i in range(len(fit_value)):
        newfit_value.append(fit_value[i] / total_fit)
    # 计算累计概率
    newfit_value = cumsum(newfit_value)
    ms = []
    pop_len = len(pop)
    for i in range(pop_len):
        ms.append(random.random())
    ms.sort()
    fitin = 0
    newin = 0
    newpop = pop
    # 转轮盘选择法
    while newin < pop_len:
        if (ms[newin] < newfit_value[fitin]):
            newpop[newin] = pop[fitin]
            newin = newin + 1
        else:
            fitin = fitin + 1
    pop = newpop
    return pop
# 交配  pc是交配概率
def crossover(pop, pc):
    pop_len = len(pop)
    for i in range(pop_len - 1):
        if (random.random() < pc):
            x = random.randint(0, len(pop)-1)
            y = random.randint(0, len(pop)-1)
            cpoint = random.randint(0, len(pop[0]))
            temp1 = [];temp2 = []
            temp1.extend(pop[x][0:cpoint])
            temp1.extend(pop[y][cpoint:len(pop[i])])
            temp2.extend(pop[y][0:cpoint])
            temp2.extend(pop[x][cpoint:len(pop[i])])
            pop[x] = temp1
            pop[y] = temp2
    return pop
# 变异，随机变异成其他D,h
def mutation(pop, pm,DHEws,Mcmax,Mcmin,Acmax,Acmin ):
    px = len(pop)
    py = len(pop[0])
    for i in range(px):
        if (random.random() < pm):
            index = random.randint(0, py - 1)
            rand_DH = random.randint(0, len(DHEws) - 1)
            rand_Mc = random.randint(Mcmin[index], Mcmax[index])
            rand_Ac = random.randint(Acmin[index], Acmax[index])
            pop[i][index][0] = DHEws[rand_DH]
            pop[i][index][1] = rand_Mc
            pop[i][index][2] = rand_Ac
    return pop
def findbest(pop,new_realT_realC_realQ):
    minT = 9999;minC = 999999999;maxQ=0;minT_index=0;minC_index=0;maxQ_index=0
    for i in range (len(pop)):
        currentT=new_realT_realC_realQ[i][0];currentC=new_realT_realC_realQ[i][1];currentQ=new_realT_realC_realQ[i][1];
        if(currentT<minT):
            minT_index=i
            minT=currentT
        if(currentC<minC):
            minC_index=i
            minC=currentC
        if(currentQ>maxQ):
            maxQ_index=i
            maxQ=currentQ
    return minT_index,minC_index,maxQ_index