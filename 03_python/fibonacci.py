# fibonacci.py

Fmax = 100
a, b = 0, 1

while b < Fmax:
   print(b, end=' ')
   a, b = b, a+b
print()
