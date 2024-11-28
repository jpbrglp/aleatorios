import random
num = random.randint(1,100)
nu = random.randint(1,100)
n = random.randint(1,100)
lista = (num, nu, n)
print(lista)
t1 = int(input("digite um número que vc acha que está na lista: "))
t2 = int(input("Digite o segundo número: "))
t3 = int(input("digite o último número que vc acha que está na lista: "))
while t1 != num and t2 != nu and t3 != n:
    print("Vc errou todos o números, tente novamente")
    t1 = int(input("digite um número que vc acha que está na lista: "))
    t2 = int(input("Digite o segundo número: "))
    t3 = int(input("digite o último número que vc acha que está na lista: "))
    if t1 == num and t2 != nu and t3 != n:
        print(f"Vc acertou o primeiro número, mas não acertou o resto {num}")
    elif t1 == num and t2 == nu and t3 != n:
        print(f"Vc acertou dois números, mas errou o último{num, nu}")
    elif t1 == num and t2 == nu and t3 == n:
        print(f"Vc acertou todos os números, parabéns!!!{num, nu,n}")    
    elif t1 != num and t2 == nu and t3 != n:
        print(f"Vc acertou apenas o egndo item {nu}")
    elif t1 != num and t2 != nu and t3 == n:
        print(f"Vc acertou apena o terceiro {n}")
    elif t1 == num and t2 != nu and t3 == n:
        print(f"Vc acertou o primero e o último número{num, n}")
    elif t1 != num and t2 == nu and t3 == n:
        print(f"Vc errou apenas o primeiro número {nu, n}")