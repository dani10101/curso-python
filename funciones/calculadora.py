import math



class calculadora():
    def suma(num1:int,num2:int):
        return num1 + num2
    def resta(num1:int,num2:int):
        return num1 - num2
class calculadora_trig(calculadora):
    def seno(num1:int):
        return math.sin(num1)
    def coseno(num1:int):
        return math.cos(num1)
print(calculadora_trig.suma(3,4))
