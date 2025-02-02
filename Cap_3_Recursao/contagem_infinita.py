i = 1
def contagem_regressiva(i):
    print(i)
    contagem_regressiva(i-1)
def contagem_progressiva(i):
    print(i)
    contagem_progressiva(i+1)
    
if __name__ == '__main__':
    contagem_regressiva(i)
    contagem_progressiva(i)