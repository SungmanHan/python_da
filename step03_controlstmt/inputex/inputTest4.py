'''''
반지름을 입력하세요 : 5
원의 둘레 : 78.5        --3.14*2*r
원의 넓이 : 31.4        --3.14*r*r
'''''

r = int(input('반지름을 입력하세요 : '))

size = 3.14 * r * r
size = 3.14 * r ** 2
rnd = 2 * 3.14 * r

print('원의 둘레 : ', rnd)
print('원의 넓이 : ', size)

print(type(rnd))
print(type(size))