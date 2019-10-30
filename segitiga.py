a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if (a<=0 or b <=0 or c<=0):
    print("segitiga tidak dapat dibangun")

elif(a>= b+c or b>=c+a or c>=a+b):
    print ("segitiga tidak dapat dibangun")

elif (a==b or b==c ):
    print("segitiga sama sisi")

elif(a==b==c):
    print("segitiga sama kaki")

elif (a>b and c) or (b>a and c) or (c>b and a):
    print ("segitiga siku siku")

elif ( a or b or c== float>0.01):
    print ("selisih panjang sisi sisinya tidak lebih dari 1%")

elif ( a or b or c== float >= 0.01):
    print("Selisih lebih dari 1% dianggap beda")

elif ( a or b or c== float <= 0.01):
    print("Selisih 1% atau kurang dianggap sama")

else:
    print("segitiga bebas")




