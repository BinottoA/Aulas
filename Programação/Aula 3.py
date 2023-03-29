print ("""Aqui vai algumas instruções""")



print ("+ para adição")
print ("- para subtração")
print ("* para multiplicação")
print ("/ para divisão")
print ("p2 para ao quadrado")
print ("p para potenciação")
print ("r para raiz quadrada")
print ("n para notação científica")
print ("Você deve escrever o primeiro número, dar ENTER")
print ("Escrever a operação, dar ENTER")
print ("Por fim, o segundo número e dar ENTER")
print ("No caso de p2 e r, não tem segundo número")

a=float(input())        

c=input()

c=c.lower()

if c=="r":
    print(a**0.5)
    quit()

if c=="p2":
    print (a**2)
    quit()

b=float(input())           



if c=="+":                 
    print(a+b) 

elif c=="-": 
    print(a-b)

elif c=="*": 
    print(a*b)

elif c=="/": 
    print(a/b)

elif c=="p":
    print(a**b)

elif c=="n":
    print(a*(10**b))

