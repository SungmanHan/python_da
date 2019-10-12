
user = '이름 : %s\n나이 : %-10d\n' % ('뽀로로', 23)
# 세번째의 %를 기준으로 앞쪽을 포맷팅 템플릿, 뒷 부분은 매개변수
#  세번째의 % : 포맷팅 연산자 (formatting operator)
# %s, %d 변환 지시어 (서식 문자)
# 매개변수가 여러개인 경우는 튜플로 묶어줌

print(user)

dept = '부서 : %s\n' % '개발부'
gender = '성별 : %c\n' % 'M'
score = '성적 : %f' % 85.3
score = '성적 : %.2f' % 85.3
tall = '신장 : %F' % 183.4
tall1 = '신장1 : %.2f' % 183.4
tall2 = '신장2 : %10.2f' % 183.4
tall3 = '신장3 : %-10.2f' % 183.4


print(dept)
print(gender)
print(score)
print(tall)
print(tall1)
print(tall2)
print(tall3)























