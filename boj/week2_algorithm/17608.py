import sys

N = int(sys.stdin.readline().strip())
stick_list = []
count = 1

for _ in range(N):
    stick_list.append(int(sys.stdin.readline()))

tmp_stick = stick_list.pop()

while stick_list:
    pop_stick = stick_list.pop()
    if pop_stick > tmp_stick:
        count += 1
        tmp_stick = pop_stick

print(count)

