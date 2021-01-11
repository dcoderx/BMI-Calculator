from BMIcalculator import BMI_calc

Name = input('Enter name : ')
Weight = float(input('Enter Weight : '))
Height = float(input('Enter Height : '))

Result = BMI_calc(Name, Weight, Height)
print(Result)
