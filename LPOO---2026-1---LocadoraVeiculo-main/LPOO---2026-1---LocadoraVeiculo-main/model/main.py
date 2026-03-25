from datetime import datetime
from locacao import Locacao
from VeiculoFactory import VeiculoFactory

veiculo1 = VeiculoFactory.criar_veiculo("carro", "ABC1234", "A", 150, 50)
veiculo2 = VeiculoFactory.criar_veiculo("motorhome", "XYZ9999", "B", 300, 80)

loc1 = Locacao(
    veiculo1,
    datetime(2026,3,1),
    datetime(2026,3,4)
)

print("Valor locação 1:", loc1.calcular_valor_locacao())

loc2 = Locacao(
    veiculo1,
    datetime(2026,3,1),
    datetime(2026,3,1)
)

print("Valor locação 2:", loc2.calcular_valor_locacao())

try:
    veiculo3 = VeiculoFactory.criar_veiculo("bike", "AAA1111", "C", 50, 10)
except ValueError as e:
    print("Erro:", e)