# программа считает стоимость билетов
total_coast_of_tickets = 0
amount_tickets = int(input("введите количество билетов: "))

for i in range(amount_tickets): #цикл для считывания возраста покупателей билетов и предварительного подсчета стоимости билетов
  print("введите возраст для" + str(i+1) + "-го покупателя билетов")
  ages = int(input())
  if ages < 18: 
    total_coast_of_tickets += 0    
  
  elif ages in range(18, 25): 
    total_coast_of_tickets += 990

  else:
    total_coast_of_tickets += 1390
print(total_coast_of_tickets)
# Обработака скидки и вывод окончательной суммы
print("~~~~~~~~~~~~~~~~~~~~~~")
print("Сумма для оплаты")
if amount_tickets > 3:
  print(total_coast_of_tickets*0.9)
else:
  print(total_coast_of_tickets)
print("~~~~~~~~~~~~~~~~~~~~~~")