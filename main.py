# This is a practice problem from a real google interview: 
# https://www.youtube.com/watch?v=qz9tKlF431k

# The function takes in multiple airports and routes 
# the planes can take from airport to airport. The goal was to start
# at an airport with zero routes and find the lowest number of routes
# from the starting airport to other airports to make sure a customer
# can reach any airport from the starting one.

# --------------------------------- INPUTS -----------------------------------

# airports = [ 
#     "BGI", "CDG", "DEL", "DOH", "DSM", 
#     "EWR", "EYW", "HND", "ICN", "JFK", 
#     "LGA", "LHR", "ORD", "SAN", "SFO", 
#     "SIN", "TLV", "BUD"
# ]

# routes = [
#     ["DSM", "ORD"],
#     ["ORD", "BGI"],
#     ["BGI", "LGA"],
#     ["SIN", "CDG"],
#     ["CDG", "SIN"],
#     ["CDG", "BUD"],
#     ["DEL", "DOH"],
#     ["DEL", "CDG"],
#     ["TLV", "DEL"],
#     ["EWR", "HND"],
#     ["HND", "ICN"],
#     ["HND", "JFK"],
#     ["ICN", "JFK"],
#     ["JFK", "LGA"],
#     ["EYW", "LHR"],
#     ["LHR", "SFO"],
#     ["SFO", "SAN"],
#     ["SFO", "DSM"],
#     ["SAN", "EYW"]
# ]

# startingAirport = "LGA"

# # Answer is 3

# --------------------------------- SELF INPUT ---------------------------------

airports = [ 
    "01", "02", "03", "04", "05", 
    "06", "07", "08", "09", "10", 
    "11", "12", "13", "14", "15", 
    "16", "17", "18", "19"
]

routes = [
    ["01", "02"],
    ["02", "03"],
    ["03", "05"],
    ["04", "06"],
    ["06", "02"],
    ["07", "08"],
    ["08", "09"],
    ["09", "07"],
    ["14", "05"],
    ["10", "11"],
    ["11", "12"],
    ["12", "13"],
    ["13", "10"],
    ["15", "16"],
    ["16", "15"],
    ["09", "10"],
    ["17", "18"],
    ["18", "19"],
    ["19", "17"],
    ["11", "03"],
    ["03", "01"],
]

startingAirport = "05"

# Answer is 5

# --------------------------------- MY CODE -----------------------------------

answer = 0
whatAirports = []

airportNum = len(airports)
routeNum = len(routes)

airports2 = airports[:]

checkAirports = [["__" for _ in range(airportNum + 1)] for _ in range(airportNum)]
checkAirports2 = ["__" for _ in range(airportNum)]

# Finds the avaliable routes based on indiviual airports then puts the routes in checkAirports
for m in range(airportNum):

    i = 0
    k = 1

    checkAirports[m][i] = airports[m]

    while True:

        if i >= len(checkAirports[m]) or checkAirports[m][i] == "__":
            break

        for j in range(routeNum):
            if routes[j][0] == checkAirports[m][i]:
                if routes[j][1] not in checkAirports[m]:
                    checkAirports[m][k] = routes[j][1]
                    k += 1

        i += 1
    checkAirports[m][airportNum] = k
    print(checkAirports[m])

print()

# Checks if the airport can be accessed by any other airport, and if not, isolates them in airports2
for f in range(airportNum):
    p = 0

    for ff in range(airportNum):

        if airports2[f] in checkAirports[ff]:
            if airports2[f] in checkAirports[ff] and p == 1:
                airports2[f] = "__"
            p = 1

    print(airports2)

bbb = 0

# Adds the collective routes the airports from airports2 can access to checkAirports2 and adds them to the "stations" counter
# so that they are counted as airports that have to be acccessed
for b in range(airportNum):
    if airports2[b] != "__":
        for bb in range(airportNum):
            if checkAirports[b][bb] not in checkAirports2:
                checkAirports2[bbb] = checkAirports[b][bb]
                bbb += 1
        answer += 1
        whatAirports.append(airports2[b])

print()

# Finds the biggest loop and adds it to the collective routes in checkAirports2 and keeps adding the loops until all airports can be accessed
for rr in range(airportNum):

    print(checkAirports2)

    Max = 0
    maxNum = 0

    for r in range(airportNum):
        if airports[r] not in checkAirports2:
            if Max < int(checkAirports[r][airportNum]):
                Max = checkAirports[r][airportNum]
                maxNum = r
        
    for w in range(airportNum):
            if checkAirports[maxNum][w] != "__" and checkAirports[maxNum][w] not in checkAirports2:
                checkAirports2[bbb] = checkAirports[maxNum][w]
                bbb += 1
    answer += 1
    whatAirports.append(airports[maxNum])

    if "__" not in checkAirports2:
        break

print(checkAirports2)

print("\nAnswer: " + str(answer))
print("From airport: " + startingAirport + "\ngo to airports: " + str(whatAirports) + " to get to all airports.")