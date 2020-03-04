import myGlobal


# Def: Initialise the stack
# Param: Stack to be initalise, size of the stack
def initStack(stack):
    stack.clear()


# Def: Push to data to the stack (list)
# Param: Stack, data to be pushed
def pushStack(stack, data):
    stack.append(data)


# Def: Pop data out of the stack (list)
# Param: Stack
# Retval: Data Popped
def popStack(stack):
    return stack.pop()
