def notasValidas(nota_a, nota_b):

    notasValidas = 0
    media = 0
    
    if (nota_a >= 0 and nota_a <= 10): 
        notasValidas =notasValidas + 1
        media = media + nota_a
    
    if (nota_b >= 0 and nota_b <= 10): 
        notasValidas =notasValidas + 1
        media = media + nota_b
        
    if notasValidas < 2:
        return "Nota inválida"
    
    else:
        return media/2