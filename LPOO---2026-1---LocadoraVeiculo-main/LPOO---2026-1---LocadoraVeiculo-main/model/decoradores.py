from abc import ABC, abstractmethod


class LocacaoDecorator(ABC):

    def __init__(self, locacao_alvo):
        self.locacao_alvo = locacao_alvo

    @abstractmethod
    def calcular_valor_locacao(self) -> float:
        pass


class GPSDecorator(LocacaoDecorator):

    def __init__(self, locacao_alvo):
        super().__init__(locacao_alvo)
        self.taxa_fixa_gps = 35.0

    def calcular_valor_locacao(self) -> float:
        return self.locacao_alvo.calcular_valor_locacao() + self.taxa_fixa_gps


class SeguroTerceirosDecorator(LocacaoDecorator):

    def __init__(self, locacao_alvo):
        super().__init__(locacao_alvo)
        self.taxa_diaria_seguro = 15.0

    def calcular_valor_locacao(self) -> float:

        loc = self.locacao_alvo

        # chegar até a locação original
        while hasattr(loc, "locacao_alvo"):
            loc = loc.locacao_alvo

        dias = (loc.data_fim - loc.data_inicio).days
        if dias <= 0:
            dias = 1

        valor_original = self.locacao_alvo.calcular_valor_locacao()

        return valor_original + (dias * self.taxa_diaria_seguro)