from datetime import datetime
from os import system
from time import sleep

def widsotka(max: float|int,score: float|int, pointi: int):
  score_d5 = int(round(score/(max/pointi), 0))
  widsotk=score_d5-0
  out = ""
  for i in range(pointi):
    if score_d5 > 0: out+="|"; score_d5-=1
    else: out+="."
  return f"{widsotk}%\n{out}"

START=datetime.strptime("2023-12-26 17:08", "%Y-%m-%d %H:%M")
END=datetime.strptime("2024-01-6 8:00", "%Y-%m-%d %H:%M")
MAX=END-START
ONE_PROCENT=MAX/100
while True:
  NEED_WAIT=END-datetime.now()
  ALREDY_WAIT=datetime.now()-START
  TO_NEXT_PROCENT=ONE_PROCENT - (ALREDY_WAIT % ONE_PROCENT)
  system("cls")
  print("Сьогодні:",datetime.now(),"\n")
  print("прочекав:",ALREDY_WAIT)
  print("ще треба чекати:", NEED_WAIT,"\n\n")
  print(widsotka(MAX, ALREDY_WAIT, 100))
  print("до кінця відсотка лишилося:",TO_NEXT_PROCENT)
  sleep(0.1)