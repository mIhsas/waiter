from datetime import datetime, timedelta
from os import system
import time
from waiter.wait_dataclass import wait_obj
class Wait:
  def __init__(
      self,
      start:datetime|None=None,
      end:datetime|None=None,
      name:str|None=None,
      description:str|None=None,
      uid:int|float|str|None=None,
      *,
      waitwat: wait_obj|None=None
  ) -> None:
    if waitwat != None:
      self.waitObj:wait_obj=waitwat
    elif waitwat==None:
      if uid==None: uid=hex(int(time.time()))

      assert start!=None, "start не може бути нан"
      assert end!=None, "end не може бути нан"

      self.waitObj:wait_obj=wait_obj(start,end,name,description,uid)  
  
  @property
  def max(self):
    return self.waitObj.end-self.waitObj.start
  
  @property
  def delta(self):
    return datetime.now()-self.waitObj.start

  @property
  def widsotok(self):
    return self.delta/(self.one_procent)
  
  @property
  def one_procent(self):
    return self.max/100
  
  @property
  def left(self):
    return self.max-self.delta
  
  @property
  def widsotka(self):
    return self.custom_widsotka()

  def custom_widsotka(self,pointi:int=100):
    score_d5 = int(round(self.delta/(self.max/pointi), 0))
    out = ""
    for i in range(pointi):
      if score_d5 > 0: out+="|"; score_d5-=1
      else: out+="."
    return out

  def __format_dt(self, dt):
    if type(dt) == timedelta:
      return str(dt).split(".")[0]
    return dt.strftime("%d.%m.%Y %H:%M:%S")
  
  def play(self,interval=0.5):
    while True:
      TO_NEXT_PROCENT=self.__format_dt(self.one_procent-(self.delta%self.one_procent))
      system("cls")
      print(f"{'Назва' if self.waitObj.name is not None else 'юайді'} очікувача: {self.waitObj.name if self.waitObj.name is not None else self.waitObj.uid}")
      print(f"Опис: {self.waitObj.description if self.waitObj.description is not None else 'нема опису'}\n")
      print("Сьогодні:",self.__format_dt(datetime.now()),"\n")
      print("Пройшло:",self.__format_dt(self.delta))
      print("Лишилося:", self.__format_dt(self.left),"\n\n")
      print(round(self.widsotok, 2),"%")
      print(self.widsotka)
      print("*до кінця відсотка лишилося:",TO_NEXT_PROCENT)
      time.sleep(interval)

  def __repr__(self) -> str:
    return f"""wait.{self.waitObj.name if self.waitObj.name is not None else self.waitObj.uid}:
  description: {self.waitObj.description}
  from:        {self.waitObj.start}
  to:          {self.waitObj.end}
  length:      {self.max}
  delta:       {self.delta}
  done:        {self.widsotok}%
  uid:         {self.waitObj.uid}"""
    # return f"wait.{self.waitObj.name if self.waitObj.name is not None else self.waitObj.uid}: {self.waitObj.start}-{self.waitObj.end} {'description: '+self.waitObj.description if self.waitObj.description is not None else ''}"