# 파이썬은 switch-case가 없어요
# dictionary를 이용하여 switch와 같은 기능을 사용

def switch(x):
    return{
        'one':1,
        'two':2,
        'three':3
    }.get(x, 9) # default

print(switch('two'))
print(switch(1000))
print(switch('a'))




















