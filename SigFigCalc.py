import math
import tkinter as tk

def sigFigCalc(num1, operation, num2):
    precision1 = findPrecision(num1)
    precision2 = findPrecision(num2)
    
    num1 = float(num1)
    num2 = float(num2)
    if precision1 >= precision2:
        precision = precision1
    else:
        precision = precision2
    
    if operation == "*":
        result = num1*num2
    if operation == "/":
        result = num1/num2
        
    result = round(result/precision)*precision
    
    strResult = str(result)

    if "." in str(result):
        numDecResult = howManyDecimal(str(result))
        numDecPrecision = howManyDecimal(str(precision))
        
        for i in range (0,numDecPrecision-numDecResult,1):
            strResult+="0"
        
    
    return strResult
                    
def findPrecision(num):
    numString = str(num)
    search = 0
    decimalLoc = 0
    for i in range(len(numString)-1,-1,-1):
        if (numString[i] != "0" and search == 0):
            sigFig = i+1
            search = 1
        
        if numString[i] == ".":
            decimalLoc = i
        
    if decimalLoc != 0:
        sigFig = -(len(numString)-decimalLoc-1)
    else:
            sigFig = len(numString)-sigFig
            
    precision = 10**(sigFig)
    
    return precision

def howManyDecimal(num):
    numStr = str(num)
    foundDec = 0
    numDec = 0
    for i in range(len(numStr)-1,-1,-1):
        if numStr[i] != "." and foundDec != 1:
            numDec += 1
        else:
            foundDec = 1
            
    return numDec

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        num1 = ""
        num2 = ""
        opp = ""
        for str in calculation:
            if str == "*" or str == "/":
                opp = str

            elif opp == "":
                num1 = num1+str

            else:
                num2 = num2+str
        return num1, opp, num2
    except:
        print("Invalid Command")

        




root = tk.Tk()

root.geometry("300x275")
root.title("Sig Fig Calculator")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)


root.mainloop()


            

#print(sigFigCalc("3.008765", "*", "2.0050"))
num1, opp, num2 = evaluate_calculation("3.008765*2.0050")
print(sigFigCalc(num1, opp, num2))