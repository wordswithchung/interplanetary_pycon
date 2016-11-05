"""
To keep things fair and simple, attendees are assumed to be making a round trip
from their home system to the conference's system and back.

Find who deserves the prize. Your solution should implement a print_winner_string()
that outputs a single line formatted as follows, showing light years rounded to the
second decimal:

Winner: Person One (traveled 4.54 light years)

Your script's template will include three sources of information:

A dictionary of star systems with their X, Y, Z coordinates. For example:
star_coordinates = { 'alpha_centauri': {'x': -1.643, 'y': -1.374, 'z': -3.838}}

A list of attendee tuples containing their name and home system. For example:

attendees = [('An Attendee', 'alpha_centauri'), ('Another Attendee', 'sol')]

A dictionary of conferences, with a list of their attendees IDs. For example:

conferences = {'sol': { 'attendees': [0, 1, 3, 4]}}

Note: the items in the attendees IDs list map to the attendees' index in the attendees[] list

Your script's template will also include a get_distance() function that can be used
to calculate the distance, in light years, between two systems. The arguments to
get_distance() must be two dictionaries each containing one system's X, Y and Z
coordinates. For example:

distance = get_distance({'x': 0, 'y': 0, 'z': 0}, {'x': -1.612, 'y': 8.078, 'z': -2.474})

# math.sqrt() is needed to compute the distance between two stars

from math import sqrt

# Star coordinates given as a dictionary

star_coordinates = {
    'alpha_centauri': {'x': -1.643, 'y': -1.374, 'z': -3.838},
    'do_cephei': {'x': 6.43, 'y': -2.73, 'z': 11.0},
    'procyon': {'x': -4.769, 'y': 10.31, 'z': 1.039},
    'ross_780': {'x': 14.24, 'y': -4.266, 'z': -3.778},
    'sirius': {'x': -1.612, 'y': 8.078, 'z': -2.474},
    'sol': {'x': 0, 'y': 0, 'z': 0},
    'vega': {'x': 3.165, 'y': -19.46, 'z': 15.85},
}



# Overall list of attendee tuples: (name, home system)

attendees = [
    ("Ada von Rossum", 'sol'),
    ("David 4431", 'sirius'),
    ("David 5111", 'sirius'),
    ("George Xie", 'sol'),
    ("Hogarth", 'procyon'),
    ("Neytiri", 'alpha_centauri'),
    ("Xtab-len Phaurspess", 'do_cephei'),
    ("Rappaport", 'procyon'),
    ("Tsu'tey", 'alpha_centauri'),
    ("Pep Aite", 'do_cephei'),
    ("Zeg Wault", 'ross_780'),
    ("Zsiggy Zegvee", 'ross_780'),
]

# Attendees and speakers for each conference, by their index in attendees[]

conferences = {
    'sol': {
        'attendees': [0, 2, 4, 7, 9, 3, 6, 1, 8],
    },
    'sirius': {
        'attendees': [2, 4, 0, 10, 5, 9],
    },
    'alpha_centauri': {
        'attendees': [3, 8, 11, 7, 2, 0, 4],
    },
}

def get_distance(s1_coordinates, s2_coordinates):
    return sqrt(
        (s2_coordinates['x'] - s1_coordinates['x']) ** 2 +
        (s2_coordinates['y'] - s1_coordinates['y']) ** 2 +
        (s2_coordinates['z'] - s1_coordinates['z']) ** 2
    )
"""

from math import sqrt

attendees = [
    ("Ada von Rossum", 'sol'),
    ("David 4431", 'sirius'),
    ("David 5111", 'sirius'),
    ("George Xie", 'sol'),
    ("Hogarth", 'procyon'),
    ("Neytiri", 'alpha_centauri'),
    ("Xtab-len Phaurspess", 'do_cephei'),
    ("Rappaport", 'procyon'),
    ("Tsu'tey", 'alpha_centauri'),
    ("Pep Aite", 'do_cephei'),
    ("Zeg Wault", 'ross_780'),
    ("Zsiggy Zegvee", 'ross_780'),
]

conferences = {
    'sol': {
        'attendees': [0, 2, 4, 7, 9, 3, 6, 1, 8],
    },
    'sirius': {
        'attendees': [2, 4, 0, 10, 5, 9],
    },
    'alpha_centauri': {
        'attendees': [3, 8, 11, 7, 2, 0, 4],
    },
}

star_coordinates = {
    'alpha_centauri': {'x': -1.643, 'y': -1.374, 'z': -3.838},
    'do_cephei': {'x': 6.43, 'y': -2.73, 'z': 11.0},
    'procyon': {'x': -4.769, 'y': 10.31, 'z': 1.039},
    'ross_780': {'x': 14.24, 'y': -4.266, 'z': -3.778},
    'sirius': {'x': -1.612, 'y': 8.078, 'z': -2.474},
    'sol': {'x': 0, 'y': 0, 'z': 0},
    'vega': {'x': 3.165, 'y': -19.46, 'z': 15.85},
}

def get_distance(s1_coordinates, s2_coordinates):
    return sqrt(
        (s2_coordinates['x'] - s1_coordinates['x']) ** 2 +
        (s2_coordinates['y'] - s1_coordinates['y']) ** 2 +
        (s2_coordinates['z'] - s1_coordinates['z']) ** 2
    )

distance = get_distance({'x': 0, 'y': 0, 'z': 0}, {'x': -1.612, 'y': 8.078, 'z': -2.474})

new = [list(x) for x in attendees]
okay = [x.append(0) for x in new]

for conference in conferences.keys():
    for a in conferences[conference]['attendees']:
        new[a][2] += (get_distance(star_coordinates[attendees[a][1]], 
                                         star_coordinates[conference]))

okay = [x.sort() for x in new]
new.sort()

print "Winner: {} (traveled {:.2f} light years)".format(new[-1][1], new[-1][0])
