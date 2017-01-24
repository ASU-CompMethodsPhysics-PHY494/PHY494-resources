# bug 8
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2017/01/24/04_Debugging_1/#activity-fix-as-many-bugs-as-possible

# Calculate the position of an object in free fall as a function of
# time and store time points (in 1-s intervals) and positions in two
# arrays (for plotting):

g = -9.81
t, h, tmax = 1., 0., 10.

times, positions = [], []
while t <= tmax:
   x = 0.5 * g * t * t
   times.append(t)
   positions.append(x)
   t += h

print(times)
print(values)
