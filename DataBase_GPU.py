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
class DB_GPU():
 c1 = '12'
 def reset():
  keyword = None
  parttype = None
  find = None
  f = None
  return keyword,find,f,parttype
 import time
 print('\033[41m'+'The GPU category provides the manufacturer is (H.O.S) GPU factory default settings, which may vary depending on the customization of each VGA manufacturer.''\033[0m')
 while (c1 == '12'):
#CPU 파일 참조하며 제작하도록
  time.sleep(1)
  keyword = input('\033[0m'+'Enter the desired part...\n')
  find = keyword
  f = find
  if find == 'back':
   from Start import reboot
  if find == 'GC1080' or find == 'GC-1080' or find == 'gc1080' or find == 'gc-1080' or f == 'GC 1080' or find == 'Gc1080' or find == 'gC1080' or f == 'gc 1080' or find == 'Gc-1080' or find == 'gC-1080':
   print('\033[46m'+'GC-1080\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:4924\nMaximum Power:350w\nVRAM:32GB\nConnection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Apr 7.2023'+'\033[0m')
   time.sleep(2)
   continue
  if find == 'BC990' or find == 'bc990' or find == 'BC-990' or find == 'bc-990' or f == 'BC 990' or find == 'Bc990' or f == 'bc 990' or find == 'bC990':
   print('\033[46m'+'BC-990\nType:GPU\nSeries:BC\nArchitecture:MEGA\nCore Numb:4502\nMaximum Power:260w\nVRAM:24GB\nConnection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Apr 7.2023'+'\033[0m')
   time.sleep(2)
   continue
  if find == 'PC1250' or find == 'pc1250' or find == 'PC-1250' or find == 'pc-1250' or f == 'PC 1250' or f == 'pc 1250' or find == 'Pc1250' or find == 'pC1250' or find == 'Pc-1250' or find == 'pC-1250':
   print('\033[46m'+'PC-1250\nType:GPU\nSeries:PC\nArchitecture:MEGA\nCore Numb:5296\nMaximum Power:140w\nVRAM:16GB\nConnection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Apr 7.2023'+'\033[0m')
   time.sleep(2)
   continue
  if f == 'GC1090' or f == 'GC-1090' or f == 'gc1090' or f == 'gc 1090' or f == 'GC 1090' or f == 'gc-1090' or f == 'gC1090' or f == 'Gc1090':
   print('\033[46m'+'GC-1090\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:5464\nMaximum Power:550w\nVRAM:36GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:3\nMemory Type:GDDR7\nRelease:Jun 22.2023'+'\033[0m')
   continue
  if f == 'GC1100' or f == 'GC-1100' or f == 'gc1100' or f == 'gc 1100' or f == 'GC 1100' or f == 'gc-1100':
   print('\033[46m'+'GC-1100\nType:GPU\nSeries:GC\nArchitecture:EOX-2\nCore Numb:4516\nMaximum Power:240w\nVRAM:38GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jul 19.2023'+'\033[0m')
   continue
  if f == 'GC1080X' or f == 'GC-1080X' or f == ' gc1080x' or f == 'gc 1080x' or f == 'GC 1080X' or f == 'gc-1080x' or f == 'GC 1080x':
   print('\033[46m'+'GC-1080X\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:5288\nMaximum Power:490w\nVRAM:36GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jun 22.2023'+'\033[0m')
   continue
  if f == 'GC-1070' or f == 'GC1070' or f == 'gc 1070' or f == 'gc1070' or f == 'gc-1070' or f == 'GC일공칠공':
   print('\033[46m'+'GC-1070\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:4764\nMaximum Power:320w\nVRAM:28GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Dec 24.2022'+'\033[0m')
   continue
  if f == 'GC-1060' or f == 'gc1060' or f == 'GC1060' or f == 'gc-1060' or f == 'gc 1060' or f == 'gc1060' or f == 'GC 1060':
   print('\033[46m'+'GC-1060\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:4382\nMaximum Power:250w\nVRAM:20GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Dec 24.2022'+'\033[0m')
   continue
  if f == 'GC-1060X' or f == 'gc 1060x' or f == 'GC 1060X' or f == 'gc-1060x' or f == 'GC 1060X' or f == 'GC1060X' or f == 'gc1060x':
   print('\033[46m'+'GC-1060X\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:4564\nMaximum Power:270w\nVRAM:24GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Dec 24.2022'+'\033[0m')
   continue
  if f == 'Gc-1050X' or f == 'GC-1050X' or f == 'gc1050x' or f == 'GC 1050X' or f == 'gc-1050x' or f == 'gc 1050x' or f == 'GC1050X' or f == 'gC1050x':
   print('\033[46m'+'GC-1050X\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:4344\nMaximum Power:220w\nVRAM:18GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 13.2022'+'\033[0m')
   continue
  if f == 'GC-1050' or f == 'gc-1050' or f == 'gc1050' or f == 'gc 1050' or f == 'GC1050' or f == 'GC 1050' or f == 'gc--1050':
   print('\033[46m'+'GC-1050\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:4194\nMaximum Power:200w\nVRAM:16GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 13.2022'+'\033[0m')
   continue 
  if f == 'GC-1040' or f == 'Gc1040' or f == 'GC1040' or f == 'gc1040' or f == 'gc-1040' or f == 'gc 1040' or f == 'GC 1040':
   print('\033[46m'+'GC-1040\nType:GPU\nSeries:GC\nArchitecture:MEGA\nCore Numb:3952\nMaximum Power:160w\nVRAM:18GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 13.2022'+'\033[0m')
   continue
  if f == 'GC-1030' or f == 'GC1030' or f == 'gc1030' or f == 'gc 1030' or f == 'gc-1030' or f == 'GC 1030':
   print('\033[46m'+'GC-1030\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:4194\nMaximum Power:490w\nVRAM:20GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:3\nMemory Type:GDDR7\nRelease:Apr 2.2022'+'\033[0m')
   continue
  if f == 'gc-1030fe' or find == 'gc 1030fe' or f == 'gc1030fe' or f == 'gc 1030 fe' or f == 'GC-1030FE' or f == 'GC1030FE' or f == 'GC 1030FE' or f == 'GC-1030fe':
   print('\033[46m'+'GC-1030FE\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3996\nMaximum Power:450w\nVRAM:16GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:3\nMemory Type:GDDR7\nRelease:Apr 2.2022'+'\033[0m')
   continue
  if f == 'gc-1020' or f == 'gc1020' or f == 'gc 1020' or f == 'GC-1020' or f == "GC1020" or f == 'GC 1020':
   print('\033[46m'+'GC-1020\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3724\nMaximum Power:350w\nVRAM:16GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Fed 9.2022'+'\033[0m')
   continue 
  if find == 'GC-1020FE' or f == 'GC1020FE' or f == 'GC 1020FE' or f == 'gc-1020fe' or f == 'gc1020fe' or f == 'gc 1020fe' or f == 'GC-1020fe':
   print('\033[46m'+'GC-1020FE\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3578\nMaximum Power:290w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Fed 9.2022'+'\033[0m')
   continue 
  if f == 'gc-1010' or f == 'GC-1010' or f == 'GC 1010' or f == 'GC1010' or f == 'gc1010' or f == 'gc 1010':
   print('\033[46m'+'GC-1010\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3498\nMaximum Power:250w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jan 10.2022'+'\033[0m')
   continue
  if f == 'gc-1010fe' or f == 'gc1010fe' or f == 'gc 1010fe' or f == 'GC-1010fe' or f == 'GC-1010FE' or f == 'GC1010FE' or f == 'GC 1010FE':
   print('\033[46m'+'GC-1010FE\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3264\nMaximum Power:220w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Apr 2.2022'+'\033[0m')
   continue  
  if f == 'GC-1000' or f == 'gc-1000' or f == 'gc1000' or f == 'GC1000' or f == 'GC 1000' or f == 'gc 1000':
   print('\033[46m'+'GC-1000\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3008\nMaximum Power:150w\nVRAM:10GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Aug 28.2021'+'\033[0m')
   continue  
  if f == 'GC-990' or f == 'GC990' or f == 'GC 990' or f == 'gc-990' or f == 'gc990' or f == 'gc 990':
   print('\033[46m'+'GC-990\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:2674\nMaximum Power:90w\nVRAM:8GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Mar 11.2021'+'\033[0m')
   continue  
  if f == 'GC-990X' or f == 'GC990X' or f == 'GC 990X' or f == 'gc 990x' or f == 'gc-990x' or f == 'gc990x' or f == 'gc990X':
   print('\033[46m'+'GC-990X\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:3008\nMaximum Power:120w\nVRAM:8GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Aug 28.2021'+'\033[0m')
   continue
  if f == 'GC-980' or f == 'GC980' or f == 'GC 980' or f == 'gc-980' or f == 'gc980' or f == 'gc 980':
   print('\033[46m'+'GC-980\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:2316\nMaximum Power:80w\nVRAM:8GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jul 17.2021'+'\033[0m')
   continue
  if f == 'GC-970' or f == 'GC970' or f == 'GC 970' or f == 'gc-970' or f == 'gc 970' or f == 'gc970':
   print('\033[46m'+'GC-970\nType:GPU\nSeries:GC\nArchitecture:Sigma\nCore Numb:1982\nMaximum Power:65w\nVRAM:6GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:1\nMemory Type:GDDR7\nRelease:Jul 17.2021'+'\033[0m')
   continue  
  if f == 'GC-950' or f == 'GC950' or f == 'GC 950' or f == 'gc-950' or f == 'gc950' or f == 'gc 950':
   print('\033[46m'+'GC-950\nType:GPU\nSeries:GC\nArchitecture:Pie\nCore Numb:2764\nMaximum Power:200w\nVRAM:12GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jun 20.2021'+'\033[0m')
   continue  
  if f == 'GC-850' or f == 'GC850' or f == 'GC 850' or f=='gc-850' or f=='gc850' or f == 'gc 850':
   print('\033[46m'+'GC-850\nType:GPU\nSeries:GC\nArchitecture:Pie\nCore Numb:2518\nMaximum Power:180w\nVRAM:10GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 29.2020'+'\033[0m')
   continue 
  if f == 'GC-750' or f == 'GC750' or f=='GC 750' or f == 'gc-750' or f=='gc 750' or f == 'gc750':
   print('\033[46m'+'GC-750\nType:GPU\nSeries:GC\nArchitecture:Pie\nCore Numb:2372\nMaximum Power:125w\nVRAM:8GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 29.2020'+'\033[0m')
   continue
  if f == 'gc-650' or f == 'gc650' or f == 'gc 650' or f == 'GC650' or f == 'GC-650' or f == 'GC 650':
   print('\033[46m'+'GC-650\nType:GPU\nSeries:GC\nArchitecture:Pie\nCore Numb:2014\nMaximum Power:85w\nVRAM:6GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 29.2020'+'\033[0m')
   continue
  if f == 'BC-1000' or f == 'BC1000' or f == 'BC 1000' or f == 'bc-1000' or f == 'bc1000' or f=='bc 1000':
   print('\033[46m'+'BC-1000\nType:GPU\nSeries:BC\nArchitecture:EOX-2\nCore Numb:4098\nMaximum Power:170w\nVRAM:28GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jul 26.2023'+'\033[0m')
   continue 
  if f == 'BC-980' or f == 'bc-980' or f == 'bc 980' or f == 'BC980' or f == 'BC 980' or f == 'bc980':
   print('\033[46m'+'BC-980\nType:GPU\nSeries:BC\nArchitecture:MEGA\nCore Numb:4256\nMaximum Power:170w\nVRAM:20GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Dec 24.2022'+'\033[0m')
   continue 
  if f == 'BC-970' or f == 'bc-970' or f == 'bc 970' or f == 'bc970' or f == 'BC 970' or f == 'BC970':
   print('\033[46m'+'BC-970\nType:GPU\nSeries:BC\nArchitecture:MEGA\nCore Numb:3944\nMaximum Power:140w\nVRAM:16GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Oct 13.2022'+'\033[0m')
   continue 
  if f == 'BC-960' or f == 'BC960' or f == 'bc960' or f == 'bc-960' or f == 'BC 960' or f == 'bc 960':
   print('\033[46m'+'BC-960\nType:GPU\nSeries:BC\nArchitecture:Sigma\nCore Numb:3178\nMaximum Power:130w\nVRAM:12GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Apr 2.2022'+'\033[0m')
   continue 
  if f == 'BC-960X' or f == 'BC960X' or f == 'BC 960X' or f == 'bc-960x' or f == 'bc960x' or find == 'bc 960x' or keyword == 'bc960X':
   print('\033[46m'+'BC-960X\nType:GPU\nSeries:BC\nArchitecture:Sigma\nCore Numb:3510\nMaximum Power:145w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Apr 2.2022'+'\033[0m')
   continue
  if f == 'BC-950' or f == 'BC950' or f == 'BC 950' or f == "bc-950" or f == 'bc950' or f == 'bc 950':
   print('\033[46m'+'BC-950\nType:GPU\nSeries:BC\nArchitecture:Sigma\nCore Numb:3102\nMaximum Power:115w\nVRAM:8GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Fed 9.2022'+'\033[0m')
   continue 
  if f == 'PC-1250' or f == 'PC1250' or f == 'PC 1250' or f == 'pc-1250' or f == 'pc1250' or f == 'pc 1250':
   print('\033[46m'+'BC-1250\nType:GPU\nSeries:PC\nArchitecture:EOX-2\nCore Numb:5498\nMaximum Power:200w\nVRAM:22GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jul 19.2023'+'\033[0m')
   continue 
  if f == 'PC-1260' or f == 'PC1260' or f == 'PC 1260' or f == 'pc-1260' or f == 'pc1260' or f == 'pc 1260':
   print('\033[46m'+'BC-1260\nType:GPU\nSeries:PC\nArchitecture:EOX-2\nCore Numb:5614\nMaximum Power:220w\nVRAM:24GB')
   print('Connection:PCIe 5.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jul 19.2023'+'\033[0m')
   continue 
  if f == 'PC-1210' or f == 'PC1210' or f == 'pc1210' or f == 'PC 1210' or f == 'pc-1210' or f == 'pc 1210':
   print('\033[46m'+'BC-1210\nType:GPU\nSeries:PC\nArchitecture:MEGA\nCore Numb:3014\nMaximum Power:100w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Dec 24.2022'+'\033[0m')
   continue 
  if f == 'PC-1200' or f == 'PC1200' or f == 'PC 1200' or f == 'pc1200' or f == 'pc 1200' or f == 'pc-1200':
   print('\033[46m'+'BC-1200\nType:GPU\nSeries:PC\nArchitecture:Sigma\nCore Numb:3234\nMaximum Power:110w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Dec 24.2022'+'\033[0m')
   continue 
  if f == 'PC-1200X' or f == 'PC1200X' or f == 'PC 1200X' or f == 'pc-1200x' or f == 'pc 1200x' or f == 'pc1200x' or f == 'pc-1200X':
   print('\033[46m'+'BC-1200X\nType:GPU\nSeries:PC\nArchitecture:Sigma\nCore Numb:3336\nMaximum Power:150w\nVRAM:14GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:2\nMemory Type:GDDR7\nRelease:Jan 3.2023'+'\033[0m')
   continue 
  #내장 그래픽 외장그래픽화 카드들
  if f == 'PhotoGraphics 680' or f == 'PHOTOGRAPHICS 680' or f == 'photographics 680' or f == 'PhotoGraphics680' or f == 'PHOTOGRAPHICS680' or f == 'photographics680' or f == 'PG680' or f == 'pg680' or f == 'pg 680' or f == 'pg-680':
   print('\033[46m'+'PG-680\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-22\nCore Numb:86\nMaximum Power:30w\nVRAM:6GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Jan 24.2022'+'\033[0m')
   continue 
  if f == 'PG-690' or f == 'PG690' or f == 'PG 690' or f == 'pg690' or f == 'pg 690' or f == 'pg-690':
   print('\033[46m'+'PG-690\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-22\nCore Numb:94\nMaximum Power:30w\nVRAM:8GB')
   print('Connection:PCIe 4.0 16x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Jan 24.2022'+'\033[0m')
   continue 
  if f == 'PG-660' or f == 'PG660' or f == 'PG 660' or f == 'pg-660' or f == 'pg660' or f == 'pg 660':
   print('\033[46m'+'PG-660\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-22\nCore Numb:62\nMaximum Power:28w\nVRAM:6GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Jan 24.2022'+'\033[0m')
   continue 
  if f == 'PG-640' or f == 'pg-640' or f == 'PG640' or f == 'PG 640' or f == 'pg640' or f == 'pg640':
   print('\033[46m'+'PG-640\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-22\nCore Numb:53\nMaximum Power:25w\nVRAM:4GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Jan 24.2022'+'\033[0m')
   continue 
  if f == 'PG-620' or f == 'PG 620' or f == 'PG620' or f == 'pg-620' or f == 'pg 620' or f == 'pg620':
   print('\033[46m'+'PG-620\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-22\nCore Numb:38\nMaximum Power:20w\nVRAM:4GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Jan 24.2022'+'\033[0m')
   continue 
  if find == 'PG-580' or f == 'PG 580' or f == 'PG580' or f == 'pg-580' or f == 'pg580' or f == 'pg 580':
   print('\033[46m'+'PG-580\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-18v2\nCore Numb:78\nMaximum Power:30w\nVRAM:6GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Dec 19.2019'+'\033[0m')
   continue
  if f == 'PG-520' or f== 'pg-520' or f=='PG520' or f=='PG 520' or f == 'pg520' or f == 'pg 520':
   print('\033[46m'+'PG-520\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-18v2\nCore Numb:36\nMaximum Power:25w\nVRAM:4GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Dec 19.2019'+'\033[0m')
   continue
  if f == 'PG-480' or f == 'PG480' or f == 'PG 480' or f == 'pg-480' or f == 'pg480' or f == 'pg 480':
   print('\033[46m'+'PG-480\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-18\nCore Numb:46\nMaximum Power:30w\nVRAM:4GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Apr 15.2018'+'\033[0m')
   continue
  if f == 'PG-460' or f == 'PG460' or f == 'PG 460' or f == 'pg460' or f == 'pg 460' or f == 'pg-460':
   print('\033[46m'+'PG-460\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-18\nCore Numb:38\nMaximum Power:28w\nVRAM:4GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Apr 15.2018'+'\033[0m')
   continue
  if f == 'PG-450' or f == 'PG450' or f == 'PG 450' or f == 'pg450' or f == 'pg-450' or f == 'pg 450':
   print('\033[46m'+'PG-450\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-18\nCore Numb:34\nMaximum Power:28w\nVRAM:3GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Apr 15.2018'+'\033[0m')
   continue
  if f == 'PG-440' or f == 'PG440' or f == 'PG 440' or f == 'pg-440' or f == 'pg 440' or f == 'pg440':
   print('\033[46m'+'PG-440\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-18\nCore Numb:24\nMaximum Power:25w\nVRAM:2GB')
   print('Connection:PCIe 4.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:Apr 15.2018'+'\033[0m')
   continue
  if f == 'PG-300' or f == 'pg-300' or f == 'PG300' or f == 'pg300' or f == 'PG 300' or f == 'pg 300':
   print('\033[46m'+'PG-300\nType:GPU\nSeries:PhotoGraphics\nArchitecture:AGC-17\nCore Numb:12\nMaximum Power:15w\nVRAM:2GB')
   print('Connection:PCIe 3.0 8x\nPCI Slot:1\nMemory Type:GDDR6\nRelease:May 1.2018'+'\033[0m')
   continue
  if f == 'Under 6' or f=='UNDER 6' or f == 'under 6' or f == 'under6' or f == 'UNDER6' or f == 'Under6': 
   print('\033[46m'+'Under 6\nType:GPU\nSeries:Under\nArchitecture:EOX\nCore Numb:1428\nMaximum Power:200w\nVRAM:6GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Dec 29.2019'+'\033[0m')
   continue
  if f == 'Under 6X' or f == 'UNDER 6X' or f=='under6x' or f=='under 6x' or f=='UNDER6X' or f=='Under6X':
   print('\033[46m'+'Under 6X\nType:GPU\nSeries:Under\nArchitecture:EOX')
   print('Core Numb:1676\nMaximum Power:240w\nVRAM:8GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Dec 29.2019'+'\033[0m')
   continue
  if f=='Under 6FE' or f=='Under6FE' or f=='UNDER 6FE' or f=='UNDER6FE' or f=='under 6fe' or f == 'under6fe' or f=='under6FE':
   print('\033[46m'+'Under 6FE\nType:GPU\nSeries:Under\nArchitecture:EOX')
   print('Core Numb:1370\nMaximum Power:190w\nVRAM:6GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Apr 24.2020'+'\033[0m')
   continue
  if f=='Under6L' or f == 'Under 6L' or f == 'under 6l' or f == 'under6l' or f == 'UNDER 6L' or f == 'UNDER6L':
   print('\033[46m'+'Under 6L\nType:GPU\nSeries:Under\nArchitecture:EOX')
   print('Core Numb:1370\nMaximum Power:120w\nVRAM:4GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:None\nMemory Type:GDDR6\nRelease:Jan 17.2020'+'\033[0m')
   continue
  if f == 'Middel 5' or f=='Middel5' or f=='MIDDEL5' or f=='MIDDEL 5' or f=='middel5' or f=='middel 5':
   print('\033[46m'+'Middel 5\nType:GPU\nSeries:Middel\nArchitecture:EOX')
   print('Core Numb:1710\nMaximum Power:270w\nVRAM:10GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Dec 29.2019'+'\033[0m')
   continue
  if f == 'Middel 5X' or f == 'Middel5X' or f=='middel5x' or f == 'middel 5x' or f== 'MIDDEL5X' or f == 'MIDDEL 5X':
   print('\033[46m'+'Middel 5X\nType:GPU\nSeries:Middel\nArchitecture:EOX')
   print('Core Numb:1786\nMaximum Power:285w\nVRAM:10GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Dec 29.2019'+'\033[0m')
   continue
  if f == 'Middel5FE' or f == 'Middel 5FE' or f == 'middel 5fe' or f=='middel 5FE' or f== 'middel5FE'or f == 'middel5fe' or f == 'MIDDEL5FE' or f == 'MIDDEL 5FE':
   print('\033[46m'+'Middel 5FE\nType:GPU\nSeries:Middel\nArchitecture:EOX')
   print('Core Numb:1688\nMaximum Power:255w\nVRAM:8GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Apr 24.2020'+'\033[0m')
   continue
  if f == 'Middel 5L' or f == 'Middel5L' or f == 'MIDDEL 5L' or f == 'MIDDEL5L' or f == 'MIDDEL 5L' or f == 'middel 5l' or f == 'middel5l':
   print('\033[46m'+'Middel 5L\nType:GPU\nSeries:Middel\nArchitecture:EOX')
   print('Core Numb:1688\nMaximum Power:150w\nVRAM:5GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Jan 17.2020'+'\033[0m')
   continue
  if f == 'Top 3X' or f == 'Top3X' or f == 'TOP3X' or f == 'TOP 3X' or f == 'top3x' or f == 'top 3x' or f == 'top 3X' or f == 'top3X':
   print('\033[46m'+'Top 3X\nType:GPU\nSeries:Top\nArchitecture:EOX')
   print('Core Numb:2048\nMaximum Power:315w\nVRAM:14GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Fed 16.2020'+'\033[0m')
   continue
  if f == 'Top 3FE' or f == 'top 3fe' or f == 'Top3FE' or f =='TOP3FE' or f == 'TOP 3FE' or f == 'top3fe':
   print('\033[46m'+'Top 3FE\nType:GPU\nSeries:Top\nArchitecture:EOX')
   print('Core Numb:1992\nMaximum Power:300w\nVRAM:12GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Fed 16.2020'+'\033[0m')
   continue
  if f == 'list' or f == 'List' or f == 'LIST' or f == 'Help' or f == 'HELP' or f == 'help':
   time.sleep(2)
   print('\033[41m'+'https://amondbabaro.notion.site/H-O-S_NNDB-2311-23b176e4e98045b1864119ea5e5e4fd3?pvs=4'+'\033[0m')
   continue
  if f == 'under 5' or f == 'under5' or f == 'Under 5' or f == 'Under5' or f == 'UNDER5' or f == 'UNDER 5':
   print('\033[46m'+'Under 5\nType:GPU\nSeries:Under\nArchitecture:EOX')
   print('Core Numb:1022\nMaximum Power:185w\nVRAM:3GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Jan 3.2019'+'\033[0m')
   continue
  if f == 'Under 5X' or f == 'Under5X' or f == 'UNDER 5X' or f == 'UNDER5X' or f == 'under5x' or f == 'under 5x':
   print('\033[46m'+'Under 5X\nType:GPU\nSeries:Under\nArchitecture:EOX')
   print('Core Numb:1168\nMaximum Power:200w\nVRAM:4GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Jan 3.2019'+'\033[0m')
   continue
  if f == 'Middel 4' or f == 'Middel4' or f == 'middel 4' or f == 'middel4' or f == 'MIDDEL 4' or f == 'MIDDEL4':
   print('\033[46m'+'Middel 4\nType:GPU\nSeries:Middel\nArchitecture:EOX')
   print('Core Numb:1306\nMaximum Power:220w\nVRAM:5GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Jan 3.2019'+'\033[0m')
   continue
  if f == 'under 4' or f == 'under4' or f == 'Under 4' or f == 'Under4' or f == 'UNDER4' or f == 'UNDER 4':
   print('\033[46m'+'Under 4\nType:GPU\nSeries:Under\nArchitecture:EOX')
   print('Core Numb:998\nMaximum Power:160w\nVRAM:3GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:May 5.2018'+'\033[0m')
   continue
  if f == 'Middel 3' or f == 'Middel3' or f == 'middel3' or f == 'middel 3' or f == 'MIDDEL3' or f == 'MIDDEL 3':
   print('\033[46m'+'Middel 3\nType:GPU\nSeries:Middel\nArchitecture:EOX')
   print('Core Numb:1168\nMaximum Power:180w\nVRAM:4GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:May 5.2018'+'\033[0m')
   continue
  if f == 'Top 2' or f =='Top2' or f == 'top2' or f == 'top 2' or f == 'TOP2' or f == 'TOP 2':
   print('\033[46m'+'Top 2\nType:GPU\nSeries:Top\nArchitecture:Function')
   print('Core Numb:1346\nMaximum Power:250w\nVRAM:8GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Aug 8.2017'+'\033[0m') 
   continue
  if f == 'Middel 2' or f == 'Middel2' or f == 'MIDDEL2' or f == 'MIDDEL 2' or f == 'middel2' or f == 'middel 2':
   print('\033[46m'+'Middel 2\nType:GPU\nSeries:Middel\nArchitecture:Function')
   print('Core Numb:954\nMaximum Power:175w\nVRAM:3GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Aug 8.2017'+'\033[0m')
   continue
  if f == 'Under 3' or f == 'Under3' or f == 'under3' or f == 'under 3' or f == 'UNDER 3' or f == 'UNDER3':
   print('\033[46m'+'Under 3\nType:GPU\nSeries:Under\nArchitecture:Function')
   print('Core Numb:755\nMaximum Power:100w\nVRAM:2GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR6\nRelease:Aug 8.2017'+'\033[0m')
   continue
  if f == 'Middel1' or f == 'Middel 1' or f == 'middel 1' or f == 'middel1' or f == 'MIDDEL1' or f == 'MIDDEL 1':
   print('\033[46m'+'Middel 1\nType:GPU\nSeries:Middel\nArchitecture:Function')
   print('Core Numb:612\nMaximum Power:120w\nVRAM:2GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR5\nRelease:Apr 18.2016'+'\033[0m')
   continue
  if f == 'under 2' or f == 'under2' or f == 'UNDER2' or f == 'UNDER 2' or f == 'Under 2' or f == 'Under2':
   print('\033[46m'+'Under 2\nType:GPU\nSeries:Under\nArchitecture:Function')
   print('Core Numb:510\nMaximum Power:100w\nVRAM:1GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR5\nRelease:Apr 18.2016'+'\033[0m')
   continue
  if f == 'Under 1' or f == 'Under1' or f == 'UNDER1' or f == 'UNDER 1' or f == 'under1' or f == 'under 1':
   print('\033[46m'+'Under 1\nType:GPU\nSeries:Under\nArchitecture:Function')
   print('Core Numb:324\nMaximum Power:75w\nVRAM:512MB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR5\nRelease:Oct 30.2015'+'\033[0m')
   continue
  if f == 'top1' or f == 'Top1' or f == 'TOP1' or f == 'top 1' or f == 'Top 1' or f == 'TOP 1':
   print('\033[46m'+'Top 1\nType:GPU\nSeries:Top\nArchitecture:Function')
   print('Core Numb:888\nMaximum Power:125w\nVRAM:4GB')
   print('Connection:PCIe 3.0 16x\nPCI Slot:2\nMemory Type:GDDR5\nRelease:Oct 30.2015'+'\033[0m')
   continue 
  if f == 'stop' or f == 'STOP' or f == 'reboot' or f=='quit' or f=='QUIT':
   print(quit())
  else:
   print('\033[41m'+'error:Please check the search word'+'\033[0m')
   time.sleep(1)
   reset
   continue