# 난수 함수 (의사 난수 : pseudo random) 컴퓨터가 임의의 숫자 생성

# 랜덤 모듈의 런덤 함수를 사용 from random import random

from random import *

print(random())
print(random()+1.0)
print(uniform(1.0,3.14))
print(randint(1,200))
print(randrange(1,300,3))
print(choice(range(1,10)))
print(sample(range(1,46),6))