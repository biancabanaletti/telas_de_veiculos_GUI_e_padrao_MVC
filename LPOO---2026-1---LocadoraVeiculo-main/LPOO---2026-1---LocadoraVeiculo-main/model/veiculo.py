from enum import Enum
from model.ExcecoesPersonalizadas import PlacaInvalidaError
from .estados_veiculo import DisponivelState


class Categoria(Enum):
    ECONOMICO = "ECONOMICO"
    EXECUTIVO = "EXECUTIVO"


class Veiculo:

    def __init__(self, placa, categoria, taxa_diaria, seguro):
        self.placa = placa
        self.categoria = categoria
        self.taxa_diaria = taxa_diaria
        self.seguro = seguro
        self.estado = DisponivelState()

    def tentar_alugar(self):
        self.estado.tentar_alugar(self)

    def tentar_devolver(self):
        self.estado.tentar_devolver(self)

    def reter_na_frota_pra_conserto(self):
        self.estado.reter_na_frota_pra_conserto(self)

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        if self.valida_placa(placa):
            self.__placa = placa

    @property
    def taxa_diaria(self):
        return self.__taxa_diaria

    @taxa_diaria.setter
    def taxa_diaria(self, taxa_diaria):
        self.__taxa_diaria = taxa_diaria

    def valida_placa(self, placa):
        placa = placa.strip().replace("-", "").upper()

        if len(placa) != 7:
            raise PlacaInvalidaError("Placa deve conter 7 caracteres")

        if not placa[0:3].isalpha():
            raise PlacaInvalidaError("Os 3 primeiros caracteres devem ser letras")

        if not placa[3].isdigit() or not placa[5:7].isdigit():
            raise PlacaInvalidaError("4º, 6º e 7º caracteres devem ser números")

        if not placa[4].isalnum():
            raise PlacaInvalidaError("5º caractere deve ser letra ou número")

        print(f"Placa {placa} válida!!")
        return True


class Carro(Veiculo):

    def __init__(self, placa, categoria, taxa_diaria, seguro):
        super().__init__(placa, categoria, taxa_diaria, seguro)


class Motorhome(Veiculo):

    def __init__(self, placa, categoria, taxa_diaria, seguro):
        super().__init__(placa, categoria, taxa_diaria, seguro)