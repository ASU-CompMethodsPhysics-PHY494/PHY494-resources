# bug 7
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2017/01/24/04_Debugging_1/#activity-fix-as-many-bugs-as-possible

# Create a list of squares of the first 10 natural numbers (0, 1, 2, ..., 10) and print their sum:

squares = []
s = 0
for n in range(1, 10):
   squares.append(s)
   s = n*n
   print(n, s)

sum_s = sum(squares)
print("sum of squares", sum_s)

# should be 385
