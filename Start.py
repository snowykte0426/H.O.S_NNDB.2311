# -*- coding: utf-8 -*-
# main.py
from os import system
system("title "+"H.O.S_NNDB_2311 v1.3.1")
import time
print('\033[92m'+'H.O.S NNDB.2311'+'\033[0m')
time.sleep(0.5)
class boot:
 kk = '1'
 while(kk == '1'):
  parttype = None
  parttype = input('Enter the type of part to search for(CPU\VGA\M/B or list,updata,utilrity)\n')
  pt = parttype
  if parttype == 'GPU' or parttype == 'gpu' or parttype == 'graphic card' or parttype == 'Graphic Card' or parttype == 'graphic_card' or parttype == 'Graphic_Card' or pt == 'VGA' or pt == 'GPGPU' or pt == 'GP GPU' or pt == 'gpgpu':
   #↑GPU(VGA)_DB 호출
   from DataBase_GPU import DB_GPU
  if parttype == 'CPU' or parttype == 'cpu':#CPU_DB 호출
   from DataBase_CPU import DB_CPU
  if parttype == 'Mainbord' or parttype == 'mainbord' or parttype == 'MAINBORD' or parttype == 'motherbord' or pt == 'Motherbord' or pt == 'MOTHERBORD' or pt == 'm/b'or pt == 'M/B':
   #↑Mainbord(Mother bord)_DB 호출
   from DataBase_Mainbord import DB_MAINBORD
  if parttype == 'Updata' or parttype == 'updata' or parttype == 'UPDATA' or pt == 'update' or pt == 'UPDATE' or pt == 'Update':#업데이트 패키지 호출
   time.sleep(0.3)
   from Updata_tool import updata
  if parttype == 'Ut' or parttype == 'ut' or pt == 'utilrity':#더미데이터
   from utilrity import hiden
  if pt == 'list' or pt == 'List' or pt == 'LIST' or pt == 'Help' or pt == 'HELP' or pt == 'help':#노션 부품 구현 리스트 링크 호출
   time.sleep(2)
   print('\033[41m'+'https://amondbabaro.notion.site/H-O-S_NNDB-2311-23b176e4e98045b1864119ea5e5e4fd3?pvs=4'+'\033[0m')
   time.sleep(1)
   continue
  if pt == 'Beta' or pt == 'beta' or pt == 'BETA':#(사실상)더미데이터
   pt = 0
   print('Checking beta version in progress...',end='')                                                    #여기부터
   time.sleep(5)
   import os, time
   os.system('cls')
   print('\r\033[41m'+'No beta tests confirmed\nBack to the original screen'+'\033[0m',end="")             #여기까지_더미데이터
   os.system('cls')#출력기록 지우기
   print('\r\033[41m'+'No beta tests confirmed\nBack to the original screen'+'\033[0m',end="") 
   time.sleep(3)
   print('\n')
   continue
  if pt == 'quit' or pt == 'QUIT' or pt == 'stop' or pt == 'STOP':
   time.sleep(1)
   print(quit())
  if pt == 'app_data' or pt == 'appdata' or pt == 'APPDATA' or pt == 'APP_DATA':
   time.sleep(1)
   from app_data import 골리앗
  if pt == 'Manager' or pt == 'manager' or pt == '관리자' or pt == '매니저' or pt == 'serise' or pt == 'Serise' or pt == 'SERISE' or pt == '제품군' or pt == '시리즈':
   time.sleep(2)
   from Untitled_1 import partserise
  if pt == '멈춰!':
   time.sleep(3)
   from user_inter import Ui_Form
  else:
   print('\033[41m'+'error:Please check the command again')#error
   time.sleep(1)
   print('fatal error: Recover and initialize the program to a recovery point'+'\033[0m')#reset
   time.sleep(2)
   continue
class close:#프로그램 재시작
 close_number='4'
 while(close_number=='4',close_number==5,close_number=='6'):
  kk = str(4)
  kk = None
  from Start import boot
class reboot:#프로그램 재시작
 def restart():
  import os
  import sys
  sys.stdout.flush()
  sys.flush()
  os.execv(sys.argv[0], sys.argv)
 restart()
 print(quit())

 