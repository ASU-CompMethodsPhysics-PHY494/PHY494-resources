# countup.py
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#the-while-loop

tmax = 10.
t, dt = 0, 2.

while t <= tmax:
   print("time " + str(t))
   t += dt
print("Finished")
