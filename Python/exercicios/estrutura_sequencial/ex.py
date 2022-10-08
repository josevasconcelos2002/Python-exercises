menu=True
while menu:
    print ("""
    1.Hello World!
    2.Informações da Memoria
    3.Informações da Rede
    4.Conexões Estabelecidas TCP
    5.Usuários
    6.Espaço livre no HDD
    7.Hora atual
    8.Registrar essas informações em um arquivo
    """)
    menu=input("Ecolha uma opção? ")
    if menu=="1":
        # exercicio 1
        print("Hello World!\n")
    elif menu=="2":
        print(os.system("cat /proc/meminfo"))
    elif menu=="3":
        print(os.system ("ifconfig"))
    elif menu == "4":
        print (os.system ("netstat -na | grep tcp"))
    elif menu == "5":
        print (os.system ("users"))
    elif menu == "6":
        print (os.system ("df -l"))
    elif menu == "7":
        print (os.system ("date +%c"))
    elif menu == "8":
        print (os.system ("ls - al > arquivo.txt"))
    elif menu !="":
      print("\n Opção Invalida. Tente Novamente")




# exercicio 1
print("Hello World!\n")

# exercicio 2
n = input("Introduza um número: ")
print("O número introduzido foi:",n)

# exercicio 3
print("Introduza os valores de a e b.")
a = input("a=")
b = input("b=")
c = int(a) + int(b)
print("A soma entre a e b é:",c)