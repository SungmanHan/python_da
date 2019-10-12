# 난수 함수 (의사 난수 : pseudo random) 컴퓨터가 임의의 숫자 생성
# from random import randint
# random 모듈의 randint() 를 임포트
from random import *

# import random

print(random())  # 0.0이상 1.0미만 의 임의의 실수
print(random()+1.0) # 1.0이상 2.0미만
print(uniform(1.0, 3.14)) # 1.0이상 3.14미만
print(randint(1, 100)) # 1이상 100이하 (마지막 수 포함 )
print(randrange(1, 100, 3)) # 1부터 100미만 까지 3의 배수
print()

print(choice([1,20,3,40,5])) #[]안의 값중 하나를 리턴
# 리스트 같은 시퀀스 값을 전달해야 함
print(sample(range(1, 46), 6))  # range범위안에서 번호 생성, 중복 배제





























