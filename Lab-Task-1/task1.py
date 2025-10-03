def calc(expr: str) -> float:
    expr = expr.replace("×", "*").replace("÷", "/")

    while "(" in expr:
        start = expr.rfind("(")
        end = expr.find(")", start)
        val = calc(expr[start+1:end])
        expr = expr[:start] + str(val) + expr[end+1:]

    stack = []
    num = ""
    for ch in expr:
        if ch.isdigit() or ch == ".":
            num += ch
        else:
            if num:
                stack.append(float(num))
                num = ""
            stack.append(ch)
    if num:
        stack.append(float(num))

    i = 0
    while i < len(stack):
        if stack[i] in ("*", "/"):
            a, op, b = stack[i-1:i+2]
            val = a * b if op == "*" else a / b
            stack[i-1:i+2] = [val]
            i -= 1
        else:
            i += 1

    i = 0
    while i < len(stack):
        if stack[i] in ("+", "-"):
            a, op, b = stack[i-1:i+2]
            val = a + b if op == "+" else a - b
            stack[i-1:i+2] = [val]
            i -= 1
        else:
            i += 1

    return stack[0]


expr1 = input("Enter first expression: ")
print("= ", calc(expr1))

expr2 = input("Enter second expression: ")
print("= ", calc(expr2))
