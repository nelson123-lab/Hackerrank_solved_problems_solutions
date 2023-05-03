"""Implementation of stack"""
def create_stack():
    stack = []
    return stack

def empty_stack(stack):
    return len(stack) == 0

# adding elements
def push(stack, item):
    stack.append(item)
    print(f"{item} has been added to the stack", item)

def pop(stack):
    if empty_stack(stack):
        return "Stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, 1)
push(stack, 3)
push(stack, 5)
print(stack)
pop(stack)
pop(stack)
print(stack)

