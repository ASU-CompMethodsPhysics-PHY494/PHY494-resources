# bug 5
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2017/01/24/04_Debugging_1/#activity-fix-as-many-bugs-as-possible

# Create a list of values -10, -9.8, -9.6, ..., -0.2, 0, 0.2, ..., 10.

h = 0.2
x = [-10 + i*h for i in range(100)]

