lado_a = float(input())
lado_b = float(input())
lado_c = float(input())

perimetro = int(lado_a + lado_b + lado_c)

if abs(lado_b - lado_c) < lado_a and lado_a < lado_b + lado_c:
    print(f"triangulo valido. {perimetro}")
elif abs(lado_a - lado_c) < lado_b and lado_b < lado_a + lado_c:
    print(f"triangulo valido. {perimetro}")
elif abs(lado_a - lado_b) < lado_c and lado_c < lado_a + lado_b:
    print(f"triangulo valido. {perimetro}")
else:
    print("triangulo invalido.")
