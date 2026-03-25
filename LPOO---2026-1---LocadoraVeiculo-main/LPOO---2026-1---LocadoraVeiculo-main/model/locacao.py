from datetime import datetime

class Locacao:

    def __init__(self, veiculo, data_inicio, data_fim):
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def calcular_valor_locacao(self):

        if self.data_fim < self.data_inicio:
            raise ValueError("Data final menor que data inicial")

        dias = (self.data_fim - self.data_inicio).days

        if dias == 0:
            dias = 1

        valor = (dias * self.veiculo.taxa_diaria) + self.veiculo.seguro

        return valor