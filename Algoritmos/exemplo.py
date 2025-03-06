# Imprime a tabela de conversão de metros para milhas
print("Tabela de Conversão de Metros para Milhas")
print("Km\tMetros\t\tMilhas")
for km in range(20, 170, 10):
    metros = km * 1000
    milhas = metros / 1609.344
    print(f"{km}\t{metros}\t\t{milhas:.4f}")