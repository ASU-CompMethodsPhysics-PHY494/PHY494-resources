# fibonacci.py
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#the-while-loop

Fmax = 100
a, b = 0, 1

while b < Fmax:
   print(b, end=' ')
   a, b = b, a+b
print()
