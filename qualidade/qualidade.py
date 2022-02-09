peso_antes = float(input())
peso_depois = float(input())

agua = round(100 - ((peso_depois/peso_antes)*100),2)

print(f"{agua:.1f}% do peso do produto é de água congelada.")

if agua < 10:
    if agua < 5:
        print("Produto qualis A.")
    else:
        print("Produto em conformidade.")
if agua >= 10:
    print("Produto não conforme.")
