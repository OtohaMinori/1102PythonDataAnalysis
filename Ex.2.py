'''
Date:2022.03.03
Name:友人Ｓ☄
SID:B10813180
Title:Ex.2
'''
import os
def clear(): return os.system('cls')

'''
Q1.
How to show six number?
顯示6個數值=> 0 1 2 3 4 5
'''
for num in range(0, 6, 1):
    print(num)
input("Press Enter to continue...")
'''
Q2.
Input a number and then show the front number.
輸入任意1個數，顯示之前的所有數字(例如輸入8)
'''
clear()
target = int(input("Input a number："))
count = 1
for num in range(1, target+1, 1):
    if ((count - 20) < 0):
        if (count == 1):
            print(str(count)+"st is "+str(num))
        elif(count == 2):
            print(str(count)+"nd is "+str(num))
        elif(count == 3):
            print(str(count)+"rd is "+str(num))
        else:
            print(str(count)+"th is "+str(num))
    else:
        if((count % 10) == 1):
            print(str(count)+"st is "+str(num))
        elif((count % 10) == 2):
            print(str(count)+"nd is "+str(num))
        elif((count % 10) == 3):
            print(str(count)+"rd is "+str(num))
        else:
            print(str(count)+"th is "+str(num))
    count += 1
input("Press Enter to continue...")
'''
Q3.
輸入任意1個數，顯示間隔的數字(例如輸入8)
'''
clear()
target = int(input("Input a number："))
count = 1
for num in range(1, target+1, 2):
    if ((count - 20) < 0):
        if (count == 1):
            print(str(count)+"st is "+str(num))
        elif(count == 2):
            print(str(count)+"nd is "+str(num))
        elif(count == 3):
            print(str(count)+"rd is "+str(num))
        else:
            print(str(count)+"th is "+str(num))
    else:
        if((count % 10) == 1):
            print(str(count)+"st is "+str(num))
        elif((count % 10) == 2):
            print(str(count)+"nd is "+str(num))
        elif((count % 10) == 3):
            print(str(count)+"rd is "+str(num))
        else:
            print(str(count)+"th is "+str(num))
    count += 1
