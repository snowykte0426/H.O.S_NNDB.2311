# -*- coding: utf-8 -*-
class partserise:
 import time,math
 print('This is the administrator is area. Please enter the administrator is password')
 password = input('')
 time.sleep(3)
 if password == 'noa4044@' or password == 'jjab4044@' or password == 'snowyingkte0426' or password == 'snowyingkte0426*' or password == 'Snowyingkte0426*' or password == '20170723':
  c1 = int(452.2)
  def reset():
   keyword = None
   parttype = None
   find = None
   f = None
   return keyword,find,f,parttype
  while (c1 == int(452.2)):
   #CPU,GPU등 부품 파일 참조하며 제작하도록
   print('\033[0m'+'Enter the product line you want to look up')
   time.sleep(1)
   ser_find = input('')
   time.sleep(0.8)
   f = ser_find
   if f == 'A3 5000' or f == 'A35000' or f == 'a35000' or f == 'a3 5000':
    print('A3아키텍쳐를 활용한 H.O.S의 2번째 CPU 제품군으로,A3 4000의 후속작이다.\nA3아키텍쳐에서 TML8 0.7nm공정을 적용한 A3R아키텍쳐를 사용한다.\nA3 5000은 대부분 0.7nm공정을 최초로 사용하였으며 RSoC(Restrictive System on Chip,제한적 통합 시스템)을 대폭 강화하였다',end=" ")
    print('또한,가상화 코어가 본격적으로 적용된 CPU세대이며 새로운 HC4소켓을 사용해 이론상 최대 400000MHz의 클럭과 550w의 전력전송이 가능해졌다.히트스프레드에 온도센서와 압력감지센서가 삽입되어',end=" ")
    print('CPU솔더링은 불가능 해졌지만 더 정확한 전력공급 및 온도제어,자가진단이 가능해졌다.전작인 A3 4000에 비해 모든 제품이 동급 전작제품 대비 평균 20%의 성능 향상을 이뤘다.\n')
    continue
   if f == 'A3 4000' or f == 'A34000' or f == 'a34000' or f == 'a3 4000':
    print('A3아키텍쳐를 활용한 첫번쨰 CPU 제품군이다.A3아키텍쳐는 전세대 A2아키텍쳐보다 효율적으로 전력을 사용함과 동시에 전력 최대 사용량역시 증가해 전작대비 전력 당 성능비는 상승하였지만',end=" ")
    print('더 많은 전력을 사용하는것이 특징이다.전력사용이 높아짐에 따라 클럭이 상승하였고 HC3소켓의 임계치까지 활용한다.가상화 코어가 시범적으로 적용되 가상화 프로그램을 연산하는데 적용된 세계 최초의 프로세서이다.',end=" ")
    print('전작대비 모든 제품이 평균 14% 성능향상을 이뤘다.\n')
    continue
   if f == 'A2 3000' or f == 'A23000' or f == 'a2 3000' or f == 'a23000':
    print('A2아키텍쳐를 활용한 2번째 H.O.S의 일반 소비자용 프로세서 제품군이다.전작의 A2아키텍쳐와 달라진 점은 JGL,일명 점핑연산방식 이라는 별칭으로 불리는',end=" ")
    print('기술이 좀더 강화된 형태로 적용되었다.하지만 그외엔 클럭을 높이고 전력사용량을 스윗스팟을 아득히 넘길정도로 설정해서 발열문제가 심각했다.',end=" ")
    print('전작 A2 2000번대 CPU들 대비 모든 제품이 5%의 성능향상을 이뤘다.\n')
    continue  
   else:
     time.sleep(2)
     print('\033[41m'+'The command was entered incorrectly.Error not allowed in administrator mode!'+'\033[0m')
     time.sleep(1.2)
     from Start import reboot
 else:
  time.sleep(2)
  print('\033[41m'+'Inaccessible, administrator authentication failed, exit program'+'\033[0m')