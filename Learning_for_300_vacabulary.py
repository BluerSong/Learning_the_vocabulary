import time
r = 0
w = 0
k = int(input("input the start number in the list:"))
p = int(input("input the end number in the list:"))
p = p+1
f = []
file = open('1.txt','r',encoding='utf-8')
file = file.readlines()
file2 = open('2.txt','r',encoding='utf-8')
file2 = file2.readlines()
while k<p:
    i = file2[k-1]
    answer = input(i+"please input the phrase>>>")
    answer = answer.split()
    f1 = file[k-1]
    if answer == f1.split():
        print("Good!")
        k += 1
        r += 1
    else:
        print("Wrong,the answer is ",file[k-1])
        print(file[k-1])
        k += 1
        w += 1
print("totally ",r,"correct words and ",w,"wrong words")





