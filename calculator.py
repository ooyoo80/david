def add(a, b) :
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0 :
        return 0  
    return a/b


if __name__ == "__main__" :
    try :
        input_choice = int(input("Choose the feature (1,2) : "))
        if input_choice == 1 :
            input_a = int(float(input("Enter first number : ")))  #float를 입력했을 경우를 대비해서, float() -> int()
            input_b = int(float(input("Enter second number : ")))
            input_operator = input("Enter operator (+,-,*,/) : ")

        elif input_choice == 2:
            input_a, input_operator, input_b = input("Enter expression: ").split()  #split()공백을 두고 입력한 식을 각각의 변수로 나눔
            input_a = int(float(input_a))
            input_b = int(float(input_b)) 

        else :
            print("Invalid choice.")
            exit()


        if input_operator == "+" :
            result = add(input_a, input_b)
        elif input_operator == "-" :
            result = subtract(input_a, input_b)
        elif input_operator == "*" :
            result = multiply(input_a, input_b)
        elif input_operator == "/" :
            result = divide(input_a, input_b)
            if not result :                # return == 0 (b==0) 고려
                print("Error: Division by zero.")
                exit()
        else :
            print("Invalid operator")
            exit()

        print(f"Result: {result}")
    

    except ValueError :
        print("Invalid input.")
        exit()