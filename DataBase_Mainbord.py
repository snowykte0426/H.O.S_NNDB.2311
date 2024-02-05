# -*- coding: utf-8 -*-
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
class DB_MAINBORD():
 import time
 c1 = '12'
 def reset():
  keyword = None
  parttype = None
  find = None
  f = None
  return keyword,find,f,parttype
 print('\033[41m'+'The motherboard may be designed and configured differently for each subvendor,\nso please double-check the specifications specified by each manufacturer'+'\033[0m')
 while (c1 == '12'):
  keyword = input('\033[0m'+'Enter the desired part...\n')
  find = keyword
  f = keyword = find
  F = keyword
  print
  if f == 'back':
   from Start import reboot
  if f == 'Model 1125' or f == 'Model1125' or f == 'model 1125' or f == 'model1125' or f == 'MODEL 1125' or f == 'MODEL1125':
   print('\033[46m'+'Model 1125\nType:Mainbord\nChipset:1125\nCPU Socket:HARM\nPhase:4+2\nTDC:100A\nScalability:2.PCIe 3.0 x8,\nM.2 Socket:True\nSupport Storage type:PCIe 3.0,NVMe 1.4,SATA3\nPCI Qumantem:None\nMaxium Temperature:75℃\nSuppport RAM type:DDR4,DDR4 ECC\nMaxium RAM Size:128GB\nMaxium RAM Speed:4800MHz\nRelease:Dec 23.2021'+'\033[0m')
   continue
  if f == 'b100' or f == 'B100' or f == 'b-100' or f == 'b100':
   print('\033[46m'+'B100\nType:Mainbord\nChipset:B100\nCPU Socket:HCS\nPhase:2+1\nTDC:25A\nScalability:1.PCIe 2.0 x16\nM.2 Socket:false')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3\nPCI Qumantem:None\nMaxium Temperature:80℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:32GB\nMaxium RAM Speed:1694MHz\nRelease:Jun 1.2014'+'\033[0m')
   continue
  if f == 'b120' or f == 'b-120' or f == 'B120' or f == 'B-120':
   print('\033[46m'+'B120\nType:Mainbord\nChipset:B100\nCPU Socket:HCS\nPhase:5+3\nTDC:30A\nScalability:1.PCIe 2.0 x16\nM.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3\nPCI Qumantem:None\nMaxium Temperature:80℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:32GB\nMaxium RAM Speed:1694MHz\nRelease:Jun 1.2014'+'\033[0m')
   continue
  if f == 'b140' or f == 'b-140' or f == 'B140' or f == 'B-140':
   print('\033[46m'+'B140\nType:Mainbord\nChipset:B100\nCPU Socket:HCS\nPhase:8+3\nTDC:30A\nScalability:1.PCIe 2.0 x16,2.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3\nPCI Qumantem:None\nMaxium Temperature:90℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:32GB\nMaxium RAM Speed:1694MHz\nRelease:Jun 1.2014'+'\033[0m')
   continue
  if f == 'b180' or f == 'B180' or f == 'B-180' or f == 'b-180':
   print('\033[46m'+'B180\nType:Mainbord\nChipset:B100\nCPU Socket:HCS\nPhase:10+4\nTDC:35A\nScalability:1.PCIe 2.0 x16,1.PCIe 2.0 x4,2.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3,U.2\nPCI Qumantem:None\nMaxium Temperature:90℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:48GB\nMaxium RAM Speed:1833MHz\nRelease:Mar 4.2014'+'\033[0m')
   continue
  if f == 'b190' or f == 'b-190' or f == 'B190' or f == 'B-190':
   print('\033[46m'+'B190\nType:Mainbord\nChipset:B100\nCPU Socket:HCS\nPhase:12+5\nTDC:35A\nScalability:2.PCIe 2.0 x16,1.PCIe 2.0 x8,4.PCIe 2.0 x4,2.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3,U.2\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:48GB\nMaxium RAM Speed:1833MHz\nRelease:Mar 4.2014'+'\033[0m')
   continue
  if f == 'b195' or f == 'b-195' or f == 'B195' or f == 'B-195':
   print('\033[46m'+'B195\nType:Mainbord\nChipset:B100\nCPU Socket:HCS\nPhase:16+8\nTDC:35A\nScalability:2.PCIe 2.0 x16,1.PCIe 2.0 x8,4.PCIe 2.0 x4,2.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3,U.2\nPCI Qumantem:None\nMaxium Temperature:105℃\nSuppport RAM type:DDR3,DDR3 ECC')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2166MHz\nRelease:Jun 6.2015'+'\033[0m')
   continue
  if f == 'Model 250' or f == 'Model250' or f == 'model 250' or f == 'model250' or f == 'MODEL 250' or f == 'MODEL250':
   print('\033[46m'+'Model 250\nType:Mainbord\nChipset:Model 200\nCPU Socket:HC2\nPhase:4+1\nTDC:35A\nScalability:1.PCIe 2.0 x16,2.PCIe 2.0 x4,1.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3\nPCI Qumantem:None\nMaxium Temperature:90℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:48GB\nMaxium RAM Speed:1833MHz\nRelease:Apr 5.2016'+'\033[0m')
   continue
  if f == 'Model 260' or f == 'Model260' or f == 'model 260' or f == 'model260' or f == 'MODEL 260' or f == 'MODEL260':
   print('\033[46m'+'Model 260\nType:Mainbord\nChipset:Model 200\nCPU Socket:HC2\nPhase:8+2\nTDC:35A\nScalability:1.PCIe 2.0 x16,2.PCIe 2.0 x4,1.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3\nPCI Qumantem:None\nMaxium Temperature:90℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:48GB\nMaxium RAM Speed:1833MHz\nRelease:Apr 5.2016'+'\033[0m')
   continue
  if f == 'Model 270' or f == 'Model270' or f == 'model 270' or f == 'model270' or f == 'MODEL270' or f=='MODEL 270':
   print('\033[46m'+'Model 270\nType:Mainbord\nChipset:Model 200\nCPU Socket:HC2\nPhase:10+2\nTDC:40A\nScalability:2.PCIe 2.0 x16,1.PCIe 2.0 x8,2.PCIe 2.0 x4,1.PCIe 2.0 x1')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3,U.2\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2166MHz\nRelease:Apr 5.2016'+'\033[0m')
   continue
  if f == 'Model 280' or f == 'model280' or f =='Model280' or f == 'MODEL 280' or f =='MODEL280' or f == 'model 280':
   print('\033[46m'+'Model 280\nType:Mainbord\nChipset:Model 200\nCPU Socket:HC2\nPhase:14+2\nTDC:40A\nScalability:2.PCIe 2.0 x16,1.PCIe 2.0 x8,2.PCIe 2.0 x3,1.PCIe 2.0 x2')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 2.0,SATA2,SATA3,U.2\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR3')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2399MHz\nRelease:Apr 5.2016'+'\033[0m')
   continue
  if f =='model300' or f =='model 300' or f == 'Model300' or f == 'Model 300' or f == 'MODEL300' or f == 'MODEL 300':
   print('\033[46m'+'Model 300\nType:Mainbord\nChipset:Model 300\nCPU Socket:HC3\nPhase:2+1\nTDC:40A\nScalability:1.PCIe 3.0 x16')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:48GB\nMaxium RAM Speed:2166MHz\nRelease:Nov 5.2017'+'\033[0m')
   continue
  if f == 'Model350' or f == 'Model 350' or f == 'model 350' or f == 'MODEL 350' or f=='MODEL350' or f == 'model350':
   print('\033[46m'+'Model 350\nType:Mainbord\nChipset:Model 300\nCPU Socket:HC3\nPhase:4+1\nTDC:40A\nScalability:2.PCIe 3.0 x16')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2666MHz\nRelease:Nov 5.2017'+'\033[0m')
   continue 
  if f == 'model380'or f=='model 380' or f=='Model380' or f=='Model 380' or f=='MODEL 380' or f=='MODEL380':
   print('\033[46m'+'Model 380\nType:Mainbord\nChipset:Model 300\nCPU Socket:HC3\nPhase:12+3\nTDC:40A\nScalability:2.PCIe 3.0 x16,1.PCIe 3.0 x4')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2666MHz\nRelease:Nov 5.2017'+'\033[0m')
   continue 
  if f=='model450' or f=='model 450' or f =='Model450' or f=='Model 450' or f=='MODEL450' or f=='MODEL 450':
   print('\033[46m'+'Model 450\nType:Mainbord\nChipset:Model 400\nCPU Socket:HC3\nPhase:5+2\nTDC:45A\nScalability:1.PCIe 3.0 x16')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2666MHz\nRelease:Fed 2.2018'+'\033[0m')
   continue 
  if f=='model460' or f=='model 460' or f=='MODEL460' or f=='MODEL 460' or f== 'Model460' or f=='Model460':
   print('\033[46m'+'Model 460\nType:Mainbord\nChipset:Model 400\nCPU Socket:HC3\nPhase:7+2\nTDC:45A\nScalability:2.PCIe 3.0 x16')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2933MHz\nRelease:Fed 2.2018'+'\033[0m')
   continue
  if f=='MODEL470' or f=='MODEL470' or f=='Model470' or f=='Model 470' or f=='model470' or f=="model 470":
   print('\033[46m'+'Model 470\nType:Mainbord\nChipset:Model 400\nCPU Socket:HC3\nPhase:9+3\nTDC:45A\nScalability:3.PCIe 3.0 x16,1.PCIe 3.0 x8,1.PCIe 3.0 x4')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2933MHz\nRelease:Fed 2.2018'+'\033[0m')
   continue
  if f=="MODEL480" or f=='MODEL 480' or f=='Model480' or f=='Model 480' or f=='model480' or f=='model 480':
   print('\033[46m'+'Model 480\nType:Mainbord\nChipset:Model 400\nCPU Socket:HC3\nPhase:14+4\nTDC:45A\nScalability:3.PCIe 3.0 x16,1.PCIe 3.0 x8,2.PCIe 3.0 x4,1.PCIe 3.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:3200MHz\nRelease:Fed 2.2018'+'\033[0m')
   continue
  if f=='Model650' or f=='Model 650' or f=='model650' or f=='model 650' or f=='MODEL 650' or f=='MODEL650':
   print('\033[46m'+'Model 650\nType:Mainbord\nChipset:Model 600\nCPU Socket:HC3\nPhase:5+2\nTDC:45A\nScalability:1.PCIe 3.0 x16,1.PCIe 3.0 x4')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:2933MHz\nRelease:Dec 16.2019'+'\033[0m')
   continue
  if f=='Model660' or f=='Model 660' or f=='MODEL660' or f=='MODEL 660' or f=='model660' or f=='model 660':
   print('\033[46m'+'Model 660\nType:Mainbord\nChipset:Model 600\nCPU Socket:HC3\nPhase:7+2\nTDC:50A\nScalability:1.PCIe 3.0 x16,1.PCIe 3.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:64GB\nMaxium RAM Speed:3200MHz\nRelease:Dec 16.2019'+'\033[0m')
   continue
  if f=='Model 670' or f=='Model670' or f=='model670' or f=='model 670' or f== 'MODEL670' or f == 'MODEL 670':
   print('\033[46m'+'Model 670\nType:Mainbord\nChipset:Model 600\nCPU Socket:HC3\nPhase:9+3\nTDC:50A\nScalability:2.PCIe 3.0 x16,1.PCIe 3.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:96GB\nMaxium RAM Speed:3200MHz\nRelease:Dec 16.2019'+'\033[0m')
   continue
  if f == 'model 680' or f=='model680' or f=='Model680' or f=='Model 680' or f=='MODEL680' or f=='MODEL 680':
   print('\033[46m'+'Model 680\nType:Mainbord\nChipset:Model 600\nCPU Socket:HC3\nPhase:14+5\nTDC:50A\nScalability:3.PCIe 3.0 x16,1.PCIe 3.0 x4,2.PCIe 3.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 3.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:96GB\nMaxium RAM Speed:3666MHz\nRelease:Dec 16.2019'+'\033[0m')
   continue
  if f=='model770' or f=='model 770' or f=='MODEL770' or f=='MODEL 770' or f=='Model 770' or f == 'Model770':#M600 시리즈에서 NVMe만 지원
   print('\033[46m'+'Model 770\nType:Mainbord\nChipset:Model 700\nCPU Socket:HC3\nPhase:9+3\nTDC:50A\nScalability:1.PCIe 4.0 x16,1.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 1.3,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:128GB\nMaxium RAM Speed:3200MHz\nRelease:Mar 9.2020'+'\033[0m')
   continue
  if f=='model780' or f=='model 780' or f=='MODEL780' or F == 'MODEL 780' or f=='Model 780' or f=='Model780':
   print('\033[46m'+'Model 780\nType:Mainbord\nChipset:Model 700\nCPU Socket:HC3\nPhase:14+4\nTDC:50A\nScalability:2.PCIe 4.0 x16,1.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 1.3,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:128GB\nMaxium RAM Speed:4800MHz\nRelease:Mar 9.2020'+'\033[0m')
   continue
  if f=='model790' or f=='model 790' or f=='MODEL790' or f=='MODEL 790' or f=='Model 790' or f=='Model790':
   print('\033[46m'+'Model 790\nType:Mainbord\nChipset:Model 700\nCPU Socket:HC3\nPhase:18+6\nTDC:50A\nScalability:4.PCIe 4.0 x16,2.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 1.3,SATA3\nPCI Qumantem:None\nMaxium Temperature:95℃\nSuppport RAM type:DDR4')
   print('Maxium RAM Size:128GB\nMaxium RAM Speed:4800MHz\nRelease:Mar 9.2020'+'\033[0m')
   continue
  if f=='model 850' or f=='model850' or f=='Model850' or f=='Model 850' or f=='MODEL850' or F=='MODEL 850':
   print('\033[46m'+'Model 850\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:7+2\nTDC:60A\nScalability:1.PCIe 5.0 x16')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 1.4,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5')
   print('Maxium RAM Size:128GB\nMaxium RAM Speed:6800MHz\nRelease:Jan 29.2022'+'\033[0m')#A3 3000 Serise Rel
   continue
  if f=='model860' or f=='model 860' or f=='Model860' or f=='Model 860' or f=='MODEL860' or f=='MODEL 860':
   print('\033[46m'+'Model 860\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:9+2\nTDC:60A\nScalability:2.PCIe 5.0 x16')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 1.4,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5')
   print('Maxium RAM Size:128GB\nMaxium RAM Speed:6800MHz\nRelease:Jan 29.2022'+'\033[0m')
   continue
  if f=='Model 870' or f=='Model870' or f=='MODEL870' or f=='MODEL 870' or f=='model 870' or f=='model870':
   print('\033[46m'+'Model 870\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:12+4\nTDC:70A\nScalability:1.PCIe 5.0 x16,2.PCIe 5.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 1.4,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5')
   print('Maxium RAM Size:256GB\nMaxium RAM Speed:8400MHz\nRelease:Jan 29.2022'+'\033[0m')
   continue
  if f=='model880' or f=='model 880' or f=='MODEL 880' or F == 'MODEL880' or f=='Model880' or f== 'model 880':
   print('\033[46m'+'Model 880\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:15+7\nTDC:75A\nScalability:4.PCIe 5.0 x16,2.PCIe 5.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 1.4,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5')
   print('Maxium RAM Size:256GB\nMaxium RAM Speed:8400MHz\nRelease:Jan 29.2022'+'\033[0m')
   continue 
  if f=='model 890' or f=='Model 890' or f=='Model890' or f=='model890' or f=='MODEL890' or F=='MODEL 890':
   print('\033[46m'+'Model 890\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:24+10\nTDC:80A\nScalability:4.PCIe 5.0 x16,4.PCIe 5.0 x4,1.PCIe 5.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 2.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR6')
   print('Maxium RAM Size:512GB\nMaxium RAM Speed:16000MHz\nRelease:Nov 20.2022'+'\033[0m')
   continue
  if f=='model875' or f=='model 875' or F=='MODEL875' or F=='MODEL 875' or f=='Model 875' or f=='Model875':
   print('\033[46m'+'Model 875\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:14+5\nTDC:80A\nScalability:3.PCIe 5.0 x16,1.PCIe 5.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 2.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR6')
   print('Maxium RAM Size:256GB\nMaxium RAM Speed:12000MHz\nRelease:Nov 20.2022'+'\033[0m')
   continue
  if f=='model 895' or f=='model895' or f=='Model 895' or f=='Model895' or f=='MODEL895' or F=='MODEL 895':
   print('\033[46m'+'Model 895\nType:Mainbord\nChipset:Model 800\nCPU Socket:HC3\nPhase:27+12\nTDC:80A\nScalability:6.PCIe 5.0 x16,4.PCIe 5.0 x4,2.PCIe 5.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 5.0,NVMe 2.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:140℃\nSuppport RAM type:DDR6')
   print('Maxium RAM Size:512GB\nMaxium RAM Speed:24444MHz\nRelease:Nov 20.2022'+'\033[0m')
   continue
  if f=='model950' or f=='model 950' or f=='MODEL950' or f=='MODEL 950' or f=='Model950' or f=='Model 950':
   print('\033[46m'+'Model 950\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:10+3\nTDC:100A\nScalability:1.PCIe 5.0 x16,1.PCIe 5.0 x4,1.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:140℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:512GB\nMaxium RAM Speed:14000MHz\nRelease:Apr 10.2023'+'\033[0m')
   continue 
  if f=='model960' or f=='model 960' or f=='Model960' or f == 'Model 960' or f=='MODEL 960' or f=='MODEL960':
   print('\033[46m'+'Model 960\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:12+4\nTDC:100A\nScalability:2.PCIe 5.0 x16,1.PCIe 5.0 x4,1.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:140℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:24000MHz\nRelease:Apr 10.2023'+'\033[0m')
   continue 
  if f=='model970' or f=='model 970' or f== 'Model970' or f=='Model 970' or f=='MODEL 970' or F=='MODEL970':
   print('\033[46m'+'Model 970\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:17+4\nTDC:100A\nScalability:2.PCIe 5.0 x16,2.PCIe 5.0 x4,1.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:24000MHz\nRelease:Apr 10.2023'+'\033[0m')
   continue
  if f=='model980' or f=='model 980' or f=='Model980' or f=='Model 980' or f=='MODEL980' or F=='MODEL 980':
   print('\033[46m'+'Model 980\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:20+5\nTDC:100A\nScalability:2.PCIe 5.0 x16,2.PCIe 5.0 x4,1.PCIq 1.0 x8,2.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:24000MHz\nRelease:Apr 10.2023'+'\033[0m')
   continue
  if f=='model990' or f=='model 990' or f=='Model990' or f=='Model 990' or f=='MODEL990' or F=='MODEL 990':
   print('\033[46m'+'Model 990\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:25+7\nTDC:140A\nScalability:3.PCIe 5.0 x16,2.PCIe 5.0 x4,2.PCIq 1.0 x4,1.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:28000MHz\nRelease:Apr 10.2023'+'\033[0m')
   continue
  if f== 'model995' or f=='model995' or f=='Model995' or f=='Model 995' or f=='MODEL995' or F=='MODEL 995':
   print('\033[46m'+'Model 995\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:28+10\nTDC:140A\nScalability:3.PCIe 5.0 x16,4.PCIe 5.0 x4,3.PCIq 1.0 x4,2.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:28000MHz\nRelease:Apr 10.2023'+'\033[0m')
   continue
  if f=='model996' or f=='model 996' or f=='MODEL 996' or f=='MODEL 996' or F=='Model 996' or F=='Model996':
   print('\033[46m'+'Model 996\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:30+10\nTDC:160A\nScalability:4.PCIe 5.0 x16,2.PCIe 5.0 x4,3.PCIq 1.0 x4,2.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:32000MHz\nRelease:Jun 1.2023'+'\033[0m')
   continue
  if f=='M997' or f=='m997' or f=='m 997' or f=='M 997':
   print('\033[46m'+'M997\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:33+14\nTDC:160A\nScalability:4.PCIe 5.0 x16,4.PCIe 5.0 x4,2.PCIq 1.0 x4,3.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:32000MHz\nRelease:Sep 5.2023'+'\033[0m')#A3 5950H Rel
   continue
  if f=='M998' or f=='m998' or f=='m 998' or f=='M 998':
   print('\033[46m'+'M998\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:35+14\nTDC:180A\nScalability:4.PCIq 1.0 x16,4.PCIq 1.0 x4,1.PCIq 1.0 x1')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:32000MHz\nRelease:Nov 14.2023'+'\033[0m')
   continue
  if f=='M951' or f=='M 951' or f=='m951' or F=='m 951':
   print('\033[46m'+'M951\nType:Mainbord\nChipset:Model 900\nCPU Socket:HC4\nPhase:11+4\nTDC:160A\nScalability:2.PCIe 5.0 x16,1.PCIq 1.0 x16,1.PCIq 1.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3\nPCI Qumantem:True\nMaxium Temperature:200℃\nSuppport RAM type:DDR7')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:24000MHz\nRelease:Sep 5.2023'+'\033[0m')
   continue
  if f == 'TPC6MTB' or f=='tpc6mtb':
   print('\033[46m'+'TPC6MTB\nType:Mainbord\nChipset:TP6\nCPU Socket:HC4\nPhase:14+4\nTDC:100A\nScalability:1.PCIe 4.0 x8')
   print('M.2 Socket:None')
   print('Support Storage type:PCIe 4.0,NVMe 2.0\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR6')
   print('Maxium RAM Size:1TB\nMaxium RAM Speed:9994MHz\nRelease:Jan 20.2021'+'\033[0m')
   continue
  if f=='TPC6MBCTS'or F=='tpc6mbcts':
   print('\033[46m'+'TPC6MBCTS\nType:Mainbord\nChipset:TP6\nCPU Socket:HC4\nPhase:16+7\nTDC:100A\nScalability:1.PCIe 4.0 x16,1.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR6')
   print('Maxium RAM Size:1TB\nMaxium RAM Speed:12222MHz\nRelease:Jan 20.2021'+'\033[0m')
   continue
  if f=='TPC7MTB'or F=='tpc7mtb':
   print('\033[46m'+'TPC7MTB\nType:Mainbord\nChipset:TP7\nCPU Socket:HC4\nPhase:16+5\nTDC:100A\nScalability:1.PCIe 4.0 x8')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR6')
   print('Maxium RAM Size:1TB\nMaxium RAM Speed:9994MHz\nRelease:Jul 25.2021'+'\033[0m')
   continue
  if f=='Model 1130' or f== 'Model1130' or f=='MODEL 1130' or F=='MODEL1130' or F=='model1130' or f=='model 1130':
   print('\033[46m'+'Model 1130\nType:Mainbord\nChipset:1125\nCPU Socket:HARM\nPhase:14+4\nTDC:120A\nScalability:2.PCIe 4.0 x16,\nM.2 Socket:True\nSupport Storage type:PCIe 4.0,NVMe 2.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC\nMaxium RAM Size:512GB\nMaxium RAM Speed:12000MHz\nRelease:Nov 30.2020'+'\033[0m')
   continue
  if f=='Model 1140' or f=='Model1140' or f=='MODEL1140' or f=='MODEL 1140' or f=='model 1140' or f=='model1140':
   print('\033[46m'+'Model 1140\nType:Mainbord\nChipset:1125\nCPU Socket:HARM\nPhase:16+5\nTDC:120A\nScalability:2.PCIe 4.0 x16,\nM.2 Socket:True\nSupport Storage type:PCIe 4.0,NVMe 2.0,SATA3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC\nMaxium RAM Size:512GB\nMaxium RAM Speed:12000MHz\nRelease:Nov 22.2022'+'\033[0m')
   continue
  if f=='S60' or f=='s60' or f=='S 60' or f=='s 60':
   print('\033[46m'+'S60\nType:Mainbord\nChipset:S10\nCPU Socket:AMHC\nPhase:12+4\nTDC:140A\nScalability:8.PCIe 4.0 x16,4.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0,SATA3,SAS3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:12000MHz\nRelease:Jun 22.2020'+'\033[0m')
   continue
  if f=='S50' or f=='S 50' or f=='s50' or f=='s 50':
   print('\033[46m'+'S50\nType:Mainbord\nChipset:S10\nCPU Socket:AMHC\nPhase:8+3\nTDC:140A\nScalability:6.PCIe 4.0 x16,2.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0,SATA3,SAS3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:12000MHz\nRelease:Jun 22.2020'+'\033[0m')
   continue
  if f== 'S70' or f=='S 70' or f=='s70' or f=='s 70':
   print('\033[46m'+'S70\nType:Mainbord\nChipset:S10\nCPU Socket:AMHC\nPhase:15+5\nTDC:140A\nScalability:12.PCIe 4.0 x16,6.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0,SATA3,SAS3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:12000MHz\nRelease:Jun 22.2020'+'\033[0m')
   continue
  if f=='S80' or f=='s80' or f=='S 80' or f=='s 80':
   print('\033[46m'+'S80\nType:Mainbord\nChipset:S10\nCPU Socket:AMHC\nPhase:18+5\nTDC:160A\nScalability:12.PCIe 4.0 x16,6.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0,SATA3,SAS3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:12000MHz\nRelease:Jun 22.2020'+'\033[0m')
   continue
  if f=='S90' or f=='S 90' or f== 's90' or f=='s 90':
   print('\033[46m'+'S90\nType:Mainbord\nChipset:S10\nCPU Socket:AMHC\nPhase:20+7\nTDC:160A\nScalability:16.PCIe 4.0 x16,8.PCIe 4.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIe 4.0,NVMe 2.0,SATA3,SAS3\nPCI Qumantem:None\nMaxium Temperature:120℃\nSuppport RAM type:DDR5 ECC')
   print('Maxium RAM Size:2TB\nMaxium RAM Speed:12444MHz\nRelease:Jun 22.2020'+'\033[0m')
   continue
  if f== 's99' or f=='s 99' or f=='S99' or f=='S 99':
   print('\033[46m'+'S99\nType:Mainbord\nChipset:S10\nCPU Socket:AMHC\nPhase:26+10\nTDC:180A\nScalability:16.PCIq 5.0 x16,8.PCIq 5.0 x4')
   print('M.2 Socket:True')
   print('Support Storage type:PCIq 1.0,PCIe 5.0,NVMe 2.1,SATA3,SAS3\nPCI Qumantem:True\nMaxium Temperature:120℃\nSuppport RAM type:DDR7 ECC')
   print('Maxium RAM Size:6TB\nMaxium RAM Speed:24000MHz\nRelease:Jun 3.2023'+'\033[0m')
   continue
  if f == 'list' or f == 'List' or f == 'LIST' or f == 'Help' or f == 'HELP' or f == 'help':
   time.sleep(2)
   print('\033[41m'+'https://amondbabaro.notion.site/H-O-S_NNDB-2311-23b176e4e98045b1864119ea5e5e4fd3?pvs=4'+'\033[0m')
   continue
  if f == 'stop' or f == 'STOP' or f == 'reboot' or f=='quit' or f=='QUIT':
   print(quit())
  else:
   print('\033[41m'+'error:Please check the search word'+'\033[0m')
   time.sleep(1)
   reset
   continue