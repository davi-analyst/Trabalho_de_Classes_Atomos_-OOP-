class Proton:
    def __init__(self, carga, massa):
        self._carga = carga             # _carga representa a carga elétrica do próton
        self._massa = massa             # _massa representa a massa do próton

    @property
    def carga(self):
        return self._carga

    @property
    def massa(self):
        return self._massa

    @carga.setter
    def carga(self, carga):
        self._carga = carga

    @massa.setter
    def massa(self, massa):
        self._massa = massa

class Neutron:
    def __init__(self, carga, massa):
        self._carga = carga              # _carga representa a carga do nêutron
        self._massa = massa              # _massa representa a massa do nêutron

    @property
    def carga(self):
        return self._carga

    @property
    def massa(self):
        return self._massa

    @carga.setter
    def carga(self, carga):
        self._carga = carga

    @massa.setter
    def massa(self, massa):
        self._massa = massa

class Eletron:
    def __init__(self, carga, massa):
        self._carga = carga              # _carga representa a carga elétrica do elétron
        self._massa = massa              # _massa representa a massa do elétron

    @property
    def carga(self):
        return self._carga

    @property
    def massa(self):
        return self._massa

    @carga.setter
    def carga(self, carga):
        self._carga = carga

    @massa.setter
    def massa(self, massa):
        self._massa = massa

class Atomo:
    def __init__(self, nome, numero_atomico, proton, neutron, eletron):
        self._nome = nome                       # _nome demonstra o nome do elemento químico
        self._numero_atomico = numero_atomico   # _numero_atomico representa o número atômico do elemento químico
        self._proton = proton                   # quantidade de protons
        self._neutron = neutron                 # quantidade de neutrons
        self._eletron = eletron                 # quantidade de elétrons

    @property
    def nome(self):
        return self._nome

    @property
    def numero_atomico(self):
        return self._numero_atomico

    @property
    def proton(self):
        return self._proton

    @property
    def neutron(self):
        return self._neutron

    @property
    def eletron(self):
        return self._eletron

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @numero_atomico.setter
    def numero_atomico(self, numero_atomico):
        self._numero_atomico = numero_atomico

    @proton.setter
    def proton(self, proton):
        self._proton = proton

    @neutron.setter
    def neutron(self, neutron):
        self._neutron = neutron

    @eletron.setter
    def eletron(self, eletron):
        self._eletron = eletron

    def mostrar(self):
        print(f"----------------------------\nElemento: {self._nome}\n")
        print(f"Número Atômico: {self._numero_atomico}\n")
        print("Próton:"f"  Carga: +{self._proton.carga}"f"  Massa: ~{self._proton.massa}")
        print("Nêutron:"f"  Carga: {self._neutron.carga}"f"  Massa: ~{self._neutron.massa}")
        print("Elétron:"f"  Carga: -{self._eletron.carga}"f"  Massa: ~{self._eletron.massa}")


# Programa principal
proton = Proton(1, 1)
neutron = Neutron(0, 1)
eletron = Eletron(1, 0)
atomo = Atomo("Hidrogênio", 1, proton, neutron, eletron)

atomo.mostrar()
print()

# Alterações via setters 
# n= A−Z (A = massa e Z = número atômico) para descobrir o número de neutrons
# https://www.todamateria.com.br/tabela-periodica/ tabela periódica para consulta e modificações

atomo.nome = "Hélio"
atomo.numero_atomico = 2
proton.carga = 2
neutron.massa = 2
eletron.carga = 2

atomo.mostrar()

atomo.nome = "Lítio"
atomo.numero_atomico = 3
proton.carga = 3
neutron.massa = 4
eletron.carga = 3

atomo.mostrar()