# bug 7
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2017/01/24/04_Debugging_1/#activity-fix-as-many-bugs-as-possible

# Create a list of squares of the first 10 natural numbers (0, 1, 2, ..., 10) and print their sum:

squares = []
for n in range(0, 11):
   s = n*n
   squares.append(s)
   print(n, s)

sum_s = sum(squares)
print("sum of squares", sum_s)

# should be 385
