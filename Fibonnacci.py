#Imprime os 100 primeiros números na sequência Fibonacci

fibonacci = 1
ultimo = 1
penultimo = 0

print("Sequência Fibonacci: \n0\n1")

for num in range(100):
  fibonacci = ultimo + penultimo
  penultimo = ultimo
  ultimo = fibonacci
  print(fibonacci)

print("FIM.")
