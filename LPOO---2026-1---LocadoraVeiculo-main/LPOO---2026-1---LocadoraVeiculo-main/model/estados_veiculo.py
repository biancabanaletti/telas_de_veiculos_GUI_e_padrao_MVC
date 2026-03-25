class VeiculoState:

    def tentar_alugar(self, veiculo):
        raise Exception("Operação não permitida neste estado")

    def tentar_devolver(self, veiculo):
        raise Exception("Operação não permitida neste estado")

    def reter_na_frota_pra_conserto(self, veiculo):
        raise Exception("Operação não permitida neste estado")


class DisponivelState(VeiculoState):

    def tentar_alugar(self, veiculo):
        print("Veículo alugado com sucesso!")
        veiculo.estado = AlugadoState()

    def tentar_devolver(self, veiculo):
        print("Veículo já está disponível.")

    def reter_na_frota_pra_conserto(self, veiculo):
        print("Veículo enviado para manutenção.")
        veiculo.estado = ManutencaoState()


class AlugadoState(VeiculoState):

    def tentar_alugar(self, veiculo):
        print("Erro: veículo já está alugado!")

    def tentar_devolver(self, veiculo):
        print("Veículo devolvido com sucesso!")
        veiculo.estado = DisponivelState()

    def reter_na_frota_pra_conserto(self, veiculo):
        print("Erro: veículo alugado não pode ir para manutenção.")


class ManutencaoState(VeiculoState):

    def tentar_alugar(self, veiculo):
        print("Erro: veículo está em manutenção!")

    def tentar_devolver(self, veiculo):
        print("Erro: veículo em manutenção não pode ser devolvido.")

    def reter_na_frota_pra_conserto(self, veiculo):
        print("Veículo já está em manutenção.")