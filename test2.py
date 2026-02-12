#Escribir y leer testfile1.txt 

a = input()

if a=="1":
    temp = input("Ingrese su nombre!")
    try:
        with open('testfile1.txt','w') as testfile:
            testfile.write(temp)
    except Exception as e:
        print("Problema!!", str(e))
else:
    try:
        with open('testfile1.txt','r') as testfile:
            print(testfile.read())
    except Exception as e:
        print("Problema!!", str(e))