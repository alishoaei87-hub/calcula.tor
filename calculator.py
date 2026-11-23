history = []

print("===== PYTHON CALCULATOR =====")

while True:

    expression = input("\nEnter calculation: ")

    if expression == "exit":
        print("Calculator closed!")
        break

    if expression == "clear":
        history.clear()
        print("History cleared!")
        continue

    if expression == "history":
        for item in history:
            print(item)
        continue

    try:

        numbers = []
        operators = []

        i = 0

        while i < len(expression):

            char = expression[i]

            if char == " ":
                i += 1
                continue

            if char in "+-*/%":

                if char in "+-" and (
                    len(numbers) == len(operators)
                ):
                    sign = char
                    i += 1

                    if i >= len(expression):
                        raise ValueError

                    start = i

                    while i < len(expression) and (
                        expression[i].isdigit()
                        or expression[i] == "."
                    ):
                        i += 1

                    number = float(expression[start:i])

                    if sign == "-":
                        number = -number

                    numbers.append(number)
                    continue

                operators.append(char)
                i += 1

            elif char.isdigit() or char == ".":

                start = i

                while i < len(expression) and (
                    expression[i].isdigit()
                    or expression[i] == "."
                ):
                    i += 1

                number = float(expression[start:i])
                numbers.append(number)

            else:
                raise ValueError

        if len(numbers) != len(operators) + 1:
            raise ValueError

        i = 0

        while i < len(operators):

            if operators[i] == "*" or operators[i] == "/" or operators[i] == "%":

                if operators[i] == "*":
                    result = numbers[i] * numbers[i + 1]

                elif operators[i] == "/":
                    if numbers[i + 1] == 0:
                        raise ZeroDivisionError

                    result = numbers[i] / numbers[i + 1]

                else:
                    if numbers[i + 1] == 0:
                        raise ZeroDivisionError

                    result = numbers[i] % numbers[i + 1]

                numbers[i] = result
                numbers.pop(i + 1)
                operators.pop(i)

            else:
                i += 1

        result = numbers[0]

        for i in range(len(operators)):

            if operators[i] == "+":
                result += numbers[i + 1]

            elif operators[i] == "-":
                result -= numbers[i + 1]

        print("Result:", result)

        history.append(expression + " = " + str(result))

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except:
        print("Error: Invalid calculation!")