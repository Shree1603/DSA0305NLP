def parse(expression):
    index = 0

    def expr():
        nonlocal index
        print("Parsing expression...")
        term()
        while index < len(expression) and expression[index] in '+-':
            operator = expression[index]
            index += 1
            term()
            print(f"Found {operator} term")

    def term():
        nonlocal index
        print("Parsing term...")
        factor()
        while index < len(expression) and expression[index] in '*/':
            operator = expression[index]
            index += 1
            factor()
            print(f"Found {operator} factor")

    def factor():
        nonlocal index
        print("Parsing factor...")
        if expression[index].isdigit():
            print("Found digit")
            index += 1
        elif expression[index] == '(':
            index += 1
            expr()
            if expression[index] == ')':
                index += 1
                print("Found '(' and ')'")
            else:
                raise ValueError("Expected ')' after expression")
        else:
            raise ValueError("Invalid character in expression")

    try:
        expr()
        if index == len(expression):
            print("Parsing successful!")
        else:
            print("Parsing failed!")
    except ValueError as e:
        print("Parsing failed:", e)

# Example usage
expression = "3*(4+5)-2"
parse(expression)
