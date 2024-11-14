while True:
    string = input()
    stack = []
    balanced = True
    if string == ".":
        break
    
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
            
        elif i == ")":
            if stack:
                x = stack.pop()
                if x != "(":
                    balanced = False
            else:
                balanced = False
                
        elif i == "]":
            if stack:
                x = stack.pop()
                if x != "[":
                    balanced = False
            else:
                balanced = False
                
        elif i == ".":
            if stack:
                balanced = False
    if balanced:
        print("yes")
    else:
        print("no")