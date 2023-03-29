from stack import Stack



def eval_postfix(expr):
    stack = Stack()
    for character in expr:
        if character in "0123456789":
            stack.push(character)
        elif character == " ":
            pass
        else:
            num1 = int(stack.top())
            stack.pop()
            num2 = int(stack.top())
            stack.pop()
            if character == "+":
                result = num1 + num2
            elif character == "-":
                result = num2-num1
            elif character == "*":
                result = num1*num2
            else:
                result = num1/num2
            stack.push(result)
    return stack.top()
            


def in2post(expr):
    if not isinstance(expr, str):
        raise TypeError("expression is not a string")
    stack = Stack()
    final_expression = ""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    for character in expr:
        if character == "(":
            stack.push(character)
        elif character in "0123456789":
            final_expression = final_expression + character + " "
        elif character in "+-*/":
            if stack.size == 0:
                stack.push(character)
            else:
                while stack.size != 0 and stack.top() != "(" and precedence[stack.top()] >= precedence[character]:
                    final_expression = final_expression + stack.top() + " "
                    stack.pop()
                stack.push(character)
        elif character == ")":
            while stack.size != 0 and stack.top() != "(":
                final_expression = final_expression + stack.top() + " "
                stack.pop()
            if stack.top() == "(":
                stack.pop()
    while stack.size != 0:
        final_expression = final_expression + stack.top() + " "
        stack.pop()
    return final_expression
            


def main():
    with open('Stack Project\data.txt', 'r') as file:
        for line in file:
            expression = line.strip()
            print("infix: " + expression)
            print("postfix: " + in2post(expression))
            print("answer: " + str(float(eval_postfix(in2post(expression)))))
            print("")
    
if __name__=="__main__":
    main()

print(eval_postfix("5-9-"))



# test_stack = Stack()

# test_stack.push(1)
# test_stack.push(10)
# test_stack.push(4)
# test_stack.push(7)
# test_stack.push(9)
# test_stack.push(3)
# test_stack.push(7)
# test_stack.push(3)
# test_stack.push("test string")
# test_stack.push("test strin")
# print(test_stack.top())


# print(test_stack)
# print(test_stack.size)

# test_stack.pop()
# test_stack.pop()
# test_stack.pop()

# print(test_stack)
# print(test_stack.size)
# print(test_stack.top)
