def main():
    print("===========Calculadora=============")

    while True:
        Calcular = str(input("Qual tipo de Calculo? Soma/Divisão/Subtração/Multiplicação: "))
        #Escolher o tipo
        if Calcular == "Soma":
            Numero1 = float(input("[1]: "))
            Numero2 = float(input("[2]: "))
            Soma = Numero1 + Numero2
            print("Resultado:", Soma)
        #Divisão
        elif Calcular == "Divisão":
            Numero1 = float(input("[1]: "))
            Numero2 = float(input("[2]: "))
            Divisão = Numero1 / Numero2
            print("Resultado:", Divisão)
        #Subtração
        elif Calcular == "Subtração":
            Numero1 = float(input("[1]: "))
            Numero2 = float(input("[2]: "))
            Subtração = Numero1 - Numero2
            print("Resultado", Subtração)
        #Multiplicação
        elif Calcular == "Multiplicação":
            Numero1 = float(input("[1]: "))
            Numero2 = float(input("[2]: "))
            Multiplicação = Numero1 * Numero2
            print("Resultado:", Multiplicação)
if __name__ == "__main__":
    main()

