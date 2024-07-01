import os
os.system('cls')
#****************************

lstSt=[]
nameS=input('type her name: ')
lstSt.append(nameS)
while True:
    for i in lstSt:
        print(i)
    ask=input('do you want add or remove?(yes/no)  ')
    if ask=='yes':
        ask2=input('remove or add name? ')
        if ask2=='add':
            nameS=input('type her name: ')
            lstSt.append(nameS)
            if ask2=='remove':
                nameR=input('what do yo want remove?type her name ')
                for i in lstSt:
                    if i==nameR:
                        lstSt.remove(nameR)
                print('Done')
    elif ask=='no':
        ask3=input('do yo want see list?(yes or no)? ')
        if ask3=='yes':
            print(*lstSt)
            if ask3=='no':
               break


    
