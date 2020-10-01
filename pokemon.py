import requests
import random

def random_pokemon():
    player_card = random.randint(1, 151)
    opponent_card = random.randint(1, 151)
    player_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_card)
    opponent_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_card)
    player_response = requests.get(player_url).json()
    opponent_response = requests.get(opponent_url).json()

    playerCard = {
    'name': player_response['name'],
    'id': player_response['id'],
    'height': player_response['height'],
    'weight': player_response['weight']
}

    opponentCard = {
    'name': opponent_response ['name'],
    'id': opponent_response['id'],
    'height': opponent_response ['height'],
    'weight': opponent_response ['weight']
}
    return [playerCard, opponentCard]

def get_input():
    stat = input('enter statistic: ')
    stat = stat.lower()
    print('You have chosen to compare the Pokemon based on' ,stat,)
    return stat

def compare_pokemon():
    cards = random_pokemon()
    player = cards [0]
    opponent = cards [1]

    print("Player Card: ", player, "\n\n" "Opponent Card: ", opponent, "\n")

    user_input = get_input()
    player_stat = ''
    opponent_stat = ''
    if (user_input == 'id'):
        player_stat = player['id']
        opponent_stat = opponent['id']
        print(compare_stats(player_stat, opponent_stat))
    elif (user_input == 'height'):
        player_stat = player['height']
        opponent_stat = opponent['height']
        print(compare_stats(player_stat, opponent_stat))
    elif (user_input == 'weight'):
        player_stat = player['weight']
        opponent_stat = opponent['weight']
        print(compare_stats(player_stat, opponent_stat))
    else:
        print('{} is not a valid statistic'.format(user_input))

def compare_stats(player, opp):
    if (player > opp):
        return ("Player Wins!")
    elif (player < opp):
        return ("Opponent Wins!")
    else:
        return ("It's a draw!")

compare_pokemon()
