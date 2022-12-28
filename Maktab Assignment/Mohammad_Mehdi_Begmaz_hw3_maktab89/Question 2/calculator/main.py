import logic.parse as parse
import logic.calc as calc
import exceptions


while True:
    equation = input("Please enter your equation: ")
    exceptions.check(equation)
    if equation == 'exit':
        break
    print(calc.inp(parse.get_number1(equation), parse.get_operation(equation), parse.get_number2(equation)))




