while True:
    n = int(input())
    if n == 0:
        break

    m = 1
    while True:
        regioes = list(range(1, n+1))
        pos = 0
        regioes.pop(pos)
        while len(regioes) > 1:
            pos = (pos + m -1)%len(regioes)
            regioes.pop(pos)
        if regioes[0]==13:
            print(m)
            break
        m +=1