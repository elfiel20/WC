#This is Excersise 3
#This is a conversion of temperature and wind velocity to windchill

#Here is the data required of the user
T=float(input("Enter temperature(F):"))
WV=float(input("Enter wind velocity(MPH):"))

#This is the operation taking place to calculate the windchill
WC=35.74+0.6215*T+(0.4275*T-35.75)*WV**0.16


#This is the result
print("Windchill is:",round(WC,1))


