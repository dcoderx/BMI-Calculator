def BMI_calc(name, weight, height):
    BMI = weight/(height ** 2)
    print(f'BMI : {BMI}')

    if 25 <= BMI < 30:
        return name + ' is overweight.'
    elif BMI < 18.5:
        return name + ' is underweight.'
    elif BMI >= 30:
        return name + ' is obese.'
    else:
        return name + ' is average weighted.'
