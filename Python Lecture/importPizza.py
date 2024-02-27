#  Importing File

import pizza

pizza.makePizza(1, 2, 3, 5)


#  For Importing specific Functions
#  from pizza import makePizza

from pizza import makePizza as mp 

mp(12, "Mushroom", "Green Pepper", "extra cheese")



from pizza import * 
#  Means pizza k sary functions import krny
