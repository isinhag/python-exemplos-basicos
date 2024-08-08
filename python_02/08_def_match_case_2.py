sabor = int(input("Indique o sabor desejado: "))

# Função fim de semana 
def sabor_pizza(sabor):
    match sabor:
        case 1: 
            return("Mussarela")
        case 2: 
            print("Calabresa")
        case 3: 
            print("Frango c/ catupiry")
        case 4: 
            print("Portuguesa")
        case _: 
            print("Sabor inválido!")

# Exibe o resultado
sabor_pizza(sabor)
