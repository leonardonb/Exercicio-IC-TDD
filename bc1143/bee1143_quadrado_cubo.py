def quadradocubo (valor):
    resultado=[]
    for num in range(1,valor+1):
        x = "{} {} {}".format(num, pow(num,2), pow(num,3))
        resultado.append(x)
        
    return resultado
