a = int(input("Вартість однієї ігрової приставки: "))
b = int(input("Введіть кількість: "))
c = int(input("Відсоток знижки: "))
operation = input("Введіть  'zaglna summa' або 'vartist pristavki':")

if operation == 'zagalna summa':
    result = (a-a/100*c)*b
    print("Загальна сума:", result)
elif operation == 'vartist pristavki':
    result = (a-a/100*c)
    print("Вартість однієї приставки:", result)



