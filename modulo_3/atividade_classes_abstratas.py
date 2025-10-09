from abc import ABC, abstractmethod

#1
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass


class cachorro(Animal):
    def __init__(self):
        super().__init__()
    def falar(self):
        return "au au!"


class gato(Animal):
    def __init__(self):
        super().__init__()
    def falar(self):
        return "miau!"


lobo_pidao = cachorro()
print(lobo_pidao.falar())

#2 

#animalzinho = Animal()
#print(animalzinho.falar())
#ele diz que não é possível instanciar a classe abstrata animal sem uma implementação para a abstrair o método "falar()"

#3
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


ret = Retangulo(5, 3)
print(f"Área do retângulo: {ret.area()}")
print(f"Perímetro do retângulo: {ret.perimetro()}")

#4
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("O carro está se movendo.")

# Teste: tentar instanciar Carro (vai gerar erro)
# carro = Carro() 
# carro.mover()

# Corrigindo: implementando parar()
class CarroCorrigido(Transporte):
    def mover(self):
        print("O carro está se movendo.")
    def parar(self):
        print("O carro parou.")

carro2 = CarroCorrigido()
carro2.mover()
carro2.parar()


