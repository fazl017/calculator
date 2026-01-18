

while True:
    try:

        firstNum = int(input("Please enter the first  number : "))
        secondNum = int(input("Please enter the second  number : "))

        process = input("Select the action you want to perform : ('+', '-', '*', '/') : ")


        def collection():
            print (f"The result of the operation you performed : {firstNum} + {secondNum} = {firstNum + secondNum}")

        def removal():
            print(f"The result of the operation you performed : {firstNum} - {secondNum} = {firstNum - secondNum}")


        def collision():
            print(f"The result of the operation you performed : {firstNum} * {secondNum} = {firstNum * secondNum}")

        def division():
            print(f"The result of the operation you performed : {firstNum} / {secondNum} = {firstNum / secondNum}")



        if process == "+":
            collection()
        elif process == "-":
            removal()
        elif process == "*":
            collision()
        elif process == "/":
            division()

        else:
            print("Enter a valid transaction")
            continue



        exit1 = input("EXIT ==> q-Q | CONTINUE ==> c-C : ").lower()

        if exit1 == "c":
            continue


        elif exit1 == "q":
            print("Goodbye")
            break


    except Exception as error :
        print("Enter a valid number ")
