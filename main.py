def es_armstrong(numero):
    numero_texto = str(numero)
    cantidad_digitos = len(numero_texto)
    
    suma = 0
    
    for digito_texto in numero_texto:
        
        digito = int(digito_texto)
        
        suma = suma + digito ** cantidad_digitos
        
    if suma == numero:
        return True
    else:
        return False
    
print("Confirma si tu número es Armstrong")
print()

user_input = int(input("Ingresa un número entero positivo: "))

if es_armstrong(user_input):
    print(f"\nEl número {user_input} es un número Armstrong")
else:
    print(f"\nEl número {user_input} lamentablemente NO lo es.")