"""
Define all the times for cities/regions as dictionaries.
"""
from pytz import timezone
from datetime import datetime


# Dictionary for African cities
africa = {
    'Cairo': datetime.now(timezone('Africa/Cairo')),
    'Joburg': datetime.now(timezone('Africa/Johannesburg')),
    'Lagos': datetime.now(timezone('Africa/Lagos')),
    'Kinshasa': datetime.now(timezone('Africa/Kinshasa')),
    'Nairobi': datetime.now(timezone('Africa/Nairobi')),
    'Tripoli': datetime.now(timezone('Africa/Tripoli'))
}


# Dictionary for Asian cities
asia = {
    'Tokyo': datetime.now(timezone('Asia/Tokyo')),
    'Seoul': datetime.now(timezone('Asia/Seoul')),
    'Delhi': datetime.now(timezone('Asia/Bishkek')),
    'Shanghai': datetime.now(timezone('Asia/Shanghai')),
    'Hong_Kong': datetime.now(timezone('Asia/Hong_Kong')),
    'Singapore': datetime.now(timezone('Asia/Singapore')),
    'Bangkok': datetime.now(timezone('Asia/Bangkok')),
    'Tashkent': datetime.now(timezone('Asia/Tashkent')),
    'Ulanbator': datetime.now(timezone('Asia/Ulan_Bator'))
}


# Dictionary for European cities
europe = {
    'London': datetime.now(timezone('Europe/London')),
    'Paris': datetime.now(timezone('Europe/Paris')),
    'Berlin': datetime.now(timezone('Europe/Berlin')),
    'Lisbon': datetime.now(timezone('Europe/Lisbon')),
    'Moscow': datetime.now(timezone('Europe/Moscow')),
    'Helsinki': datetime.now(timezone('Europe/Helsinki'))
}


# Dictionary for Middle East cities
middle_east = {
    'Isanbul': datetime.now(timezone('Asia/Istanbul')),
    'Riyadh': datetime.now(timezone('Asia/Riyadh')),
    'Dubai': datetime.now(timezone('Asia/Dubai')),
    'Tel_Aviv': datetime.now(timezone('Asia/Tel_Aviv')),
}


# Dictionary for North American cities
n_america = {
    'Los_Angles': datetime.now(timezone('US/Pacific')),
    'New_York': datetime.now(timezone('US/Eastern')),
    'Toronto': datetime.now(timezone('America/Toronto')),
    'Mexico_City': datetime.now(timezone('America/Mexico_City')),
    'Detroit': datetime.now(timezone('US/Michagan')),
    'Austin': datetime.now(timezone('US/Central')),
    'Montreal': datetime.now(timezone('America/Montreal')),
    'Anchorage': datetime.now(timezone('US/Alaska')),
}


# Dictionary for Australia, NZ, and elsewhere in the Pacific
oceania = {
    'Sydney': datetime.now(timezone('Australia/Sydney')),
    'Auckland': datetime.now(timezone('Pacific/Auckland')),
    'Perth': datetime.now(timezone('Australia/Perth')),
    'Honolulu': datetime.now(timezone('US/Hawaii')),
    'Fiji': datetime.now(timezone('Pacific/Auckland')),
}


# Dictionary for S. American cities and their times
s_america = {
    'Sao_Paulo': datetime.now(timezone('America/Sao_Paulo')),
    'Buenos_Aires': datetime.now(timezone('America/Argentina/Buenos_Aires')),
    'Santiago': datetime.now(timezone('America/Santiago')),
    'Bogota': datetime.now(timezone('America/Bogata')),
}