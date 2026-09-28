Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Banglore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in Australia and city2 in Australia:
    print("Both the cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both the cities are in UAE") 
elif city1 in India and city2 in India:
    print("Both the cities are in India")  
else:
    print("They don't belong to same country")        