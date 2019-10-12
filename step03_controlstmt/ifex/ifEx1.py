# 3항 연산자
# condition_if_true if condition else condition_if_false

score = 90
print('합격') if score >= 60 else print('불합격')



# 단순 if문 -----------------------------------------------4
score = 95

if 90 <= score <= 100:
    grade = 'A'
if score >= 80 and score < 90:
    grade = 'B'
if score >= 70 and score < 80:
    grade = 'C'
if score >= 60 and score < 70:
    grade = 'D'
if score >= 0 and score < 60:
    grade = 'F'

print('점수는 ', score,'점이고 학점은 ', grade, '입니다')


# # if~elif~else문--------------------------------------------3
#
# score = 95
#
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
#
# print('점수는 ', score,'점이고 학점은 ', grade, '입니다')


# # if~else문 ------------------------------------------------2
# # if condition:
# #     statement1    조건식이 참일때 수행하는 문장
# # else:
# #     statement2    조건식이 거짓일때 수행하는 문장
#
# score = 65
# if score >= 60: # score 가 60보다 크거나 같은가?
#     print('합격')
#     print('점수는 ', score, '점입니다')
# else:
#     print('불합격')
#     print('점수는 ', score, '점이며, 다음 기회에...')


# # if문 --------------------------------------------------1
# # 조건 검사 의 결과가 참 거짓으로 나오는 문장
# # if condition:
# #     statement....
#
# string = 'koroa'
#
# if string == 'korea' :    # string이 korea의 값을 가지고 있다면
#     print('대한민국')
#     print('한국')
# print('서울')  # 조건의 참 거짓과 상관 없이 실행

# 자동 정렬 : ctrl+alt+i



















