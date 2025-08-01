
# --- Exemplo de herança
print ("\nExemplo de herança:")
class Animal:
    def __init__(self, nome):   # self é sempre o primeiro parâmetro dos métodos de uma classe. 
        self.nome = nome        # Ele representa a própria instância do objeto que está chamando o método.

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass     # pass deixa passar sem implementação, se não houvesse o pass abaixo do def nesse caso, daria erro

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
# Exemplo de herança: Cachorro e Gato têm todas as características de Animal, mas com um comportamento
# diferente...


# A implementação de cada animal foi diferente, exemplo de Polimorfismo
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de Polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de Encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # Privando atributo, eh possivel privar metodos assim tb
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
    # Ao privar o saldo no inicio da classe, garante que o saldo foi manipulado de maneira correta.

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.sacar(valor=-500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.sacar(valor=300)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")

conta02 = ContaBancaria(saldo=300)
print(f"\nSaldo da conta bancaria 02: {conta02.consultar_saldo()}")

# --- Abstração 

print("\nExemplo de Abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod   # Decorador para definir como metodo abstrato
    def ligar(self):  # Ou seja, quando for criada uma classe derivada de Veiculo, obrigatoriamente devera implementar
        pass          # o metodo abstrato ligar

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado"

    def desligar(self):
        return "Carro desligado"


carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

# Classe Abstrata é bem útil ao manipular Data Bases
