#! /usr/bin/env python3

from auth import API, API_SECRET, BEARER_TOKEN, ACCESS, ACCESS_SECRET
import tweepy
import sys

# verify that API keys have been entered into auth.py

if len(API) <= 4:
    sys.exit("ERROR! API key not correct. Please check auth.py")
if len(API_SECRET) <= 4:
    sys.exit("ERROR! API_SECRET key is not correct. Please check auth.py")
if len(ACCESS) <= 4:
    sys.exit("ERROR! ACCESS key is not correct. Please check auth.py")
if len(ACCESS_SECRET) <= 4:
    sys.exit("ERROR! ACCESS_SECRET key is not correct. Please check auth.py")


# print list of agencies
print("\n[1] LAPD")
print("[2] LASD")
print("[3] CHP")
print("[q] Quit")
agencyselected = input("\nEnter the agency involved: ")

# lapd
if agencyselected == '1':
    agency = 'LAPD'
    print("\n[1] CENTRAL")
    print("[2] RAMPART")
    print("[3] SOUTHWEST")
    print("[4] HOLLENBECK")
    print("[5] HARBOR")
    print("[6] HOLLYWOOD")
    print("[7] WILSHIRE")
    print("[8] WEST LA")
    print("[9] VAN NUYS")
    print("[10] WEST VALLEY")
    print("[11] NORTHEAST")
    print("[12] 77TH STREET")
    print("[13] NEWTON")
    print("[14] PACIFIC")
    print("[15] NORTH HOLLYWOOD")
    print("[16] FOOTHILL")
    print("[17] DEVONSHIRE")
    print("[18] SOUTHEAST")
    print("[19] MISSION")
    print("[20] OLYMPIC")
    print("[21] TOPANGA")
    print("[v] VALLEY")
    print("[s] SOUTH")
    print("[c] CENTRAL")
    print("[w] WEST")
    print("[u] UNKNOWN LOCATION")
    print("[q] Quit")
    divisionselected = input("\nDivision or location: ")
    if divisionselected == '1':
        division = 'CENTRAL DIVISION'
    elif divisionselected == '2':
        division = 'RAMPART DIVISION'
    elif divisionselected == '3':
        division = 'SOUTHWEST DIVISION'
    elif divisionselected == '4':
        division = 'HOLLENBECK DIVISION'
    elif divisionselected == '5':
        division = 'HARBOR DIVISION'
    elif divisionselected == '6':
        division = 'HOLLYWOOD DIVISION'
    elif divisionselected == '7':
        division = 'WILSHIRE DIVISION'
    elif divisionselected == '8':
        division = 'WEST LA DIVISION'
    elif divisionselected == '9':
        division = 'VAN NUYS DIVISION'
    elif divisionselected == '10':
        division = 'WEST VALLEY DIVISION'
    elif divisionselected == '11':
        division = 'NORTHEAST DIVISION'
    elif divisionselected == '12':
        division = '77TH STREET DIVISION'
    elif divisionselected == '13':
        division = 'NEWTON DIVISION'
    elif divisionselected == '14':
        division = 'PACIFIC DIVISION'
    elif divisionselected == '15':
        division = 'NORTH HOLLYWOOD DIVISION'
    elif divisionselected == '16':
        division = 'FOOTHILL DIVISION'
    elif divisionselected == '17':
        division = 'DEVONSHIRE DIVISION'
    elif divisionselected == '18':
        division = 'SOUTHEAST DIVISION'
    elif divisionselected == '19':
        division = 'MISSION DIVISION'
    elif divisionselected == '20':
        division = 'OLYMPIC DIVISION'
    elif divisionselected == '21':
        division = 'TOPANGA DIVISION'
    elif divisionselected == 'v':
        division = 'VALLEY BUREAU'   
    elif divisionselected == 's':
        division = 'SOUTH BUREAU' 
    elif divisionselected == 'c':
        division = 'CENTRAL BUREAU'
    elif divisionselected == 'w':
        division = 'WEST BUREAU'
    elif divisionselected == 'u':
        division = 'UNKNOWN LOCATION'
    elif divisionselected == 'q':
        print('\nExiting...\n')
        exit()
    else:
        print('\nInvalid selection. Please try again.\n')

