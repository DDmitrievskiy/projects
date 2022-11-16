#Создайте программу для расчёта банковского вклада на заданный срок. 
#клад без ежемесячного пополнения, но с ежемесячным начислением процентов и капитализацией (начислением процентов на проценты). 
#Результат сохраните в файле output.csv.

# Формат ввода amount - целое число, равное сумме вклада; period - целое число, равное сроку (в годах) вклада;
# rate - число, равное процентной ставке вклада

numbers = input().split()

total = int(numbers[0])
years = int(numbers[1])
months = years * 12
interest_rate = float(numbers[2])


counter = 1

csv_filename = 'output.csv'
with open(csv_filename, 'w') as csv_file:
  labels = ["Месяц", "Сумма на вкладе", "Начисление"]
  print(*labels, sep=',', file=csv_file)

  while months > 0:
    months -= 1
    prozent = (interest_rate / 12.0 / 100.0) * total
    total = total + prozent
    print(counter,f'{total:0.2f}', f'{prozent:0.2f}', sep =',', file=csv_file)
    counter += 1
