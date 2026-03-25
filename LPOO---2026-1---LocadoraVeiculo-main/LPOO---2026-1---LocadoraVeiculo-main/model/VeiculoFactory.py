from .veiculo import Carro, Motorhome

class VeiculoFactory:

    @staticmethod
    def criar_veiculo(tipo, placa, categoria, taxa_diaria, seguro):

        tipo = tipo.lower()

        if tipo == "carro":
            return Carro(placa, categoria, taxa_diaria, seguro)

        elif tipo == "motorhome":
            return Motorhome(placa, categoria, taxa_diaria, seguro)

        else:
            raise ValueError("Tipo de veículo inválido")