def main():
    #escribe tu código abajo de esta línea
    SMA= float(input("Dame el saldo del mes anterior: "))
    IN=  float(input("Dame los ingresos: "))
    EG=  float(input("Dame los egresos: "))
    NC=  float(input("Dame el número de cheques: "))
    prom = float((SMA + IN - EG ) - (NC * 13))
    prom = prom * .925
    print("El saldo final de la cuenta es: " + str(prom))



if __name__ == '__main__':
    main()
