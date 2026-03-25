from model.locacao import *
from model.veiculo import *
from model.VeiculoFactory import VeiculoFactory
from datetime import datetime
from model.decoradores import GPSDecorator, SeguroTerceirosDecorator
from model.locacao import Locacao

carro = Carro("ABC1D34", Categoria.ECONOMICO, 100, True)
locacao = Locacao(veiculo=carro, data_fim=None, data_inicio=None)

print("\n--- TESTANDO O PADRÃO STATE RESTRITIVO ---")

carro_estado = VeiculoFactory.criar_veiculo(
    "carro",
    "HJI3K45",
    Categoria.ECONOMICO,
    100.0,
    True
)

carro_estado.tentar_alugar()
carro_estado.tentar_alugar()
carro_estado.reter_na_frota_pra_conserto()
carro_estado.tentar_devolver()
carro_estado.reter_na_frota_pra_conserto()
carro_estado.tentar_alugar()


print("\n--- TESTANDO O PADRÃO DECORATOR ---")

locacao_base = Locacao(
    veiculo=carro,
    data_inicio=datetime(2026, 3, 1),
    data_fim=datetime(2026, 3, 5)
)

print(f"Valor Base (somente Diária + Seguro Base): R$ {locacao_base.calcular_valor_locacao()}")

locacao_com_gps = GPSDecorator(locacao_base)
print(f"Valor somado do pacote + GPS: R$ {locacao_com_gps.calcular_valor_locacao()}")

locacao_vip_top = SeguroTerceirosDecorator(locacao_com_gps)
print(f"Valor pacote completão (Base + GPS + Seg.Terceiros): R$ {locacao_vip_top.calcular_valor_locacao()}")
