def main():
    # Inicializamos la variable para almacenar la suma total
    total_dinero = 0

    # Contador de personas
    contador_personas = 0

    
    while contador_personas < 10:
        try:
            dinero_persona = float(input(f"Ingrese el dinero invertido por la persona {contador_personas + 1}: "))
            if dinero_persona == 0:
                print("Ya no quedan boletos, vuelva más tarde")
                break
            elif dinero_persona < 0:
                print("Por favor, ingrese una cantidad válida (mayor o igual a 0).")
            else:
                total_dinero += dinero_persona
                contador_personas += 1
        except ValueError:
            print("Por favor, ingrese una cantidad válida (número positivo).")

    # la suma total 
    print(f"La suma total de dinero recolectado es: ${total_dinero:.2f}")

if __name__ == "__main__":
    main()
