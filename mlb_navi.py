import googlemaps
import geocoder
from datetime import timedelta
import dateutil.parser
import statsapi  # please, install statsapi first ## pip install MLB-StatsAPI ##
from bs4 import BeautifulSoup

gmaps = googlemaps.Client(key='Your API KEY')

mylocation = geocoder.ip('me')
origin = mylocation.latlng  # GPS, my location
# origin = {'lat': 34.1899, 'lng': -118.4514} #Van Nuys, CA
# origin = {'lat': 40.7128, 'lng': -74.0060} #New York
# origin = {'lat': 41.8781, 'lng': -87.6298} #Chicago
# origin = {'lat': 37.7749, 'lng': -122.4194} #San Francisco
# origin = {'lat': 47.6062, 'lng': -122.3321} #Seattle
# origin = {'lat': 47.5515, 'lng': -101.0020} #North Dakota, where no human is.... index error exception

places_result = gmaps.places_nearby(
    location=origin, keyword='mlb', radius=50000, open_now=False, type='stadium')

# each team id gets game info and check home game and get game info


def game_info_detail(team_id):
    game_id = statsapi.next_game(team_id)
    home_game_check(game_id, team_id)
    game_info(game_id)


def game_info(gameid):
    statsapi.schedule(game_id=gameid)
    get_wrong_game_time = dateutil.parser.parse(statsapi.schedule(
        game_id=gameid)[0]['game_datetime'])  # change datetime format
    # statsapi's time is 7 hours later, so I used timedelta
    adjust_game_time = get_wrong_game_time - timedelta(hours=7)
    game_time = adjust_game_time.strftime('%H:%M:%S')

    game_date = statsapi.schedule(game_id=gameid)[0]['game_date']
    home_team = statsapi.schedule(game_id=gameid)[0]['home_name']
    away_team = statsapi.schedule(game_id=gameid)[0]['away_name']
    home_probable_pitcher = statsapi.schedule(
        game_id=gameid)[0]['home_probable_pitcher']
    away_probable_pitcher = statsapi.schedule(
        game_id=gameid)[0]['away_probable_pitcher']

    game_time_string = 'Next game will be at {} on {}'
    home_team_string = 'Home team, Probable Pitcher: {} // {}'
    away_team_string = 'Away team, Probable Pitcher: {} // {}'
    print(game_time_string.format(game_time, game_date))
    print(home_team_string.format(home_team, home_probable_pitcher))
    print(away_team_string.format(away_team, away_probable_pitcher))

# home game check


def home_game_check(gameid, teamid):
    if statsapi.schedule(game_id=gameid)[0]['away_name'] == statsapi.lookup_team(teamid)[0]['name']:
        print('There is no home game!')

# check stadium name is matched with specific teams name and get its info


def get_game_info():
    if places_result['results'][0]['name'] == 'Angel Stadium of Anaheim':
        team_id = 108
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Dodger Stadium':
        team_id = 119
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Yankee Stadium':
        team_id = 147
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Citi Field':
        team_id = 121
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Globe Life Park in Arlington':
        team_id = 140
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Minute Maid Park':
        team_id = 117
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Oakland-Alameda County Coliseum':
        team_id = 133
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'T-Mobile Park':
        team_id = 136
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Tropicana Field':
        team_id = 139
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Fenway Park':
        team_id = 111
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Rogers Centre':
        team_id = 141
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Oriole Park at Camden Yards':
        team_id = 110
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Target Field':
        team_id = 142
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Oracle Park':
        team_id = 137
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Progressive Field':
        team_id = 114
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Guaranteed Rate Field':
        team_id = 145
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Wrigley Field':
        team_id = 112
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Comerica Park':
        team_id = 116
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Kauffman Stadium':
        team_id = 118
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Miller Park':
        team_id = 158
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Busch Stadium':
        team_id = 138
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Great American Ball Park':
        team_id = 113
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'PNC Park':
        team_id = 134
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Coors Field':
        team_id = 115
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Chase Field':
        team_id = 109
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Petco Park':
        team_id = 135
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'SunTrust Park':
        team_id = 144
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Citizens Bank Park':
        team_id = 143
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Nationals Park':
        team_id = 120
        game_info_detail(team_id)
    if places_result['results'][0]['name'] == 'Marlins Park':
        team_id = 146
        game_info_detail(team_id)


try:
    destination = places_result['results'][0]['geometry']['location']
    directions_result = gmaps.directions(origin, destination)
    # Check if there is only one stadium nearby
    if places_result['results'][0] == places_result['results'][-1]:
        print('Closest mlb stadium is: ', places_result['results'][0]['name'])
        print("")
        get_game_info()
        print("")
        print('distance is :',
              directions_result[0]['legs'][0]['distance']['text'])
        print('duration is :',
              directions_result[0]['legs'][0]['duration']['text'])
        print("")
        for step in directions_result[0]['legs'][0]['steps']:
            # used Beautifulsoup to get text only
            soup = BeautifulSoup(step['html_instructions'], 'html.parser')
            print(step['distance']['text'], ',', step['duration']
                  ['text'], ',', soup.get_text())
    else:  # If there are two results(I believe maximum 2 results are allowed, as long as I get right information)
        try:  # find closest one.
            destination_1 = places_result['results'][1]['geometry']['location']
            directions_result_1 = gmaps.directions(origin, destination_1)
            if int(directions_result[0]['legs'][0]['distance']['value']) < int(
                    directions_result_1[0]['legs'][0]['distance']['value']):  # comparison by distance value
                print("There are two mlb stadium near your location : ",
                      places_result['results'][0]['name'], ",", places_result['results'][1]['name'])
                print('Closest mlb stadium is: ',
                      places_result['results'][0]['name'])
                print("")
                get_game_info()
                print("")
                print('distance is :',
                      directions_result[0]['legs'][0]['distance']['text'])
                print('duration is :',
                      directions_result[0]['legs'][0]['duration']['text'])
                print("")
                for step in directions_result[0]['legs'][0]['steps']:
                    soup = BeautifulSoup(
                        step['html_instructions'], 'html.parser')
                    print(step['distance']['text'], ',',
                          step['duration']['text'], ',', soup.get_text())
            elif int(directions_result[0]['legs'][0]['distance']['value']) > int(
                    directions_result_1[0]['legs'][0]['distance']['value']):
                print("There are two mlb stadium near your location : ",
                      places_result['results'][0]['name'], ",", places_result['results'][1]['name'])
                print('Closest mlb stadium is: ',
                      places_result['results'][1]['name'])
                print("")
                get_game_info()
                print("")
                print('distance is :',
                      directions_result_1[0]['legs'][0]['distance']['text'])
                print('duration is :',
                      directions_result_1[0]['legs'][0]['duration']['text'])
                print("")
                for step in directions_result_1[0]['legs'][0]['steps']:
                    soup = BeautifulSoup(
                        step['html_instructions'], 'html.parser')
                    print(step['distance']['text'], ',',
                          step['duration']['text'], ',', soup.get_text())
        except IndexError:
            pass
except IndexError:
    # index error unless there is result
    print('There is no mlb stadium nearby!')
