# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome # Atributo de instancia

    def metodo_instancia(self): # Metodos de instancia requer uma instancia (objeto) para ser chamado 
        return f"Metodo de instancia chamado para {self.valor}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Metodo da classe chamado para valor = {cls.valor}"
    
    @staticmethod
    def metodo_estatico():    # Nao recebe referencia da classe
        return "Metodo estatico chamado"

    
obj = MinhaClasse(nome="CLasse Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor) #Já os atributos da classe nao precisam de instancias para serem chamados
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca,modelo,int(ano))

configuracao1 = "Toyota, Corolla, 2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"\n Marca: {carro1.marca}\n Modelo: {carro1.modelo}\n Ano: {carro1.ano}\n")


class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
print(Matematica.somar(a=10, b=20))