import sys

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    # 스택의 맨 위에꺼 리턴
    def peek(self):
        return self.data[-1]

def convert_to_postfix(S):
    opStack = ArrayStack() #연산자 스택
    answer = '' # 피연산자+연산자(outstack)
    
    for w in S :
        if w in prec : #연산자를 만난다면,
            if opStack.isEmpty() :
                opStack.push(w)
            else :
                if w == '(' :
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) : #만난 연산자의 우선순위<=opstack 맨위 연산자의 우선순위
                        answer += opStack.pop() # 스택 연산자의 우선순위가 높으면, 다 빼서 outstack에 넣음
                        if opStack.isEmpty() : break
                    opStack.push(w)
        elif w == ')' :
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop() # '(' 빼는 작업
        else : # 숫자를 만난다면
            answer += w
    
    while not opStack.isEmpty() : #연산자스택에 남은거 다 빼서 정리
        answer += opStack.pop()
    
    return answer

def calculate(tokens):
    stack = ArrayStack() #postfix 스택
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop())
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.push(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()/rv)
        else:
            stack.push(int(token))
    return stack.pop()

infix = sys.stdin.readline().replace("\n", "").replace(" ","")

postfix = convert_to_postfix(infix)

print(f"postfix : {postfix}")

result = calculate(postfix)
print(f"result : {result}")