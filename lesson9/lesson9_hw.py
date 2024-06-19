import pyinputplus as pyip

class BMI():
    def __init__(self,n:str,h:float,w:float):
        super().__init__()
        self.name = n
        self.height = h
        self.weight = w

    @property
    def bmi(self):
        return self.weight / (self.height/100) ** 2

    def status(self)->str:
        if self.bmi < 18.5:
            result = '過輕'
        elif self.bmi < 24:
            result = '正常'
        elif self.bmi < 27:
            result = '過重'
        elif self.bmi < 30:
            result = '輕度肥胖'
        elif self.bmi < 35:
            result = '中度肥胖'
        else:
            result = '重度肥胖'
        return result
    
    def __repr__(self):  # __repr__只能有一個(?
        data = f"\n{self.name}您好:\n"
        data += f"您的BMI值是{self.bmi:.2f}\n"
        data += f"您的體重:{self.status()}\n"
        return data
    
name = input("請輸入姓名: ")
height = pyip.inputFloat("請輸入身高(cm): ", min=1)
weight = pyip.inputFloat("請輸入體重(kg): ", min=1)

p1 = BMI(name,height,weight)
print(p1)