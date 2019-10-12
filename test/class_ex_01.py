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
        one = int(input("첫 번째 입력값 : "))
        two = int(input("두 번째 입력값 : "))
        cal1.setData(one, two)

        three = input("연산 종류 (+,-,*,/) : ")

        if three in ["+", "-", "*", "/"]:
            test = {"+": cal1.add(), "-": cal1.sub(), "*": cal1.mul(), "/": cal1.div()}
            print("결과 : ", test[three])
            print("-" * 20)
        else:
            print("없는 연산 종류 입력 프로그램 종료")
            print("-" * 20)
            break
    except Exception as e:
        print("숫자를 입력하세요.")
