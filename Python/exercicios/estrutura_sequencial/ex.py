import os

# exercicio 1
def hello():
    print("Hello World!\n")   
# exercicio 2
def numero():
   n = input("Introduza um número: ")
   print("O número introduzido foi:",n) 
# exercicio 3
def soma():
    print("Introduza os valores de a e b.")
    a = input("a=")
    b = input("b=")
    c = int(a) + int(b)
    print("A soma entre a e b é:",c)

menu=True
while (menu!=19):
    print ("""
    1.Hello World!
    2.Número
    3.Soma de 2 nrs
    4.Conexões Estabelecidas TCP
    5.Usuários
    6.Espaço livre no HDD
    7.Hora atual
    8.Registrar essas informações em um arquivo
    9.Hora atual
    10.Hora atual
    11.Hora atual
    12.Hora atual
    13.Hora atual
    14.Hora atual
    15.Hora atual
    16.Hora atual
    17.Hora atual
    18.Hora atual
    19.Exit
    """)
    menu=input("Ecolha uma opção? ")
    if menu=="1":
        # exercicio 1
        hello();
    elif menu=="2":
        # exercicio 2
        numero();
    elif menu=="3":
        # exercicio 3
        soma();
    #elif menu == "4":
        # exercicio 4
        #print (os.system ("netstat -na | grep tcp"))
    #elif menu == "5":
        # exercicio 5
        #print (os.system ("users"))
    #elif menu == "6":
        # exercicio 6
        #print (os.system ("df -l"))
    #elif menu == "7":
        # exercicio 7
        #print (os.system ("date +%c"))
    #elif menu == "8":
        # exercicio 8
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "9":
        # exercicio 9
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "10":
        # exercicio 10
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "11":
        # exercicio 11
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "12":
        # exercicio 12
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "13":
        # exercicio 13
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "14":
        # exercicio 14
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "15":
        # exercicio 15
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "16":
        # exercicio 16
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "17":
        # exercicio 17
        #print (os.system ("ls - al > arquivo.txt"))
    #elif menu == "18":
        # exercicio 18
        #print (os.system ("ls - al > arquivo.txt"))
    elif menu == "19":
        # Exit
        exit();
    elif menu !="":
      print("\n Opção Invalida. Tente Novamente\n")