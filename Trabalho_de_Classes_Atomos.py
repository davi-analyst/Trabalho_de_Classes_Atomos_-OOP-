class Proton:
    def __init__(self, carga, massa):
        self._carga = carga # _carga representa a carga elétrica do próton
        self._massa = massa # _massa representa a massa do próton

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
        self._carga = carga # _carga representa a carga do nêutron
        self._massa = massa # _massa representa a massa do nêutron

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
        self._carga = carga # _carga representa a carga elétrica do elétron
        self._massa = massa # _massa representa a massa do elétron

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
    def __init__(self, nome, numero_atomico, num_protons, num_neutrons, num_eletrons, proton, neutron, eletron):
        self._nome = nome # _nome demonstra o nome do elemento químico
        self._numero_atomico = numero_atomico # _numero_atomico representa o número atômico do elemento químico
        self._num_protons = num_protons   # quantidade de prótons
        self._num_neutrons = num_neutrons # quantidade de nêutrons
        self._num_eletrons = num_eletrons # quantidade de elétrons
        self._proton = proton
        self._neutron = neutron
        self._eletron = eletron

    @property
    def nome(self):
        return self._nome

    @property
    def numero_atomico(self):
        return self._numero_atomico

    @property
    def num_protons(self):
        return self._num_protons

    @property
    def num_neutrons(self):
        return self._num_neutrons

    @property
    def num_eletrons(self):
        return self._num_eletrons

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

    @num_protons.setter
    def num_protons(self, num_protons):
        self._num_protons = num_protons

    @num_neutrons.setter
    def num_neutrons(self, num_neutrons):
        self._num_neutrons = num_neutrons

    @num_eletrons.setter
    def num_eletrons(self, num_eletrons):
        self._num_eletrons = num_eletrons

    def mostrar(self):
        print(f"----------------------------\nElemento: {self._nome}\n")
        print(f"Número Atômico: {self._numero_atomico}\n")
        print("Próton:"  f" Carga: +{self._proton.carga}"  f" Massa: ~{self._proton.massa} | Quantidade: {self._num_protons}")
        print("Nêutron:" f" Carga: {self._neutron.carga}"  f" Massa: ~{self._neutron.massa} | Quantidade: {self._num_neutrons}")
        print("Elétron:" f" Carga: -{self._eletron.carga}" f" Massa: ~{self._eletron.massa} | Quantidade: {self._num_eletrons}")

# Programa principal
proton  = Proton(1, 1)
neutron = Neutron(0, 1)
eletron = Eletron(1, 0.00055) # massa do elétron é ~0,00055 u, não 0

atomo = Atomo("Hidrogênio", 1, num_protons=1, num_neutrons=0, num_eletrons=1, proton=proton, neutron=neutron, eletron=eletron)
atomo.mostrar()

print()

# Alterações via setters
# n= A−Z (A = massa e Z = número atômico) para descobrir o número de neutrons
# https://www.todamateria.com.br/tabela-periodica/ tabela periódica para consulta e modificações
atomo.nome = "Hélio"
atomo.numero_atomico = 2
atomo.num_protons  = 2
atomo.num_neutrons = 2
atomo.num_eletrons = 2
atomo.mostrar()

atomo.nome = "Lítio"
atomo.numero_atomico = 3
atomo.num_protons  = 3
atomo.num_neutrons = 4
atomo.num_eletrons = 3
atomo.mostrar()
