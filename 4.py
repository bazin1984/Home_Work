# Определить,является ли год високосным.
year = int(input("Введите год , который требуется определить"))
if year % 4 ==0 and year % 100 != 0 :
    print("год високосный")
elif year % 400 == 0 :
    print("Год является високосным")
else:
    print("Год не является високосным")
