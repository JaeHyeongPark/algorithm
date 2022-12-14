# 0~9,+,-
# 최대 다섯자리
# 처음 시작은 항상 '숫자'

# - 나올때 인지, 뒤에 다시 - 나올때까지 다 더하기.

import sys
equation = sys.stdin.readline().strip().split('-')

result_equation = []
for eq in equation:
    if '+' in eq:
        numbers=eq.split('+')
        a = sum(map(int, numbers))
        result_equation.append(a)
    else:
        result_equation.append(int(eq))
# 첫번째 - 가 나오기 전까지의 숫자들의 합
if len(result_equation) == 1:
    print (result_equation[0])
else:
    result = result_equation[0]
    for num in result_equation[1:]:
        result -= num
    print(result)