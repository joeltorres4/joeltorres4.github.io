# ------------------------------------------------------------
# VoyageTools.py
# ------------------------------------------------------------
places = {
    'NY': 'New York City, NY',
    'FL': 'Orlando, FL',
    'NV': 'Las Vegas, NV',
    'CA': 'Los Angeles, CA',
    'TX': 'Dallas, TX',
    'MA': 'Boston, MA',
    'NC': 'Charlotte, NC',
    'WA': 'Seattle, WA',
    'TN': 'Memphis, TN',
    'GA': 'Atlanta, GA',
    'OH': 'Cleveland, OH',
}

airlines = {
    'AA': 'American Airlines',
    'UA': 'United Airlines',
    'JB': 'Jet Blue',
    'DA': 'Delta Airlines',
    'CA': 'Continental Airlines',
    'SA': 'Southwest Airlines',
}

flight = {
    'NY': {
        'AA': "$450",
        'UA': "$400"
    },
}

def createpackage(lastname, name):
    return "creating package..."


def destinations():
    loc = 'NY'
    ticket = {}
    try:
        ticket = flight[loc]
        for z in ticket:
            print(airlines[z] + " " + ticket[z])
    except:
        return "invalid location"

    # for x in flight:
    #     if (loc == x)
    #         ticket = flight
    #     for y in flight[x]:
    #         print (airlines[y])
    #         print (flight[x][y])


    dest = "\n"
    for values in places:
        dest = dest + places[values] + "\n"
    return dest

def flights(destination, date1, date2):
    ticket = {}
    try:
        ticket = flight[loc]
        for z in ticket:
            print(airlines[z] + " " + ticket[z])
    except:
        return "invalid location"


def fly(destination, airline):
    return "reserving flight to destination through given airline..."


def hotels(destinations):
    return "displaying available hotels in destination..."


# param could be hotel or rental
def reserve(reservation):
    return "reserving hotel/car..."


def cars(destination):
    return "displaying available car rentals in destination..."


def tours(destination):
    return "displaying available tours on given destination..."


# tours is a list of places to visit
def visit(tours):
    return "reserve tour(s) on given destination..."


def book():
    return "complete package reservation..."
