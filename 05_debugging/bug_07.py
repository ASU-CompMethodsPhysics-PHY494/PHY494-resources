# bug 6

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

