from datetime import datetime
from collections import Counter

clients ={
'Попова':['Депеляция', '1000',  '29.04.2020'],
'Степанова':['Стрижка', '500','22.05.2020'],
'Амелина':['Покраска',  '1500','10.05.2020'],
'Щеглова':['Стрижка',  '1500','13.05.2020']}

print(clients)
print("Добавление клиента:")
new_clients = (input("Введите фамилию? "))
slovar=[(input("Услуга? ")),(input("Стоимость услуги? ")),(input("Дата? "))]
upgrade={new_clients:slovar}
clients.update(upgrade)
print(clients)
 
def del_client():
   
 print(clients)
print("Удаление клиента")
Name = input("Фамилия? ")
clients.pop(Name)
print(clients)
print('\n') 
def add_element():
    
 print(clients) 
print("Добавление элемента")
Name = input("Фамилия? ")
Service = input("Услуга? ")
Price = input("Стоимость? ")
Date= input("Дата? ")
clients[Name].append({'Услуга': Service, 'Стоимость': Price, 'Дата': Date})
print(clients)
    
def sum_price():
    
 print(clients)
print("Сумма потраченных денег")
Name = input("Фамилия? ")
sum=0
for i in range(len(d[Name])):
 sum=sum+d[Name][i]['Стоимость']
print(sum)

def client_find():

 print(clients)
print("Самый частый клиент")
Name = ["Щеглова", "Амелина"]
number = 0
for i in range(len(d)): 
    if len(d[Name[i]]) > number:
            number = len(d[Name[i]])
            Name_Find = Name[i]
    print(Name_Find)

def client_rich():
    Name = ["Щеглова", "Амелина"]
    n=0
    sum=0
    for i in range(len(d)):
        for j in range(len(d[Name[i]])):
            sum=sum+d[Name[i]][j]['Стоимость']
        if sum>n:
            n=sum
            rich=Name[i]
    print(rich)
    