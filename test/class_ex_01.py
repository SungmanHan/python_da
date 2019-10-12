class Calculator:

    def __init__(self):
        self.result = 0
        self.x = 0
        self.y = 0

    def setData(self, num1, num2):
        self.x = num1
        self.y = num2

    def add(self):
        self.result = self.x + self.y
        return self.result

    def sub(self):
        self.result = self.x - self.y
        return self.result

    def mul(self):
        self.result = self.x * self.y
        return self.result

    def div(self):
        self.result = self.x / self.y
        return self.result


cal1 = Calculator()

while True:
    try:
        three = input("연산 종류 (+,-,*,/) : ")
        one = int(input("첫 번째 입력값 : "))
        two = int(input("두 번째 입력값 : "))
        cal1.setData(one, two)

        test = lambda x: {"+": cal1.add(), "-": cal1.sub(), "*": cal1.mul(), "/": cal1.div()}.get(x, "연산 종류가 틀리다")

        print("결과 : ", test(three))

    except Exception as e:
        print("숫자를 입력하세요.")
