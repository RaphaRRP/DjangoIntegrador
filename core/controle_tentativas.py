tentativas = 0
def tentar():
    global tentativas 
    tentativas += 1
    print(tentativas)
    return tentativas