def main():
    from math import sqrt
    import math
    oper1 = round ((2*(3/4) + 4 * (2/3) - (3* (1/5)) + 5 * (1/2)),4)
    print (str(oper1))
    oper2 = round (2 * math.sqrt( pow(35,2)) + 4 * math.sqrt( pow(36,3)) - 6 * math.sqrt( pow(49,2)),4)
    print (str(oper2))

    a = 4
    b = 5

    oper3 = round(math.pow(a,3) + (2 * (math.pow(b,2)))) / (4 * (a) )
    print (str(oper3))
    oper4 = (2*(math.pow(a+b, 2)) + 4*(math.pow(a-b, 2))) / (a*math.pow(b,2))
    print (str(oper4))
    oper5 = round((math.sqrt((math.pow(a+b, 2))+(math.pow(2,a+b)))) / (math.pow((2*a + 2*b), 2)), 4)
    print (str(oper5))
    
   



if __name__ == '__main__':
    main()
