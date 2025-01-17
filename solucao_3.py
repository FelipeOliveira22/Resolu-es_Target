import json
import sys
import locale

sys.stdout.reconfigure(encoding='utf-8')

dados = '''
{
    "faturamento_diario": [0, 1500.0, 2300.0, 0, 800.0, 900.0, 0, 1600.0, 1200.0, 1700.0, 0]
}
'''
faturamento = json.loads(dados)["faturamento_diario"]

dias_uteis = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(dias_uteis)
maior_faturamento = max(dias_uteis)
media_mensal = sum(dias_uteis) / len(dias_uteis)
dias_acima_da_media = len([valor for valor in dias_uteis if valor > media_mensal])

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
