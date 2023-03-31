def variavel(*args,**kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(valor)

#a = (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

variavel(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

