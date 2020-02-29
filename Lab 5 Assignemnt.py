"""Name: Hillol Dutta
Date created: 14-Feb-2020
Version of Python you are using: Python 3.4.
Very brief description of the assignment or the assignment name: Dictionary of refugee population and data extraction of it."""


#Dictionary of five countries with name and refugee population as key-value pairs.
refugee_14={'Bangladesh':13176, 'Chad':12138, 'Kenya':83750, 'Thailand':46978, 'India':65057}

#Function to extract country names.
for x in refugee_14.keys():
    print(x)

#Function to extract refugee population.
for x in refugee_14.values():
    print(x)


#Function to extract refugee population.
for x,y in refugee_14.items():
    print(x,"has",y, "refugees" )
