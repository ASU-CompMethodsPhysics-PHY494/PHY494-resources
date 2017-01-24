# bug 6
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2017/01/24/04_Debugging_1/#activity-fix-as-many-bugs-as-possible

# The sinc function is defined for all real numbers
# but this implementation is incomplete.
# 1. find values for which our function does not produce the correct
#    result
# 2. fix it
# 3. BONUS: plot sinc(x) for values from -10 to 10 in steps
#    of 0.2.

import math
def sinc(x):
   return math.sin(x)/x

