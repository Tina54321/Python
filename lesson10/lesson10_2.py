import random
import pyinputplus as pyip

# (run .py檔時) names.txt此檔案存在lesson10,並分在根目錄,所以若檔案在該資料夾必須重新打開在該目錄的終端機
with open('names.txt',encoding='utf-8') as file:  
    content:str = file.read()

n: int = pyip.inputInt("請輸入取得名字的數量", min=0, max=200)
names:list[str] = content.split(sep='\n') # 文字變串列-->可擷取需要範圍
random_names:list[str] = random.choices(population=names, k=n)
for name in random_names:
    print(name, end=' ')
print()