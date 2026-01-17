class OperasBas():
    num1=0
    num2=0
    res=0
    #Declaracion del constructor.
    def __init__(self):
        self.num1=0
        self.num2=2
        
    def suma(self,a):
        self.num1=0
        self.res=self.num1+self.num2
        print("La suma es: {}". format(self.res))
    
    def suma(self):
        self.num1=0
        self.res=self.num1-self.num2
        print("La resta es: {}". format(self.res))
        
def main():
    obj=OperasBas()
    obj.suma(5)
    obj.resta()
    
        
        