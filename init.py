# coding=utf-8
from function import *

excel1 = 'z_last_data.xls'
excel2 = 'zDHEW_data.xls'
excel3 = 'zhiliangquanzhong.xls'
# Tn正常工期Lcn工人预计花费Lq工人工作质量Mc材料花费Mq材料质量Ac设备花费Aq设备质量
Tn, Lcn, Lqmin, Mcmin, Mqmin, Acmin, Aqmin, Ecmin, Eqmin, Epmin, Lqmax, Mcmax, Mqmax, Acmax, Aqmax, Ecmax, Eqmax, Epmax, allinfo = gainData(excel1)
DHEws = gainDHEw(excel2)
QWTi, LWTi, MWTi, AWTi = gainData2(excel3)  # 质量权重信息，分别是工序，工人，材料，管理
count = len(allinfo)  # 总的工序数
allP = [];
TcInfo = [];
Lcc = [];
Tc = [];
Qcsum = 0;
Tcsum = 0;
Ccsum = 0;
Cnsum = 0
for i in range(0, len(DHEws)):
    p = gainP(DHEws[i])
    allP.append(p)
for i in range(0, count):
    minTcInfo = min_Tc(allinfo[i][3], DHEws, Epmax[i])  # 第一个数是取第几个D，H取到的Tc,第二个数是Tc的值,第三个是取到这个Tc时每周的,第四个是相应的D H  Ew
    TcInfo.append(minTcInfo)
    Tc.append(minTcInfo[1])
insertAllP(excel2, allP)
insertAllTc(excel1, TcInfo)
for i in range(0, count):
    Lcci = gainCc(TcInfo[i][2], Lcn[i], allP[TcInfo[i][0]])
    Lcc.append(Lcci)
