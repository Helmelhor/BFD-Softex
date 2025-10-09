from abc import ABC, abstractmethod

# 1. Interface Pagamento
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor} no cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor} no boleto.")


cartao = CartaoCredito()
cartao.processar(100)

boleto = Boleto()
boleto.processar(200)

# 2. Interface múltipla
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")
    def desligar(self):
        print("Computador desligado.")


pc = Computador()
pc.ligar()
pc.desligar()

# 3. Interface em herança múltipla
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório impresso.")
    def exportar(self):
        print("Relatório exportado.")


rel = Relatorio()
rel.imprimir()
rel.exportar()

# 4. Forçando contrato
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass

# Classe com método faltando (vai dar erro ao instanciar)
class RepositorioMemoriaErro(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")
    # def buscar(self, id):
    #     pass

# repo_erro = RepositorioMemoriaErro()


class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print("Objeto salvo na memória.")
    def buscar(self, id):
        print(f"Buscando objeto com id {id} na memória.")


repo = RepositorioMemoria()
repo.salvar({"nome": "João"})
repo.buscar(1)
