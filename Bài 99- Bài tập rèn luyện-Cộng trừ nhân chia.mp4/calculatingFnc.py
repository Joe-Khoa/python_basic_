def calculatingFnc(a,b,op):    
    reslt = 0;
    error = 0;
    
    if op == '+':
        reslt = a+b
    elif op == '-':
        reslt = a-b
    elif op == '*':
        reslt = a*b
    elif op == "/":
        if  b==0:
            error = 'devide 0'
        else:
            reslt = a/b
    else:
        error = 'not the operator'
    if error != 0:
        return('error: ',error)
    else:
        return(reslt)