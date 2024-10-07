numero1 = int(input("Número 1: "))  
numero2 = int(input("Número 2: "))  
numero3 = int(input("Número 3: "))  
numero4 = int(input("Número 4: "))  
numero5 = int(input("Número 5: ")) 
numero6 = int(input("Número 6: "))

def somador(n1, n2, n3, n4, n5, n6):
    soma = n1 + n2 + n3 + n4 + n5 + n6
    return soma

resultado = somador(numero1, numero2, numero3, numero4, numero5, numero6)
print(resultado)