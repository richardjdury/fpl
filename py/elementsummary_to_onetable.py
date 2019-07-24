# --- Packages
import pandas as pd
import json
import time

# --- Time script
start = time.time()

# --- Empty dataframe for data
all_players = pd.DataFrame([])

# --- Choose columns from json file to keep
pCols = [
    'id', 'kickoff_time', 'fixture', 'team_h_score', 'team_a_score', 'round', 'total_points', 'minutes',
    'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
    'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity',
    'threat', 'ict_index', 'ea_index', 'open_play_crosses', 'big_chances_created',
    'clearances_blocks_interceptions', 'recoveries', 'key_passes', 'tackles', 'winning_goals',
    'attempted_passes', 'completed_passes', 'penalties_conceded', 'big_chances_missed',
    'errors_leading_to_goal', 'errors_leading_to_goal_attempt', 'tackled', 'offside', 'target_missed',
    'fouls', 'dribbles'
]

# --- Loop through all players "element-summary"'s
for i in range(1, 625):

    # --- empty dataframe for player
    player = pd.DataFrame([])

    # --- generate "element-summary" filename
    fn = '/home/rich/fpl/data/json/element-summary/' + str(i) + '.json'

    # --- open element-summary
    with open(fn, 'r') as f:
        data = json.load(f)

    # --- determine number of games played
    nGames = len(data['history'])

    # --- loop through all player's games and append to master table.
    for j in range(0, nGames):
        tmp_df = pd.DataFrame.from_dict(data['history'][j], orient='index').transpose()
        tmp_df = tmp_df[pCols]
        player = player.append(tmp_df, ignore_index=True)

    # --- Append to all_players
    all_players = all_players.append(player, ignore_index=True)

# --- save dataframe as csv
all_players.to_csv(r'/home/rich/github/fpl/data/csv/allplayers.csv')
print(all_players.shape)

# --- Stop timer
end = time.time()
print('Execution time: ' + str(end-start) + ' seconds.')
