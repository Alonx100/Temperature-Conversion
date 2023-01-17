#TemperatureConversion Made by Alon Rehin for CIS 261

def ConFar():

    for FarTemp in range(0,212,40):
        CelcTemp = (FarTemp-32)*5/9
        print(FarTemp, "Fahrenheit = ", round(CelcTemp, 2), "Celsius\n")
   #print(CelcTemp)
    
ConFar()

def ConCel():

    for CelTemp in range(0,100,20):
        FarTemp = CelTemp*9/5+32
        print(CelTemp, "Celsius = ", round(FarTemp, 2), "Fahrenheit\n")
    
ConCel()
