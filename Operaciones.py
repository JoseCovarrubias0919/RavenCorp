def Suma_Bin (self, numeros):
    x = 0
    while (numeros.Len() != x):
        numero1 = numeros[x]
        numero2 = numeros[x+1]
        x = x+2
        z = 0
        numeroNuevo = []
        while (numero1.Len() != z or numero2.Len() != z):
            a = numero1[z]
            b = numero2[z]
            r = SumNumBin(self, a, b)
            if r == "10":
                numeroNuevo.append("0")
                g = "1"
            if g == "1":
                n = SumNumBin(self, g, r)


            
    return 0

def SumNumBin (self, a, b):
    if a == "1" and b == "0":
        return "1"
    elif a == "0" and b == "1":
        return "1"
    elif a == "1" and b == "1":
        return "10"
    elif a == "0" and b == "0":
        return "0"
    return "0"