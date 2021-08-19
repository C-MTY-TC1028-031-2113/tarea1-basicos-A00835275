def main():
    #escribe tu código abajo de esta línea
    PI= float(input("Dame el peso inicial: "))
    PF= float(input("Dame el peso final: "))
    CM= float(input("Dame la cantidad de meses: "))
    prom = float(PI - PF)/ CM 
    print("Lo que debes bajar por mes es: " + str(prom)) 



if __name__ == '__main__':
    main()
