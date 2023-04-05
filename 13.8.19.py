ticket = int(input("Сколько билетов хотите приобрести?"))
sum_price = 0
for i in range(1,ticket + 1):
    age = int(input("Сколько лет посетителю?"))
    if age < 18:
        sum_price += 0
    elif 18 <= age <= 25:
        sum_price += 990
    else:
        sum_price += 1390
if ticket > 3:
    print(sum_price * 0.9)
else:
    print(sum_price)