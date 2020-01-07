class Pessoa:
    def __init__(self, *filhos, name= None, idade=39):
        self.filhos = list(filhos)
        self.idade = idade
        self.name = name

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    renzo =Pessoa(name= 'Renzo')
    luciano = Pessoa(renzo, name = 'Luciano ')
    print(Pessoa.cumprimentar(renzo))
    print(id(renzo))
    print(renzo.cumprimentar())
    print(renzo.name)
    renzo.name = 'Carlos'
    print(luciano.name)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.name)