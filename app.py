# Calculadora de Consumo de Energia

print("⚡ Calculadora de Consumo de Energia ⚡\n")

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Horas de uso por dia: "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Valor do kWh (você pode alterar depois)
valor_kwh = 0.75

custo_mensal = consumo_mensal * valor_kwh

# Saída
print("\n📊 Resultado:")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal:.2f}")