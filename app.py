# Calculadora de Consumo de Energia

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite o uso diário (em horas): "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo de custo (opcional)
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

# Saída
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")
