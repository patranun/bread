list1 =[]
def showbill():
    print("-----Kai FoOD-----")
    for number in range(len(list1)):
        print(list1[number][0])
        print(list1[number][1])
while True:
    menuname = input('pls enter menu')
    if(menuname.lower() == 'exit'):
        break
    else:
        menuprice = input('price')
        list1.append([menuname,menuprice])
print(list1)
showbill()

