def exchang_the_number(number1, number2):
    number=number1
    number1=number2
    number2=number
    print "%r, %r" %(number1, number2)

exchang_the_number(11, 21)

num1=10
num2=20
exchang_the_number(num1, num2)

exchang_the_number(num1+1, num2-2)

exchang_the_number(raw_input("num1"),raw_input("num2"))
