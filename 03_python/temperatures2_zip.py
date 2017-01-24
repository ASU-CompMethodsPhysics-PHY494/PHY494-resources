# temperature conversion with results stored in a list
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#activity-for-loop
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2017/01/19/03_Introduction_to_Python_2/#activity-range

temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
temp_Kelvin = []
for theta in temperatures:
   T = (theta - 32) * (5/9) + 273.15
   temp_Kelvin.append(T)

# show T in F and K side by side (with zip())
for T_F, T_K in zip(temperatures, temp_Kelvin):
    print(str(T_F) + " F", str(T_K) + " K")


