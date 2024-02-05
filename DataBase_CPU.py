# -*- coding: utf-8 -*-
class DB_CPU():
 import time
 c1 = None
 c1 ='12'
 def reset():#더미데이터
  keyword = None
  parttype = None
  find = None
  f = None
  return keyword,find,f,parttype
 while (c1 == '12'):
  keyword = None
  find = None
  f = None
  keyword = input('\033[0m'+'Enter the desired part...\n')
  find = keyword
  f = keyword = find
  if f == 'back':
   from Start import close
  if f == 'A35900H' or f == 'A3 5900H' or f == 'a3 5900h' or f == 'a35900h':
   print('\033[46m'+'A3 5900H\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:470w\nCore:32\nVirtualization Core:128\nThread:64\nBase Clock:164000MHz\nBost Clock:281000MHz\nSocket:HC4\nMaxium Temperature:125℃\nAOB:true\nInnards Graphics:Graphics 890\nRelease:Apr 14.2023'+'\033[0m')
   time.sleep(2)
   continue
  #                                 Jan _ 1월
  #                                 Feb _ 2월
  #                                 Mar _ 3월
  #                                 Apr _ 4월
  #                                 May _ 5월
  #                                 Jun _ 6월
  #                                 Jul _ 7월
  #                                 Aug _ 8월
  #                                 Sep _ 9월
  #                                 Oct _ 10월
  #                                 Nov _ 11월
  #                                 Dec _ 12월
  if f == 'A3 5100' or f=='a35100' or f=='a3 5100' or f=='A35100':#24년 1월 기준 5000번대 가장 하위 제품
   print('\033[46m'+'A3 5100\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:90w\nCore:16\nVirtualization Core:48\nThread:32\nBase Clock:50000MHz\nBost Clock:100000MHz\nSocket:HC4\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 860\nRelease:Jan 27.2024'+'\033[0m')
   continue 
  if f == 'A34750' or f == 'a34750' or f == 'a3 4750' or f == 'A3 4750': #A3 4700H 23년 12월 리프래시 버전
   print('\033[46m'+'A3 4750\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr')
   print('TDP:270w\nCore:30\nVirtualization Core:16\nThread:60\nBase Clock:120000MHz\nBost Clock:140000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:true')
   print('Innards Graphics:Graphics 880\nRelease:Dec 30.2023'+'\033[0m')
   continue
  if f == 'A35950H' or f == 'A3 5950H' or f == 'a35950h' or f == 'a3 5950h':
   print('\033[46m'+'A3 5950H\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:500w\nCore:48\nVirtualization Core:128\nThread:96\nBase Clock:220000MHz\nBost Clock:300000MHz\nSocket:HC4\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 890\nRelease:Sep 5.2023'+'\033[0m')
   continue 
  if f == 'A35900' or f == 'A3 5900' or f == 'a3 5900' or f == 'a35900':
   print('\033[46m'+'A3 5900\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:340w\nCore:28\nVirtualization Core:86\nThread:56\nBase Clock:148800MHz\nBost Clock:250000MHz\nSocket:HC4\nMaxium Temperature:120℃\nAOB:true\nInnards Graphics:Graphics 890\nRelease:Apr 10.2023'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'A35900C' or f == 'A3 5900C' or f == 'a3 5900c' or f == 'a35900c':
   print('\033[46m'+'A3 5900C\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:300w\nCore:28\nVirtualization Core:86\nThread:56\nBase Clock:82000MHz\nBost Clock:199000MHz\nSocket:HC4\nMaxium Temperature:95℃\nAOB:true\nInnards Graphics:Graphics 890\nRelease:Apr 14.2023'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'A35700' or f == 'A3 5700' or f == 'a3 5700' or f == 'a35700':
   print('\033[46m'+'A3 5700\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:285w\nCore:28\nVirtualization Core:86\nThread:56\nBase Clock:85000MHz\nBost Clock:200000MHz\nSocket:HC4\nMaxium Temperature:100℃\nAOB:true\nInnards Graphics:Graphics 880\nRelease:Apr 10.2023'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'A3 5200C' or f== 'a3 5200c' or f== 'a3 5200C' or f=='a35200c' or f=='A35200C':
   print('\033[46m'+'A3 5200C\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:120w\nCore:18\nVirtualization Core:52\nThread:36\nBase Clock:55000MHz\nBost Clock:118000MHz\nSocket:HC4\nMaxium Temperature:100℃\nAOB:true\nInnards Graphics:Graphics 860\nRelease:Apr 10.2023'+'\033[0m')
   time.sleep(2)
   continue 
  if f == 'A35200' or f == 'A3 5200' or f == 'a3 5200' or f == 'a35200':
   print('\033[46m'+'A3 5200\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:150w\nCore:20\nVirtualization Core:54\nThread:40\nBase Clock:59000MHz\nBost Clock:123000MHz\nSocket:HC4\nMaxium Temperature:100℃\nAOB:true\nInnards Graphics:Graphics 860\nRelease:Apr 10.2023'+'\033[0m')
   time.sleep(2)
   continue 
  if f == 'A35200H' or f == 'A3 5200H' or f == 'a3 5200h' or f == 'a35200h':
   print('\033[46m'+'A3 5200H\nType:CPU\nBase:K64\nSeries:A3 5000\nSupport Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3\nTDP:220w\nCore:24\nVirtualization Core:72\nThread:48\nBase Clock:77000MHz\nBost Clock:125700MHz\nSocket:HC4\nMaxium Temperature:125℃\nAOB:true\nInnards Graphics:Graphics 870\nRelease:Apr 14.2023'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'A34900H' or f == 'A3 4900H' or f == 'a3 4900h' or f == 'a34900h':
   print('\033[46m'+'A3 4900H\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:380w\nCore:30\nVirtualization Core:12\nThread:60\nBase Clock:112000MHz\nBost Clock:130000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:true\nInnards Graphics:Graphics 790\nRelease:Oct 19.2022'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'A34900' or f == 'A3 4900' or f == 'a3 4900' or  f == 'a34900':
   print('\033[46m'+'A3 4900\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:300w\nCore:28\nVirtualization Core:8\nThread:56\nBase Clock:92300MHz\nBost Clock:100000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:true\nInnards Graphics:Graphics 780\nRelease:Aug 1.2022'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'A34700C' or f == 'A3 4700C' or f == 'a3 4700c' or f == 'a34700c':
    print('\033[46m'+'A3 4700C\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:190w\nCore:16\nVirtualization Core:8\nThread:32\nBase Clock:73000MHz\nBost Clock:99000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:true\nInnards Graphics:Graphics 780\nRelease:Oct 19.2022'+'\033[0m')
    time.sleep(2)
    continue
  if f == 'A34700' or f ==  'A3 4700' or f == 'a3 4700' or f =='a34700':
    print('\033[46m'+'A3 4700\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:240w\nCore:20\nVirtualization Core:8\nThread:40\nBase Clock:81000MHz\nBost Clock:99000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:true\nInnards Graphics:Graphics 780\nRelease:Aug 1.2022'+'\033[0m')
    time.sleep(2)
    continue
  if f == 'A34700H' or f == 'A3 4700H' or f == 'a3 4700h' or  f == 'a34700h':
    print('\033[46m'+'A3 4700H\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:270w\nCore:28\nVirtualization Core:8\nThread:56\nBase Clock:86100MHz\nBost Clock:99000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:true\nInnards Graphics:Graphics 780\nRelease:Oct 19.2022'+'\033[0m')
    time.sleep(2)
    continue
  if f == 'A34700CL' or f == 'A3 4700CL' or f == 'a3 4700cl' or f == 'a34700cl':
    print('\033[46m'+'A3 4700CL\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr,LTCC\nTDP:50w\nCore:16\nThread:32\nBase Clock:12000MHz\nBost Clock:16600MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:fales\nInnards Graphics:Graphics 780\nRelease:Set 15.2022'+'\033[0m')
    time.sleep(2)
    continue
  if f == 'A34500' or f == 'A3 4500' or f == 'a3 4500' or f == 'a34500':
    print('\033[46m'+'A3 4500\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:230w0w\nCore:12\nVirtualization Core:4\nThread:24\nBase Clock:59910MHz\nBost Clock:88000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:true\nInnards Graphics:Graphics 770\nRelease:Aug 1.2022'+'\033[0m')
    time.sleep(2)
    continue
  if f == 'A34500L' or f == 'A3 4500L' or f == 'a3 4500l' or f == 'a34500l':
    print('\033[46m'+'A3 4500L\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:45w\nCore:12\nVirtualization Core:4\nThread:24\nBase Clock:10050MHz\nBost Clock:11500MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:true\nInnards Graphics:Graphics 770\nRelease:Aug 1.2022'+'\033[0m')
    continue
  if f == 'A34500C' or f == 'A3 4500C' or f == 'a3 4500c' or f == 'a34500c':
    print('\033[46m'+'A3 4500C\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:200w\nCore:12\nVirtualization Core:2\nThread:24\nBase Clock:53010MHz\nBost Clock:70000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:true\nInnards Graphics:Graphics 770\nRelease:Aug 1.2022'+'\033[0m')
    continue
  if f == 'A34500CL' or f == 'A3 4500CL' or f == 'a3 4500cl' or f == 'a34500cl':
    print('\033[46m'+'A3 4500CL\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:55w\nCore:10\nVirtualization Core:2\nThread:20\nBase Clock:9910MHz\nBost Clock:10000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 770\nRelease:Aug 1.2022'+'\033[0m')
    continue
  if f == 'A34200' or f == 'A3 4200' or f == 'a3 4200' or f == 'a34200':
   print('\033[46m'+'A3 4200\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:150w\nCore:6\nVirtualization Core:1\nThread:12\nBase Clock:39010MHz\nBost Clock:41000MHz\nSocket:HC3\nMaxium Temperature:100℃\nAOB:fales\nInnards Graphics:Graphics 760\nRelease:Aug 1.2022'+'\033[0m')
   continue
  if f == 'A34200FE' or f == 'A3 4200FE' or f == 'a3 4200fe' or f == 'a34200fe':
   print('\033[46m'+'A3 4200FE\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:120w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:32000MHz\nBost Clock:39000MHz\nSocket:HC3\nMaxium Temperature:100℃\nAOB:fales\nInnards Graphics:Graphics 750\nRelease:Aug 3.2022'+'\033[0m')
   continue
  if f == 'A34200CoreDuo' or f == 'A3 4200 Core Duo' or f == 'A34200COREDUO' or f == 'A3 4200 core duo' or f == 'a34200coreduo' or f == 'a34200 coreduo' or f == 'a3 4200 core duo' or f == 'a3 4200core duo' or f == 'a3 4200coreduo':
   print('\033[46m'+'A3 4200 Core Duo\nType:CPU\nBase:K64\nSeries:A3 4000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:50w\nCore:2\nVirtualization Core:None\nThread:4\nBase Clock:11000MHz\nBost Clock:20000MHz\nSocket:HC3\nMaxium Temperature:100℃\nAOB:fales\nInnards Graphics:Graphics 760\nRelease:Aug 3.2022'+'\033[0m')
   continue
  if f == 'A2 3900H' or f == 'A23900H' or f == 'a23900h' or f == 'a2 3900h':
   print('\033[46m'+'A2 3900H\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,OTC,PTMD,AMD+,Lans+,ALans+,32bitAr,16bitAr\nTDP:150w\nCore:20\nVirtualization Core:None\nThread:40\nBase Clock:46000MHz\nBost Clock:68000MHz\nSocket:HC3\nMaxium Temperature:100℃\nAOB:fales\nInnards Graphics:Graphics 690\nRelease:Jan 12.2021'+'\033[0m')
   continue
  if f == 'A2 3900' or f == 'A23900' or f == 'a2 3900' or f == 'a23900':
   print('\033[46m'+'A2 3900\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:120w\nCore:18\nVirtualization Core:None\nThread:36\nBase Clock:41300MHz\nBost Clock:50000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 690\nRelease:Jan 12.2022'+'\033[0m')
   continue
  if f == 'A2 3900L' or f == 'A23900L' or f == 'a2 3900l' or f == 'a23900l':
   print('\033[46m'+'A2 3900L\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:60w\nCore:18\nVirtualization Core:None\nThread:36\nBase Clock:8300MHz\nBost Clock:10000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:fales\nInnards Graphics:Graphics 690\nRelease:Jan 28.2022'+'\033[0m')
   continue
  if f == 'A2 3700' or f == 'A23700' or f == 'a2 3700' or f == 'a23700':
   print('\033[46m'+'A2 3700\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:90w\nCore:16\nVirtualization Core:None\nThread:32\nBase Clock:39100MHz\nBost Clock:47000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 680\nRelease:Jan 12.2022'+'\033[0m')
   continue
  if f == 'A2 3700H' or f == 'A23700H' or f == 'a2 3700h' or f == 'a2 3700h' or f == 'A2 3700h' or f == 'a2 3700H':
   print('\033[46m'+'A2 3700H\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:100w\nCore:16\nVirtualization Core:None\nThread:32\nBase Clock:40000MHz\nBost Clock:47950MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 680\nRelease:Jan 12.2022'+'\033[0m')
   continue
  if f == 'A2 3700L' or f == 'A23700L' or f == 'a2 3700l' or f == 'a23700l':
   print('\033[46m'+'A2 3700L\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:120w\nCore:16\nVirtualization Core:None\nThread:32\nBase Clock:7000MHz\nBost Clock:9200MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:fales\nInnards Graphics:Graphics 680\nRelease:Jan 28.2022'+'\033[0m')
   continue
  if f == 'A2 3500' or f == 'A23500' or f == 'a23500' or f == 'a2 3500':
   print('\033[46m'+'A2 3500\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:100w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:29700MHz\nBost Clock:35000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 670\nRelease:Jan 12.2022'+'\033[0m')
   continue
  if f == 'A2 3500FE' or f == 'A23500FE' or f == 'a23500fe' or f == 'a2 3500fe' or f == 'A23500fe':
   print('\033[46m'+'A2 3500FE\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:90w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:29500MHz\nBost Clock:35000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 670\nRelease:Apr 1.2022'+'\033[0m')
   continue
  if f == 'A2 3500L' or f == 'A23500L' or f == 'a23500l' or f =='a2 3500l':
   print('\033[46m'+'A2 3500L\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:45w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:5500MHz\nBost Clock:6000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:fales\nInnards Graphics:Graphics 670\nRelease:Jan 28.2022'+'\033[0m')#\nInnards Graphics:Graphics 670
   continue
  if f == 'A2 3200' or f == 'A23200' or f == 'a23200' or f == 'a2 3200':
   print('\033[46m'+'A2 3200\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:65w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:23000MHz\nBost Clock:27000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 660\nRelease:Ape 1.2022'+'\033[0m')
   continue
  if f == 'A2 3200L' or f == 'A23200L' or f == 'a23200l' or f == 'a2 3200l' or find == 'a2 3200L':
    print('\033[46m'+'A2 3200L\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:40w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:4900MHz\nBost Clock:5000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:fales\nInnards Graphics:Graphics 660\nRelease:Jan 28.2022'+'\033[0m')#\nInnards Graphics:Graphics 660
    continue
  if f == 'A2 3200FE' or f == 'A23200FE' or f == 'a23200fe' or f == 'a2 3200fe' or f == 'A2 3200fe' or find == 'a2 3200FE':
    print('\033[46m'+'A2 3200FE\nType:CPU\nBase:K64\nSeries:A2 3000\nSupport Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr\nTDP:60w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:21400MHz\nBost Clock:26800MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 650\nRelease:Apr 1.2022'+'\033[0m')#\nInnards Graphics:Graphics 650
    continue
  if f == 'A2 2900' or f == 'A22900' or f == 'a22900' or f == 'a2 2900':
    print('\033[46m'+'A2 2900\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
    print('TDP:150w\nCore:16\nVirtualization Core:None\nThread:32\nBase Clock:12600MHz\nBost Clock:20000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 590\nRelease:Dec 16.2019'+'\033[0m')#\nInnards Graphics:Graphics 590
    continue
  if find == 'a2    2700' or f == 'A2 2700' or f == 'A22700' or f == 'a22700' or f == 'a2 2700':
    print('\033[46m'+'A2 2700\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
    print('TDP:125w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:11000MHz\nBost Clock:18400MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 580\nRelease:Dec 16.2019'+'\033[0m')#\nInnards Graphics:Graphics 580
    continue
  if f == 'A2 2750L' or find == 'A22750L' or f == 'a22750l' or f == 'a2 2750l':
    print('\033[46m'+'A2 2750L\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
    print('TDP:80w\nCore:18\nVirtualization Core:None\nThread:20\nBase Clock:3800MHz\nBost Clock:5500MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales\nInnards Graphics:Graphics 590\nRelease:Jan 29.2020'+'\033[0m')#\nInnards Graphics:Graphics 590
    continue
  if f == 'A2 2550L' or f == 'A22550L' or f == 'a22550l' or f == 'a2 2550l':
   print('\033[46m'+'A2 2550L\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:70w\nCore:14\nVirtualization Core:None\nThread:18\nBase Clock:3400MHz\nBost Clock:4000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 580\nRelease:Jan 29.2020'+'\033[0m')#Innards Graphics:Graphics 580
   continue
  if f == 'A2 2500' or f == 'A22500' or f =='a22500' or f == 'a2 2500':
   print('\033[46m'+'A2 2500\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:100w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:8900MHz\nBost Clock:13700MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 570\nRelease:Dec 16.2019'+'\033[0m')#Innards Graphics:Graphics 570
   continue
  if f == 'A2 2305NG' or f == 'a2 2305ng' or f == 'A22305NG' or f == 'a22305ng':
   print('\033[46m'+'A2 2305NG\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:70w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:6100MHz\nBost Clock:8000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:None\nRelease:Mar 9.2020'+'\033[0m')
   continue
  if f == 'A2 2305' or f == 'a2 2305' or f == 'a22305' or f == 'a2 2305':
   print('\033[46m'+'A2 2305\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:75w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:6100MHz\nBost Clock:8000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 560\nRelease:Mar 9.2020'+'\033[0m')
   continue
  if f == 'A2 2200' or f == 'a2 2200' or f == 'A22000' or f == 'a22000':
   print('\033[46m'+'A2 2200\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:55w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:5200MHz\nBost Clock:7700MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 550\nRelease:Dec 16.2019'+'\033[0m')
   continue
  if f == 'A2 2200X' or f == 'A22200X' or f == 'a2 2200x' or f == 'a22200x' or f == 'a2200X':
   print('\033[46m'+'A2 2200X\nType:CPU\nBase:K64\nSeries:A2 2000\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:70w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:6000MHz\nBost Clock:7900MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 550\nRelease:Dec 22.2019'+'\033[0m')
   continue
  if f == 'A1 1900' or f == 'A11900' or f == 'a1 1900' or f == 'a11900':
   print('\033[46m'+'A1 1900\nType:CPU\nBase:K64\nSeries:A2\1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:110w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:8000MHz\nBost Clock:10200MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 490\nRelease:May 3.2018'+'\033[0m')
   continue
  if f == 'A1 1800' or f == 'A11800' or f == 'a1 1800' or f == 'a11800':
   print('\033[46m'+'A1 1800\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:90w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:7500MHz\nBost Clock:9900MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 490\nRelease:May 3.2018'+'\033[0m')
   continue
  if f == 'A1 1750L' or f == 'A11750L' or f == 'a1 1750l' or f == 'a11750l':
   print('\033[46m'+'A1 1750L\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:50w\nCore:10\nVirtualization Core:None\nThread:20\nBase Clock:2100MHz\nBost Clock:2300MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 480\nRelease:Jul 1.2018'+'\033[0m')
   continue
  if f == 'A1 1750T' or f == 'A11750T' or f == 'a1 1750t' or f == 'a11750t':
   print('\033[46m'+'A1 1750T\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:75w\nCore:10\nVirtualization Core:None\nThread:20\nBase Clock:6900MHz\nBost Clock:7800MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 470\nRelease:May 3.2018'+'\033[0m')
   continue
  if f == 'A1 1500' or f == 'A11500' or f == 'a1 1500' or f == 'a11500':
   print('\033[46m'+'A1 1500\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:60w\nCore:10\nVirtualization Core:None\nThread:20\nBase Clock:5500MHz\nBost Clock:6300MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 460\nRelease:May 3.2018'+'\033[0m')
   continue
  if f == 'A1 1300' or f == 'A11300' or f == 'a1 1300' or f == 'a11300':
   print('\033[46m'+'A1 1300\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:55w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:5200MHz\nBost Clock:6000MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 460\nRelease:May 3.2018'+'\033[0m')
   continue
  if f == 'A1 1200L' or f == 'A11200L' or f == 'a1 1200l' or f == 'a11200l':
   print('\033[46m'+'A1 1200\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:30w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:1700MHz\nBost Clock:2000MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 460\nRelease:Jul 1.2018'+'\033[0m')
   continue
  if f == 'A1 1000' or f == 'A11000' or f == 'a1 1000' or f == 'a11000':
   print('\033[46m'+'A1 1000\nType:CPU\nBase:K64\nSeries:A1 1000\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:45w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:4900MHz\nBost Clock:5500MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 460\nRelease:May 3.2018'+'\033[0m')
   continue
  if f == 'A1 900' or f == 'A1900' or f == 'a1 900' or f == 'a1900':
   print('\033[46m'+'A1 900\nType:CPU\nBase:K64\nSeries:A1 100\nSupport Command:HTCA1,NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:70w\nCore:12\nVirtualization Core:None\nThread:24\nBase Clock:3000MHz\nBost Clock:3300MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 350\nRelease:Fed 20.2018'+'\033[0m')#Graphics 350 고정
   continue
  if f == 'A1 700' or f == 'A1700' or f == 'a1 700' or f == 'a1700':
   print('\033[46m'+'A1 700\nType:CPU\nBase:K64\nSeries:A1 100\nSupport Command:HTCA1,NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:60w\nCore:10\nVirtualization Core:None\nThread:20\nBase Clock:3000MHz\nBost Clock:3000MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 350\nRelease:Fed 20.2018'+'\033[0m')
   continue
  if f == 'A1 500' or f == 'A1500' or f == 'a1 500' or f == 'a1500':
   print('\033[46m'+'A1 500\nType:CPU\nBase:K64\nSeries:A1 100\nSupport Command:HTCA1,NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:55w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:2700MHz\nBost Clock:2700MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 350\nRelease:Fed 20.2018'+'\033[0m')
   continue
  if f == 'A1 300' or f == 'A1300' or f == 'a1 300' or f == 'a1300':
   print('\033[46m'+'A1 300\nType:CPU\nBase:K64\nSeries:A1 100\nSupport Command:HTCA1,NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:40w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:2300MHz\nBost Clock:2300MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 350\nRelease:Fed 20.2018'+'\033[0m')
   continue
  if f == 'A1 CFV100' or f == 'A1CFV100' or f == 'a1 cfv100' or f == 'a1cfv100' or f == 'A1 cfv100' or f == 'ㅁ1 ㅊㄿ100' or f == 'a1 CFV100':
   print('\033[46m'+'A1 CFV100\nType:CPU\nBase:K64\nSeries:A1 100\nSupport Command:HTCA1,NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,32bitAr,16bitAr,8bitAr')
   print('TDP:35w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:1900MHz\nBost Clock:2100MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 290\nRelease:Fed 2.2018'+'\033[0m')#TEST_MODEL
   continue
  if f == 'Fastcoll 1-Core Single' or f == 'fastcoll 1-core single' or f == 'fastcoll1-coresingle' or f == 'fastcoll1coresingle':#32Bit Base CPU
   print('\033[46m'+'Fastcoll 1-Core Single\nType:CPU\nBase:K32\nSeries:Fastcoll 1\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr')
   print('TDP:30w\nCore:1\nVirtualization Core:None\nThread:2\nBase Clock:1200MHz\nBost Clock:1600MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Apr 5.2016'+'\033[0m')
   continue
  if f == 'Fastcoll 1-Core Duo' or f == 'fastcoll 1-core duo' or f == 'fastcoll1-coreduo' or f == 'fastcoll1coreduo':
   print('\033[46m'+'Fastcoll 1-Core Duo\nType:CPU\nBase:K32\nSeries:Fastcoll 1\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr')
   print('TDP:55w\nCore:2\nVirtualization Core:None\nThread:4\nBase Clock:1440MHz\nBost Clock:1790MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Apr 5.2016'+'\033[0m')
   continue
  if f == 'Fastcoll 2-Core Single' or f == 'fastcoll 2-core single' or f == 'fastcoll2-coresingle' or f == 'fastcoll2coresingle':
   print('\033[46m'+'Fastcoll 2-Core Single\nType:CPU\nBase:K32\nSeries:Fastcoll 2\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr')
   print('TDP:40w\nCore:1\nVirtualization Core:None\nThread:2\nBase Clock:1350MHz\nBost Clock:1680MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Sep 30.2017'+'\033[0m')
   continue
  if f == 'Fastcoll 2-Core Duo' or f == 'fastcoll 2-core duo' or f == 'fastcoll2-coreduo' or f == 'fastcoll2coreduo':
   print('\033[46m'+'Fastcoll 2-Core Duo\nType:CPU\nBase:K32\nSeries:Fastcoll 2\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr')
   print('TDP:65w\nCore:2\nVirtualization Core:None\nThread:4\nBase Clock:1500MHz\nBost Clock:1730MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Sep 30.2017'+'\033[0m')
   continue
  if f == 'Fastcoll 2-Core X' or f == 'fastcoll 2-core x' or f == 'fastcoll2-corex' or f == 'fastcoll2corex':
   print('\033[46m'+'Fastcoll 2-Core X\nType:CPU\nBase:K32\nSeries:Fastcoll 2\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr')
   print('TDP:80w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:1900MHz\nBost Clock:2290MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 290\nRelease:Nov 5.2017'+'\033[0m')
   continue
  if f == 'Ion 100' or f == 'ion 100' or f == 'Ion100' or f == 'ion100' or f == 'ION100' or find == 'ㅑㅒㅜ!))':
   print('\033[46m'+'Ion 100\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:35w\nCore:1\nVirtualization Core:None\nThread:2\nBase Clock:1265MHz\nBost Clock:1300MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 250\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 100S' or f == 'ion 100s' or f == 'Ion100S' or f == 'ion100s' or f == 'ion100S':
   print('\033[46m'+'Ion 100S\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:40w\nCore:1\nVirtualization Core:None\nThread:2\nBase Clock:1300MHz\nBost Clock:1420MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 250\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 200' or f == 'ion 200' or f == 'Ion200' or f == 'ion200' or f == 'ion100   ':
   print('\033[46m'+'Ion 200\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:50w\nCore:2\nVirtualization Core:None\nThread:4\nBase Clock:1370MHz\nBost Clock:1490MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 260\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 200S' or f == 'ion 200s' or f == 'Ion200S' or f == 'ion200s' or f == 'ion200S':
   print('\033[46m'+'Ion 200S\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:55w\nCore:2\nVirtualization Core:None\nThread:4\nBase Clock:1410MHz\nBost Clock:1500MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 260\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 300' or f == 'ion 300' or f == 'Ion300' or f == 'ion300' or f == 'ION300':
   print('\033[46m'+'Ion 300\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:60w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:1490MHz\nBost Clock:1600MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 300S' or f == 'ion 300s' or f == 'Ion300s' or f == 'ion300s' or f == 'ION300S':
   print('\033[46m'+'Ion 300S\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:65w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:1500MHz\nBost Clock:1630MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 260\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion300L' or f == 'ion 300l' or f == 'Ion300L' or f == 'ION300L' or f == 'ion300l' or f == 'ION300l' or f == 'ion 300L' or f == 'ION 300L':
   print('\033[46m'+'Ion 300L\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:30w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:1100MHz\nBost Clock:1130MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Dec 15.2016'+'\033[0m')
   continue
  if f == 'ion300fe' or f == 'Ion 300FE' or f == 'Ion300FE' or f == 'Ion300fe' or f == 'ion300Fe' or f == 'ION300FE':
   print('\033[46m'+'Ion 300FE\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:50w\nCore:4\nVirtualization Core:None\nThread:8\nBase Clock:1390MHz\nBost Clock:1580MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 250\nRelease:Dec 15.2016'+'\033[0m')
   continue
  if f == 'Ion 400' or f == 'ion400' or f == 'Ion400' or f == 'ION400' or f == 'ion 400':
   print('\033[46m'+'Ion 400\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:85w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:1600MHz\nBost Clock:1750MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 280\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 400S' or f == 'ion400s' or f == 'Ion400S' or f == 'ion400에스' or f == 'ION400S' or f == 'Ion 400S':
   print('\033[46m'+'Ion 400S\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr,ECCC')
   print('TDP:90w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:1650MHz\nBost Clock:1790MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 270\nRelease:Mar 2.2016'+'\033[0m')
   continue
  if f == 'Ion 400FE' or f == 'ion400fe' or f == 'ion 400fe' or f == 'Ion400fe' or f == 'Ion400FE' or f == '아이온사공공에프이' or f == 'ION400FE':
   print('\033[46m'+'Ion 400FE\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:75w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:1500MHz\nBost Clock:1650MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 250\nRelease:Dec 15.2016'+'\033[0m')
   continue
  if f == 'Ion 400L' or f == 'ion400l' or f == 'ION 400L' or f == 'Ion400L' or f == 'ion400L' or f == 'ㅑㅒㅜ $))ㅣ' or f == 'ion 400L':
   print('\033[46m'+'Ion 400L\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:45w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:1300MHz\nBost Clock:1520MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 280\nRelease:Dec 15.2016'+'\033[0m')
   continue
  if f == 'Ion 477L' or f == 'ion 477l' or f == 'ION 477L' or f == 'ion477l' or f == 'ion477 l' or f == 'Ion477L' or f == 'ION477L':
   print('\033[46m'+'Ion 477L\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:60w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:1410MHz\nBost Clock:1500MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 290\nRelease:Jan 1.2017'+'\033[0m')
   continue
  if find == 'Ion 499' or f == 'ion499' or f == 'ION499' or f == 'ion 499' or f == 'Iom499':
   print('\033[46m'+'Ion 499\nType:CPU\nBase:K32\nSeries:Ion\nSupport Command:NKPCCPL,HCC,ORO1,ORO2,ORG,OROS,OTC,PTMD,16bitAr,8bitAr,ABitAr')
   print('TDP:110w\nCore:8\nVirtualization Core:None\nThread:16\nBase Clock:1780MHz\nBost Clock:1900MHz\nSocket:HC2\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 290\nRelease:Jan 1.2017'+'\033[0m')
   continue
  if f == 'Sky 1000' or f == 'sky 1000' or f == 'sky1000' or f == 'Sky1000' or f == 'SKY 1000':#Sky CPU,'H.O.S 최초의 소비자용 CPU'
   print('\033[46m'+'Sky 1000\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenNKC,OpenProject-ZERO,OpenProject-Metal')
   print('TDP:40w\nCore:2\nVirtualization Core:None\nThread:2\nBase Clock:700MHz\nBost Clock:1000MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 150\nRelease:Jun 1.2014'+'\033[0m')
   time.sleep(0.5)
   easteregger_sky = input('')
   if easteregger_sky == 'Sky' or easteregger_sky == '하늘' or easteregger_sky == 'SKY' or easteregger_sky == 'sky' or easteregger_sky == 'ㅎㄴ' or easteregger_sky == '나ㅛ' or easteregger_sky == 'てん' or easteregger_sky == '天' or easteregger_sky == 'mimétisme' or easteregger_sky == 'mouvement ondulant' or easteregger_sky == 'cielo' or easteregger_sky == 'der Himme' or easteregger_sky == 'das Paradies' or easteregger_sky == 'das Himmelreich' or easteregger_sky == ' trời' or easteregger_sky == 'bầu trời' or easteregger_sky == 'небо':
    print('\033[104m'+'푸른 하늘 우리의 하늘 그리고,연산의 끝없는 하늘The blue sky, our sky, and the endless sky of Yeonsan青い空、私たちの空、延山の果てしない空蔚蓝的天空,我们的天空,连绵不断的燕山天空El cielo azul, nuestro cielo y el cielo infinito de YeonsanLe ciel bleu, notre ciel, et le ciel sans fin de YeonguanDer blaue Himmel, unser Himmel und der endlose Himmel von YeonsanГолубое небо, наше небо и бесконечное небо Йонсанаท้องฟ้าสีฟ้า ท้องฟ้าของเรา และท้องฟ้าที่ไม่มีที่สิ้นสุดของยอนซานBầu trời xanh, bầu trời của chúng ta, và bầu trời bất tận của YeonsanIl cielo blu, il cielo e il cielo infinito di YeonsanO céu azul, o nosso céu, e o céu infinito de Yeonsanनीला आकाश, हमारा आकाश, और योनसन का अंतहीन आकाशLangit biru, langit kita, dan langit Yeonsan yang tak berujung'+'\033[0m')
    continue
   time.sleep(3)
   continue
  if f == 'Sky 1200' or f == 'sky1200' or f == 'SKY1200' or f == 'sky 1200' or f == 'SKY 1200' or f == 'Sky1200' or f == 'SKy1200':
   print('\033[46m'+'Sky 1200\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenNKC,OpenProject-ZERO,OpenProject-Metal')
   print('TDP:80w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:860MHz\nBost Clock:1200MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 150\nRelease:Jun 1.2014'+'\033[0m')
   continue 
  if f == 'Sky 1200X' or f == 'sky1200x' or f == 'SKY1200X' or f == 'sky 1200x' or f == 'sky1200':
   print('\033[46m'+'Sky 1200X\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenNKC,OpenProject-ZERO,OpenProject-Metal')
   print('TDP:90w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:920MHz\nBost Clock:1300MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 160\nRelease:Feb 5.2014'+'\033[0m')
   continue 
  if f == 'Sky 1400' or f == 'sky1400' or f == 'SKY1400' or f == 'sky 1400':
   print('\033[46m'+'Sky 1400\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenNKC,OpenProject-ZERO,OpenProject-Metal')
   print('TDP:120w\nCore:6\nVirtualization Core:None\nThread:6\nBase Clock:1000MHz\nBost Clock:1400MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 160\nRelease:Jun 1.2014'+'\033[0m')
   continue 
  if f == 'Sky 1400X' or f == 'sky1400x' or f == 'SKY1400X' or f == 'sky 1400x' or f == 'Sky1400x':
   print('\033[46m'+'Sky 1400X\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenNKC,OpenProject-ZERO,OpenProject-Metal')
   print('TDP:125w\nCore:6\nVirtualization Core:None\nThread:6\nBase Clock:1100MHz\nBost Clock:1470MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 170\nRelease:Feb 5.2014'+'\033[0m')
   continue 
  if f == 'Sky 1400L' or f == 'sky1400l' or f == 'SKY1400L' or f == 'sky 1400l' or f == 'Sky1400l':
   print('\033[46m'+'Sky 1400LX\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenNKC,OpenProject-ZERO,OpenProject-Metal,LABTOP_SSL')
   print('TDP:30w\nCore:6\nVirtualization Core:None\nThread:6\nBase Clock:590MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 150\nRelease:Feb 28.2014'+'\033[0m')
   continue 
  if f == 'Sky 2000' or f == 'sky2000' or f == 'SKY2000' or f == 'sky 2000' or f == 'Sky2000' or f == 'SKY 2000':
   print('\033[46m'+'Sky 2000\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AlOS')
   print('TDP:60w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:950MHz\nBost Clock:1200MHz\nSocket:HCS\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 180\nRelease:Fed 1.2015'+'\033[0m')
   continue 
  if f == 'Sky 2000X' or f == 'sky2000x' or f == 'SKY2000X' or f == 'sky 2000x' or f == 'Sky2000X' or f == 'SKY 2000X' or f == 'SKY 2000X':
   print('\033[46m'+'Sky 2000X\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AIOS')
   print('TDP:75w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:1000MHz\nBost Clock:1300MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 190\nRelease:Fed 1.2015'+'\033[0m')
   continue 
  if f == 'Sky 2000L' or f == 'sky2000l' or f == 'SKY2000X' or f == 'Sky2000L' or f == 'SKY 2000L' or f == 'sky 2000l':
   print('\033[46m'+'Sky 2000L\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AIOS,LABTOP_SSL')
   print('TDP:40w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:700MHz\nBost Clock:900MHz\nSocket:HCS\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:Graphics 170\nRelease:Fed 1.2015'+'\033[0m')
   continue 
  if f == 'Sky 2000FE' or f == 'sky2000fe' or f == 'SKY2000FE' or f == 'Sky2000fe' or f == 'sky2000FE' or f == 'sky 2000fe':
   print('\033[46m'+'Sky 2000FE\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AIOS')
   print('TDP:50w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:900MHz\nBost Clock:1050MHz\nSocket:HCS\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 180\nRelease:Jun 6.2015'+'\033[0m')
   continue 
  if f == 'Sky 2000C' or f == 'sky2000c' or f == 'SKY2000C' or f == 'Sky2000c' or f == 'sky 2000c' or f == 'SKY 2000C':
   print('\033[46m'+'Sky 2000C\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AIOS')
   print('TDP:90w\nCore:6\nVirtualization Core:None\nThread:6\nBase Clock:950MHz\nBost Clock:1320MHz\nSocket:HCS\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 180\nRelease:Jun 6.2015'+'\033[0m')
   continue 
  if f == 'sky 2000h' or f == 'Sky 2000H' or f == 'SKY2000H' or f == 'sky2000h' or f == 'Sky2000H' or f == '하늘이천뜨거운' or f == 'sky 2000H':
   print('\033[46m'+'Sky 2000H\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AIOS')
   print('TDP:120w\nCore:6\nVirtualization Core:None\nThread:6\nBase Clock:1200MHz\nBost Clock:1400MHz\nSocket:HCS\nMaxium Temperature:120℃\nAOB:fales')
   print('Innards Graphics:Graphics 190\nRelease:Nov 12.2015'+'\033[0m')
   continue 
  if f == 'Sky 2000XEU' or f == 'sky2000xeu' or f == 'sky2000 xeu' or f == 'Sky2000XEU' or f == 'SKY2000XEU' or f == 'sky 2000xeu':
   print('\033[46m'+'Sky 2000XEU\nType:CPU\nBase:K32\nSeries:Sky\nSupport Command:HCC,ORO1,16bitAr,8bitAr,ABitAr')
   print('TDP:30w\nCore:2\nVirtualization Core:None\nThread:4\nBase Clock:1400MHz\nBost Clock:1500MHz\nSocket:HCS\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 250\nRelease:Mar 1.2016'+'\033[0m')#test_model
   continue 
  if f == 'Nano 1' or f == 'nano1' or f == 'NANO1' or f == 'NANO 1' or f == 'nano 1' or f == 'NANO One':#서버용
   print('\033[46m'+'Nano 1\nType:CPU\nBase:K128\nSeries:Nano\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr,AIOS,FQSS')
   print('TDP:140w\nCore:24\nVirtualization Core:None\nThread:48\nBase Clock:2600MHz\nBost Clock:3000MHz\nSocket:AMHC\nMaxium Temperature:90℃\nAOB:fales')
   print('Innards Graphics:None\nRelease:Jun 22.2020'+'\033[0m')
   continue 
  if f == 'Nano 2' or f == 'nano2' or f == 'NANO2' or f == 'nano 2' or f == 'NANO 2' or f == 'Nano2':
   print('\033[46m'+'Nano 2\nType:CPU\nBase:K128\nSeries:Nano\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr,AIOS,FQSS')
   print('TDP:185w\nCore:56\nVirtualization Core:None\nThread:112\nBase Clock:3400MHz\nBost Clock:3700MHz\nSocket:AMHC\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:None\nRelease:Nov 3.2021'+'\033[0m')
   continue
  if f == 'Nano 3' or f == 'nano3' or f == 'NANO3' or f == 'nano 3' or f == 'NANO 3' or f == 'Nano3':
   print('\033[46m'+'Nano 3\nType:CPU\nBase:K128\nSeries:Nano\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,intel+,AMD+,32bitAr,16bitAr,8bitAr,AIOS,FQSS')
   print('TDP:250w\nCore:64\nVirtualization Core:None\nThread:128\nBase Clock:3800MHz\nBost Clock:3000MHz\nSocket:AMHC\nMaxium Temperature:100℃\nAOB:fales')
   print('Innards Graphics:None\nRelease:Dec 10.2022'+'\033[0m')
   continue
  if find == 'Nano 4' or f == 'nano4' or f == 'NANO4' or f == 'nano 4' or f == 'NANO 4' or f == 'Nano4':
   print('\033[46m'+'Nano 4\nType:CPU\nBase:K128\nSeries:Nano\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,intel+,AMD+,32bitAr,16bitAr,8bitAr,AIOS,FQSS')
   print('TDP:275w\nCore:128\nVirtualization Core:24\nThread:256\nBase Clock:4200MHz\nBost Clock:5100MHz\nSocket:AMHC\nMaxium Temperature:110℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jun 19.2023'+'\033[0m')
   continue
  if f == 'Nano 4E' or f == 'nano4e' or f == 'NANO4E' or f == 'Nano4E' or f == 'nano 4e' or f == 'NANO 4E':
   print('\033[46m'+'Nano 4E\nType:CPU\nBase:K128\nSeries:Nano\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,intel+,AMD+,32bitAr,16bitAr,8bitAr,AIOS,FQSS')
   print('TDP:260w\nCore:92\nVirtualization Core:4\nThread:184\nBase Clock:4100MHz\nBost Clock:4900MHz\nSocket:AMHC\nMaxium Temperature:110℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jun 19.2023'+'\033[0m')
   continue
  if f == 'Nano 4S' or f == 'nano4s' or f=='nano 4s' or f=='NANO4S' or f == 'NANO 4S' or f == 'Nano4S':
   print('\033[46m'+'Nano 4S\nType:CPU\nBase:K128\nSeries:Nano\nSupport Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,intel+,AMD+,32bitAr,16bitAr,8bitAr,AIOS,FQSS')
   print('TDP:300w\nCore:138\nVirtualization Core:64\nThread:276\nBase Clock:4500MHz\nBost Clock:5500MHz\nSocket:AMHC\nMaxium Temperature:110℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jun 19.2023'+'\033[0m')
   continue
  if f == 'Automata9 9900' or f == 'automata99900' or f == 'automata9 9900' or f == 'AUTOMATA9 9900' or f == 'AUTOMATA99900' or f == 'Automata99900':
   print('\033[46m'+'Automata9 9900\nType:CPU\nBase:K64\nSeries:Automata')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:320w\nCore:128\nVirtualization Core:256\nThread:256\nBase Clock:191000MHz\nBost Clock:220000MHz\nSocket:AMHC\nMaxium Temperature:140℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jul 3.2023'+'\033[0m')
   continue
  if f == 'Automata9 9700' or f == 'automata9 9700' or f == 'automata99700' or f == 'AUTOMATA99700' or f == 'AUTOMATA9 9700' or f == 'Automata99700':
   print('\033[46m'+'Automata9 9700\nType:CPU\nBase:K64\nSeries:Automata')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:285w\nCore:94\nVirtualization Core:154\nThread:188\nBase Clock:184000MHz\nBost Clock:210000MHz\nSocket:AMHC\nMaxium Temperature:140℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jul 3.2023'+'\033[0m')
   continue
  if f == 'Automata9 9500' or f == 'automata9 9500' or f == 'automata99500' or f == 'AUTOMATA99700' or f == 'AUTOMATA9 9700' or f == 'Automata99500':
   print('\033[46m'+'Automata9 9500\nType:CPU\nBase:K64\nSeries:Automata')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:180w\nCore:64\nVirtualization Core:128\nThread:128\nBase Clock:179000MHz\nBost Clock:208000MHz\nSocket:AMHC\nMaxium Temperature:140℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jul 3.2023'+'\033[0m')
   continue
  if find == 'Automata9 9900X' or f == 'automata9 9900x' or f == 'automata99900x' or f == 'Automata99900X' or f == 'AUTOMATA9 9900X' or f == 'AUTOMATA99900X':
   print('\033[46m'+'Automata9 9900X\nType:CPU\nBase:K64\nSeries:Automata')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:360w\nCore:136\nVirtualization Core:270\nThread:272\nBase Clock:192000MHz\nBost Clock:226000MHz\nSocket:AMHC\nMaxium Temperature:140℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jul 3.2023'+'\033[0m')
   continue
  if f == 'A3 4700S' or f == 'A34700S' or f == 'a34700s' or f == 'a3 4700s' or f == 'A3 4700s' or f == 'a3 4700S':
   print('\033[46m'+'A3 4700S\nType:CPU\nBase:K64\nSeries:A3 4000')
   print('Support Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr')
   print('TDP:300w\nCore:24\nVirtualization Core:64\nThread:48\nBase Clock:120000MHz\nBost Clock:183000MHz\nSocket:HC3\nMaxium Temperature:90℃\nAOB:true')
   print('Innards Graphics:Graphics 880\nRelease:Jul 28.2023'+'\033[0m')
   continue 
  if f == 'N1 Duo' or f == 'N1DUO' or f == 'N1 DUO' or f == 'n1duo' or f == 'n1 duo' or f == 'N1 duo':
   print('\033[46m'+'N1 Duo\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:25w\nCore:2\nVirtualization Core:54\nThread:4\nBase Clock:3200MHz\nBost Clock:5500MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 850\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'N1 Triple' or f == 'N1 triple' or f == 'n1triple' or f == 'n1 triple' or f == 'N1TRIPLE' or f == 'N1 TRIPLE' or f == 'N1triple':
   print('\033[46m'+'N1 Triple\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:35w\nCore:3\nVirtualization Core:54\nThread:6\nBase Clock:3900MHz\nBost Clock:5700MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 850\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'N1 Quad' or f == 'N1Quad' or f == 'n1 quad' or f == 'n1quad' or f == 'N1 QUAD' or f == 'N1QUAD' or f == 'n1 QUAD':
   print('\033[46m'+'N1 Quad\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:40w\nCore:4\nVirtualization Core:54\nThread:8\nBase Clock:4100MHz\nBost Clock:5900MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 850\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'N1 Penta' or f == 'N1Penta' or f == 'n1 penta' or f == 'n1penta' or f == 'N1PENTA' or f == 'n1 Penta' or f == 'N1 penta':
   print('\033[46m'+'N1 Penta\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:50w\nCore:5\nVirtualization Core:64\nThread:10\nBase Clock:4500MHz\nBost Clock:6900MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 850\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'N1 Octa' or f == 'n1octa' or f == 'N1Octa' or f == 'n1 octa' or f == 'N1 OCTA' or f == 'N1OCTA' or f == 'N1Octa' or f == '엔원 옥타':
   print('\033[46m'+'N1 Octa\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:65w\nCore:8\nVirtualization Core:64\nThread:16\nBase Clock:5000MHz\nBost Clock:7000MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 850\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'N1 Twelve' or f == 'N1Twelve' or f == 'n1 twelve' or f == 'n1twelve' or f == 'N1 TWELVE' or f == 'N1TWELVE':
   print('\033[46m'+'N1 Triple\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:90w\nCore:12\nVirtualization Core:72\nThread:24\nBase Clock:5500MHz\nBost Clock:7900MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 860\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'N1 Arcron' or f == 'N1Arcron' or f == 'N1 arcron' or f == 'n1 arcron' or f == 'n1arcron' or f == 'N1ARCRON' or f == 'M1 ARCRON':
   print('\033[46m'+'N1 Arcron\nType:CPU\nBase:K128\nSeries:N1')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3')
   print('TDP:140w\nCore:18\nVirtualization Core:96\nThread:36\nBase Clock:6000MHz\nBost Clock:9900MHz\nSocket:AMHC\nMaxium Temperature:120℃\nAOB:true')
   print('Innards Graphics:Graphics 870\nRelease:Jun 6.2023'+'\033[0m')
   continue
  if f == 'P1' or f == 'p1':
   print('\033[46m'+'P1\nType:CPU\nBase:K32\nSeries:P')
   print('Support Command:8BitAr,16BitAr,HCC')
   print('TDP:30w\nCore:2\nVirtualization Core:None\nThread:2\nBase Clock:2500MHz\nBost Clock:2900MHz\nSocket:HC2\nMaxium Temperature:90℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Dec 5.2015'+'\033[0m')
   continue
  if f == 'P2' or f == 'p2':
   print('\033[46m'+'P2\nType:CPU\nBase:K32\nSeries:P')
   print('Support Command:HCC,ORO1,OpenProject-ZERO,OpenProject-Metal,AIOS')
   print('TDP:120w\nCore:2\nVirtualization Core:None\nThread:2\nBase Clock:1700MHz\nBost Clock:1800MHz\nSocket:HC2\nMaxium Temperature:90℃\nAOB:true')
   print('Innards Graphics:Graphics 250\nRelease:Dec 11.2015'+'\033[0m')
   continue
  if f == 'P3' or f == 'p3':
   print('\033[46m'+'P3\nType:CPU\nBase:K64\nSeries:P')
   print('Support Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:170w\nCore:12\nVirtualization Core:1\nThread:24\nBase Clock:6500MHz\nBost Clock:7200MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:true')
   print('Innards Graphics:Graphice 590\nRelease:Feb 18.2020'+'\033[0m')
   continue
  if f == 'P4' or f=="p4":
   print('\033[46m'+'P4\nType:CPU\nBase:K64\nSeries:P')
   print('Support Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,32bitAr,16bitAr,8bitAr')
   print('TDP:70w\nCore:1\nVirtualization Core:None\nThread:2\nBase Clock:5100MHz\nBost Clock:8000MHz\nSocket:HC3\nMaxium Temperature:100℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Mar 3.2020'+'\033[0m')
   continue
  if f == 'P5' or f == 'p5':
   print('\033[46m'+'P5\nType:CPU\nBase:KARM\nSeries:P')
   print('Support Command:LELPM,OEES,OEEE-1121,OEEE-1240,OEEE-1242')
   print('TDP:30w\nCore:4\nVirtualization Core:None\nThread:4\nBase Clock:3400MHz\nBost Clock:4200MHz\nSocket:HARM\nMaxium Temperature:70℃\nAOB:fales')
   print('Innards Graphics:PieLPR Gen 2+\nRelease:Jun 9.2020'+'\033[0m')
   continue
  if f == 'P5 Pro' or f == 'p5 pro' or f == 'P5 pro' or f == 'p5pro' or f == 'P5Pro' or f == 'P5PRO' or f == "P5 PRO":
   print('\033[46m'+'P5 Pro\nType:CPU\nBase:KARM\nSeries:P')
   print('Support Command:LELPM,OEES,OEEE-1121,OEEE-1240,OEEE-1242,OEEE-1300,OEEE-1319,OROM')
   print('TDP:60w\nCore:6\nVirtualization Core:None\nThread:6\nBase Clock:3600MHz\nBost Clock:4500MHz\nSocket:HARM\nMaxium Temperature:85℃\nAOB:fales')
   print('Innards Graphics:PieLPR Gen 2+\nRelease:Nov 30.2020'+'\033[0m')
   continue
  if f == 'P5 Ultar' or f == 'p5 ultar' or f == 'p5ultar' or f == 'P5Ultar' or f == 'P5ULTAR' or f == 'P5 ULTAR':
   print('\033[46m'+'P5 Ultar\nType:CPU\nBase:KARM\nSeries:P')
   print('Support Command:LELPM,OEES,OROM,TMLARMCMD')
   print('TDP:75w\nCore:12\nVirtualization Core:None\nThread:12\nBase Clock:4000MHz\nBost Clock:5200MHz\nSocket:HARM\nMaxium Temperature:85℃\nAOB:fales')
   print('Innards Graphics:SigmaLPR Gen 1+\nRelease:Nov 22.2022'+'\033[0m')
   continue
  if f == 'p6' or f == 'P6':
   print('\033[46m'+'P6\nType:CPU\nBase:TK86\nSeries:P')
   print('Support Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,64bitAr,32bitAr,16bitAr,8bitAr')
   print('TDP:130w\nCore:24\nVirtualization Core:24\nThread:24\nBase Clock:8000MHz\nBost Clock:12000MHz\nSocket:TPC6EX\nMaxium Temperature:100℃\nAOB:true')
   print('Innards Graphics:Graphice 650\nRelease:Jan 20.2021'+'\033[0m')
   continue
  if f == 'P7' or f == 'p7':
   print('\033[46m'+'P7\nType:CPU\nBase:TK96\nSeries:P')
   print('Support Command:NKPCCPL,HCC,ORO2,ORO3,ORG,OROS,OTC,PTMD,Lans+,ALans+,86bitAr,64bitAr,32bitAr,16bitAr,8bitAr')
   print('TDP:150w\nCore:24\nVirtualization Core:24\nThread:24\nBase Clock:8100MHz\nBost Clock:12100MHz\nSocket:TPC7EX\nMaxium Temperature:100℃\nAOB:true')
   print('Innards Graphics:None\nRelease:Jul 25.2021'+'\033[0m')
   continue
  if f == 'P8' or f == 'p8':
   print('\033[46m'+'P8\nType:CPU\nBase:K64\nSeries:P')
   print('Support Command:HCC,HCC+,ORO3,ORO4,ORG,OROS,OROM,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,CCA3,TMLARMCMD')
   print('TDP:120w\nCore:12\nVirtualization Core:56\nThread:24\nBase Clock:120200MHz\nBost Clock:140000MHz\nSocket:HC4\nMaxium Temperature:90℃\nAOB:true')
   print('Innards Graphics:MEGALPR Gen 2\nRelease:Jan 27.2023'+'\033[0m')
   continue
  if f == 'A2 3050' or f == 'a2 3050' or f == 'a23050' or f == 'A23050' or f == 'A2-3050':
   print('\033[46m'+'A2 3050\nType:CPU\nBase:K64\nSeries:A2 3000')
   print('Support Command:HCC,HCC+,ORO3,ORG,OROS,OTC,PTMD,AMD+,intel+,Lans+,ALans+,DLans+,MEGA+,32bitAr,16bitAr')
   print('TDP:45w\nCore:6\nVirtualization Core:None\nThread:12\nBase Clock:18120MHz\nBost Clock:23000MHz\nSocket:HC3\nMaxium Temperature:95℃\nAOB:fales')
   print('Innards Graphics:Graphics 650\nRelease:Jan 12.2022'+'\033[0m')
   continue
  if f == 'list' or f == 'List' or f == 'LIST' or f == 'Help' or f == 'HELP' or f == 'help':
   time.sleep(2)
   print('\033[41m'+'https://amondbabaro.notion.site/H-O-S_NNDB-2311-23b176e4e98045b1864119ea5e5e4fd3?pvs=4'+'\033[0m')
   continue
  if f == 'stop' or f == 'STOP' or f == 'reboot' or f=='quit' or f=='QUIT':
   print(quit())
  else:
   print('\033[41m'+'error:Please check the search word'+'\033[0m')#error
   time.sleep(1)
   reset
   continue