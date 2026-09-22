notas = [18, 20, 15, 12]

# Bucle correcto en Python
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")
promedio = sum(notas) / len(notas)
nota_alta = max(notas)
nota_baja = min(notas)
print (f"promedio: {promedio}\nnota mas alta: {nota_alta}\nnota mas baja: {nota_baja}")