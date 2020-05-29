def showbill():
    totalprice = 0
    print("-----Kai FoOD-----")
    for number in range(len(list1)):
        print(list1[number],pricelist[number])
        totalprice += int(pricelist[number])
        print('turtle:',totalprice)

list1 =[]
pricelist = []
while True:
    menuname = input('pls enter menu')
    if(menuname.lower() == 'exit'):
        break
    else:
        menuprice = input('price')
        list1.append(menuname)
        pricelist.append(menuprice)
print(list1,pricelist)
showbill()

