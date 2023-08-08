import sys
from collections import deque
input = sys.stdin.readline

def push_front(x):
    deque.appendleft(x)

def push_back(x):
    deque.append(x)

def pop_front():
    if deque:
        print(deque.popleft())
    else:
        print(-1)

def pop_back():
    if deque:
        print(deque.pop())
    else:
        print(-1)

def size():
    print(len(deque))

def empty():
    if deque:
        print(0)
    else:
        print(1)

def front():
    if deque:
        print(deque[0])
    else:
        print(-1)

def back():
    if deque:
        print(deque[-1])
    else:
        print(-1)

n = int(input())
deque = deque()
instructions = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

for _ in range(n):
    instruction_input = input().split()
    instruction = instruction_input[0]
    instructions[instruction]() if len(instruction_input) == 1 else instructions[instruction](instruction_input[1])