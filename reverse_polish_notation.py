# -*- coding: utf-8 -*-

__author__ = "Shybkoi"

u"""Реализация алгоритма обратной польской записи"""


class Expression:
    def __init__(self, expression):
        self.init_exp = expression
        self.rpn_exp = []

    def make_rpn(self):
        try:
            operands = [str(x) for x in range(9)]
            operators_pr1 = ["*", "/"]
            operators_pr2 = ["+", "-"]
            result = ""
            stack = []
            for symbol in self.init_exp:
                if symbol in operands:
                    result += symbol
                    continue
                if symbol in operators_pr1 + operators_pr2:
                    result += ","
                if ((symbol == "(") or
                    ((symbol in operators_pr1 + operators_pr2) and len(stack) == 0) or
                    (symbol in operators_pr1 and stack[0] in operators_pr2) or
                    ((symbol in operators_pr1 + operators_pr2) and stack[0] == "(")):
                    stack.insert(0, symbol)
                    continue
                if ((symbol in operators_pr2 and stack[0] in operators_pr2) or
                   (symbol in operators_pr1 and stack[0] in operators_pr1) or
                   (symbol in operators_pr2 and stack[0] in operators_pr1)):
                    result += stack.pop(0) + ","
                    stack.insert(0, symbol)
                    continue
                if symbol == ")":
                    while True:
                        item = stack.pop(0)
                        if item == "(":
                            break;
                        else:
                            result += "," + item
            else:
                while len(stack) > 0:
                    result += "," + stack.pop(0)
            self.rpn_exp.extend(result.split(','))
        except (IndexError, ValueError) as e:
            print("Incorrect expression!")

    def calculate(self):
        if self.rpn_exp:
            stack = []
            operators = ["+", "-", "*", "/"]
            for symbol in self.rpn_exp:
                if symbol not in operators:
                    stack.append(int(symbol))
                else:
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    if symbol == "+":
                        stack.append(temp1+temp2)
                    if symbol == "-":
                        stack.append(temp2-temp1)
                    if symbol == "*":
                        stack.append(temp1*temp2)
                    if symbol == "/":
                        stack.append(temp2/temp1)
            return stack.pop()
        return None

    def show_expression(self):
        print(self.init_exp)


if __name__ == "__main__":
    exp = Expression("(6+10-4)/(1+1*2)+1")
    exp.show_expression()
    exp.make_rpn()
    print(exp.rpn_exp)
    print("Result is {}".format(exp.calculate()))

