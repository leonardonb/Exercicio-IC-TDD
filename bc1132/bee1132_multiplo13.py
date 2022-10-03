def soma_mult13(x, y):
    soma = 0
    
    if x > y:
        x,y =y,x
        
    for s in range(x,y+1):
        if not (s%13==0):
            soma=soma+s
    
    return soma

print (soma_mult13(500,550))
