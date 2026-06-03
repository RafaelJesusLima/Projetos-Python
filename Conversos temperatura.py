# Fazer um conversor de Celsius pra fahrenheit

def main():
    print("========== Temperatura Converter ==========")

    while True:
        Convertor = str(input("Qual temperatura converter? (Celsius/Fahrenheit) ou 'sair': "))

        if Convertor.lower() == "sair":
            print("👋 Até mais!")
            break

        print("==========Tipo==========")

        if Convertor == "Celsius":
            Celsius = float(input("Quantos Graus Celsius: "))
            Fahrenheit = (Celsius * 9/5) + 32
            print(f"{Celsius}°C equivale a {Fahrenheit:.1f}°F")

        elif Convertor == "Fahrenheit":
            Fahrenheit = float(input("Quantos Graus Fahrenheit: "))
            Celsius = (Fahrenheit - 32) * 5/9
            print(f"{Fahrenheit}°F equivale a {Celsius:.1f}°C")

        else:
            print("Opção invalida! Digite 'Celsius' ou 'Fahrenheit'.")

if __name__ == "__main__":
    main()