# lasd
elif agencyselected == '2':
    agency = 'LASD'
    print("\n[1] CRESCENTA VLY / ALTA DENA")
    print("[2] WEST HOLLYWOOD")
    print("[3] EAST LA")
    print("[4] CENTURY")
    print("[5] SANTA CLARITA")
    print("[6] WALNUT / SAN DIMAS / DIAMOND BAR")
    print("[7] LOMITA / AVALON")
    print("[8] INDUSTRY")
    print("[9] CARSON / COMPTON")
    print("[10] MALIBU / LOST HILLS")
    print("[11] TEMPLE CITY")
    print("[12] SOUTH LA / MDR")
    print("[13] NORWALK / PICO RIVERA")
    print("[14] LAKEWOOD / CERRITOS")
    print("[15] LANCASTER / PALMDALE")
    print("[16] LAKE LA / ANTELOPE VALLEY")
    print("[17] TRANSIT SERVICES / COLLEGE SERVICES")
    print("[18] AERO")
    print("[19] SPECIAL UNITS / SWAT / BOMB / K9")
    print("[u] UNKNOWN LOCATION")
    print("[q] Quit")
    divisionselected = input("\nDivision or location: ")
    if divisionselected == '1':
        division = 'CRESCENTA VLY / ALTA DENA'
    elif divisionselected == '2':
        division = 'WEST HOLLYWOOD'
    elif divisionselected == '3':
        division = 'EAST LA'
    elif divisionselected == '4':
        division = 'CENTURY'
    elif divisionselected == '5':
        division = 'SANTA CLARITA'
    elif divisionselected == '6':
        division = 'WALNUT / SAN DIMAS / DIAMOND BAR'
    elif divisionselected == '7':
        division = 'LOMITA / AVALON'
    elif divisionselected == '8':
        division = 'INDUSTRY'
    elif divisionselected == '9':
        division = 'CARSON / COMPTON'
    elif divisionselected == '10':
        division = 'MALIBU / LOST HILLS'
    elif divisionselected == '11':
        division = 'TEMPLE CITY'
    elif divisionselected == '12':
        division = 'SOUTH LA / MDR'
    elif divisionselected == '13':
        division = 'NORWALK / PICO RIVERA'
    elif divisionselected == '14':
        division = 'LAKEWOOD / CERRITOS'
    elif divisionselected == '15':
        division = 'LANCASTER / PALMDALE'
    elif divisionselected == '16':
        division = 'LAKE LA / ANTELOPE VALLEY'
    elif divisionselected == '17':
        division = 'TRANSIT SERVICES / COLLEGE SERVICES'
    elif divisionselected == '18':
        division = 'AERO'
    elif divisionselected == '19':
        division = 'SPECIAL UNITS / SWAT / BOMB / K9'
    elif divisionselected == 'u':
        division = 'UNKNOWN LOCATION'
    elif divisionselected == 'q':
        print('\nExiting...\n')
        exit()
    else:
        print('\nInvalid selection. Please try again.\n')

# chp
elif agencyselected == '3':
    agency = 'CHP'
    print("\n[1] CENTRAL LA")
    print("[2] ALTADENA")
    print("[3] SANTA FE SPRINGS")
    print("[4] BALDWIN PARK")
    print("[5] WEST LA")
    print("[6] NEWHALL")
    print("[7] WEST VALLEY")
    print("[8] SOUTH LA")
    print("[9] EAST LA")
    print("[u] UNKNOWN LOCATION")
    print("[q] Quit")
    divisionselected = input("\nDivision or location: ")
    if divisionselected == '1':
        division = 'CENTRAL LA'
    elif divisionselected == '2':
        division = 'ALTADENA'
    elif divisionselected == '3':
        division = 'SANTE FE SPRINGS'
    elif divisionselected == '4':
        division = 'BALDWIN PARK'
    elif divisionselected == '5':
        division = 'WEST LA'
    elif divisionselected == '6':
        division = 'NEWHALL'
    elif divisionselected == '7':
        division = 'WEST VALLEY'
    elif divisionselected == '8':
        division = 'SOUTH LA'
    elif divisionselected == '9':
        division = 'EAST LA'
    elif divisionselected == 'u':
        division = 'UNKNOWN LOCATION'
    elif divisionselected == 'q':
        print('\nExiting...\n')
        exit()
    else:
        print('\nInvalid selection. Please try again.\n')
elif agencyselected == 'q':
    print('Exiting...\n')
    exit()

# assign crime variable
crime = input("\nDescribe incident:")

# verify things look correct. If they do, send the tweet. 
message = agency + ' ' + division + ': ' + crime.upper()
print('\n')
print(message)
correct = input('\nDoes everything appear correct? [y]/[n]:')
if correct == 'y':
    auth = tweepy.OAuthHandler(API, API_SECRET)
    auth.set_access_token(ACCESS, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(message)
else:
    exit()


