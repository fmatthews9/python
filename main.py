# This is a Codeacademy challenge for dictionaries. It exploers hurricanes in the Atlantic Ocean.

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
# This function will change the string monetary values into floats

def update_damages_not_recorded(damages):
  updated_damages = []
  conversions = {"M": 1000000, "B": 10000000}
  for damage in damages:
      if damage == "Damages not recorded":
          updated_damages.append(damage)
      if damage.find("M") != -1:
          updated_damages.append(float(damage[0:damage.find('M')])*conversions["M"])
      if damage.find("B") != -1:
          updated_damages.append(float(damage[0:damage.find('B')]) * conversions["B"])
  return updated_damages

updated_damages = update_damages_not_recorded(damages)

# write your construct hurricane dictionary function here:
def create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"Name": names[i],
                                "Month": months[i],
                                "Year": years[i],
                                "Max Sustained Winds": max_sustained_winds[i],
                                "Areas Affected": areas_affected[i],
                                "Damages": updated_damages[i],
                                "Deaths": deaths[i]}

    return hurricanes


hurricanes = create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(hurricanes):
    hurricane_by_year = {}
    for cane in hurricanes:
        current_year = hurricanes[cane]["Year"]
        current_cane = hurricanes[cane]
        if current_year not in hurricane_by_year:
            hurricane_by_year[current_year] = [current_cane]
        else:
            hurricane_by_year[current_year].append(current_cane)
    return hurricane_by_year

hurricanes_by_year = hurricanes_by_year(hurricanes)

# write your count affected areas function here:
def hurricane_occurrence_in_area(hurricanes):
    hurricane_by_area = {}
    for cane in hurricanes:
        for area in hurricanes[cane]["Areas Affected"]:
            if area not in hurricane_by_area:
                hurricane_by_area[area] = 1
            else:
                hurricane_by_area[area] += 1
    return hurricane_by_area

areas = hurricane_occurrence_in_area(hurricanes)

# write your find most affected area function here:

def most_affected_areas(areas):
    max_area = ""
    max_area_count = 0
    for area, value in areas.items():
        if value > max_area_count:
            max_area_count = value
            max_area = area
    return(max_area, max_area_count)

most_affected_areas = most_affected_areas(areas)

# write your greatest number of deaths function here:

def most_deaths(hurricanes):
    max_deaths = 0
    area = ""
    name = ""
    for cane in hurricanes:
        if hurricanes[cane]["Deaths"] > max_deaths:
            max_deaths = hurricanes[cane]["Deaths"]
            area = hurricanes[cane]["Areas Affected"]
            name = hurricanes[cane]["Name"]
    return max_deaths, area, name

max_death = most_deaths(hurricanes)

# write your catgeorize by mortality function here:
def mortality_function(hurricanes):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in hurricanes:
        if hurricanes[cane]["Deaths"] == 0:
            hurricanes_by_mortality[0].append(cane)
        if hurricanes[cane]["Deaths"] > 0 & hurricanes[cane]["Deaths"] <= 100:
            hurricanes_by_mortality[1].append(cane)
        if hurricanes[cane]["Deaths"] > 100 & hurricanes[cane]["Deaths"] <= 500:
            hurricanes_by_mortality[2].append(cane)
        if hurricanes[cane]["Deaths"] > 500 & hurricanes[cane]["Deaths"] <= 1000:
            hurricanes_by_mortality[3].append(cane)
        if hurricanes[cane]["Deaths"] > 1000 & hurricanes[cane]["Deaths"] <= 10000:
            hurricanes_by_mortality[4].append(cane)
        if hurricanes[cane]["Deaths"] > 10000:
            hurricanes_by_mortality[5].append(cane)
    return hurricanes_by_mortality

mortality = mortality_function(hurricanes)

# write your greatest damage function here:

def costly_hurricane(hurricanes):
    cost = 0
    storm = ""
    for cane in hurricanes:
        if hurricanes[cane]["Damages"] != "Damages not recorded":
            if int(hurricanes[cane]["Damages"]) > cost:
                cost = int(hurricanes[cane]["Damages"])
                name = hurricanes[cane]["Name"]
    return cost, name

cost = costly_hurricane(hurricanes)

