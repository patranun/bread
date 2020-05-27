User = input("username: ")
Password = input("password: ")
if User == "bread" and Password == "1234" :
    print("Done")
    print("----Welcome to Bread shop :D----")
    print("-----Product List-----")
    print("type product price")
    print("   1 banana 10 THB")
    print("   2 apple  12 THB")
    select = int(input("-----Please choose a product: D-----"))
    if select == 1:
        amount = int(input("Amount?"))
        x = 10 * amount
        print(x)
    elif select == 2:
        amount = int(input("Amount?"))
        y = 12 * amount
        print(y)
select = int(input("-----Please choose a product: D-----"))
if select == 1 :
    amount = int(input("Amount?"))
    x = 10 * amount
    print(x)
elif select == 2 :
    amount = int(input("Amount?"))
    y = 12 * amount
    print(y)