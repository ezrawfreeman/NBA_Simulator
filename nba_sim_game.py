import random
import time
from nba_sim_data import * 
undrafted_players = players.copy()
player_team = {}
opp_team = {}

def assign_weights():

    weights = {

        # League averages
        "avg_half_trb": 22,
        "avg_half_ast": 12,
        "avg_team_defense": 35,

        # Team modifiers
        "trb_modifier": 0.015,
        "ast_modifier": 0.020,
        "defense_modifier": 0.020,

        # Performance distribution
        "performance_mean": 1.00,
        "performance_sd": 0.10,

        # Performance ranges
        "normal_min": 0.80,
        "normal_max": 1.25,

        "bad_min": 0.25,
        "bad_max": 0.80,

        "exceptional_min": 1.25,
        "exceptional_max": 2.00,

        "extreme_min": 2.00,
        "extreme_max": 2.50
    }

    return weights
weights = assign_weights()

def create_categories(team):

    # Team categories
    team["first_half_pts"] = 0
    team["first_half_trb"] = 0
    team["first_half_ast"] = 0
    team["first_half_def"] = 0
  
    

    team["second_half_pts"] = 0
    team["second_half_trb"] = 0
    team["second_half_ast"] = 0
    team["second_half_def"] = 0

    team["total_pts"] = 0
    team["total_trb"] = 0
    team["total_ast"] = 0
    team["total_def"] = 0

    for position in positions:
        player = team[position]

        # Player categories
        player["first_half_pts"] = 0
        player["first_half_trb"] = 0
        player["first_half_ast"] = 0
        player["first_half_def"] = 0

        player["second_half_pts"] = 0
        player["second_half_trb"] = 0
        player["second_half_ast"] = 0
        player["second_half_def"] = 0

        player["total_pts"] = 0
        player["total_trb"] = 0
        player["total_ast"] = 0
        player["total_def"] = 0

        player["game_score"] = 0
        player["rel_game_score"] = 0

def pregame_analysis(player_team, opp_team):
    print("\n==================== PREGAME ANALYSIS ====================\n")

    player_points = player_team["exp_pts"]
    opp_points = opp_team["exp_pts"]

    player_trb = player_team["exp_trb"]
    opp_trb = opp_team["exp_trb"]

    player_ast = player_team["exp_ast"]
    opp_ast = opp_team["exp_ast"]

    # Expected scoring comparison
    if player_points > opp_points:
        point_diff = player_points - opp_points
        print(f"Our sophisticated pregame analysis says that the "
              f"{player_team['name']} have a higher expected score "
              f"by {point_diff:.1f} points.")
    elif opp_points > player_points:
        point_diff = opp_points - player_points
        print(f"Our sophisticated pregame analysis says that the "
              f"{opp_team['name']} have a higher expected score "
              f"by {point_diff:.1f} points.")
    else:
        print("Our sophisticated pregame analysis says that the teams "
              "have identical expected scores.")

    # Rebound comparison
    if player_trb > opp_trb:
        trb_diff = player_trb - opp_trb
        print(f"The {player_team['name']} have a {trb_diff:.1f} advantage "
              f"in expected rebounds,")
    elif opp_trb > player_trb:
        trb_diff = opp_trb - player_trb
        print(f"The {opp_team['name']} have a {trb_diff:.1f} advantage "
              f"in expected rebounds,")
    else:
        print("The teams are even in expected rebounds,")

    # Assist comparison
    if player_ast > opp_ast:
        ast_diff = player_ast - opp_ast
        print(f"while the {player_team['name']} hold a {ast_diff:.1f} "
              f"edge in expected assists.")
    elif opp_ast > player_ast:
        ast_diff = opp_ast - player_ast
        print(f"while the {opp_team['name']} hold a {ast_diff:.1f} "
              f"edge in expected assists.")
    else:
        print("while the teams are even in expected assists.")

    # Create lists of the five players on each team
    player_list = [
        player_team["PG"],
        player_team["SG"],
        player_team["SF"],
        player_team["PF"],
        player_team["C"]
    ]

    opp_list = [
        opp_team["PG"],
        opp_team["SG"],
        opp_team["SF"],
        opp_team["PF"],
        opp_team["C"]
    ]

    # Find leading scorer on each team
    player_leader = max(player_list, key=lambda player: player["pts"])
    opp_leader = max(opp_list, key=lambda player: player["pts"])

    # Find best defender on each team
    player_defender = max(player_list, key=lambda player: player["defense"])
    opp_defender = max(opp_list, key=lambda player: player["defense"])

    print(f"The {player_team['name']} are looking to "
          f"{player_leader['name']} to lead them in scoring,")
    print(f"but {opp_defender['name']} of the {opp_team['name']} "
          f"will be doing his best to stop him.")

    print(f"The {opp_team['name']} are looking to "
          f"{opp_leader['name']} to lead them in scoring,")
    print(f"but {player_defender['name']} of the {player_team['name']} "
          f"will be doing his best to stop him.")

    print("\n==========================================================")

def announce_pick(position, player):
    print(f"Your {position} will be '{random.choice(player['nicknames'])},' {player['name']}!")

def choose_random_team():
    chosen_team = {}
    chosen_team['name'] = random.choice(random_cities) + " " + random.choice(random_team_names)
    #print(f"This team is the {chosen_team['name']}.")
    for position in positions:
        chooser = random.randint(1,10)
        if chooser == 1:
            chosen_team[position] = create_average_player(position)
        elif chooser == 2:
            chosen_team[position] = create_all_star_player(position)
        else:
            while True:
                try_this_player = random.choice(undrafted_players)
    
                if position in try_this_player["positions"]:
                    chosen_team[position] = try_this_player
                    undrafted_players.remove(try_this_player)
                    break
    return chosen_team

def choose_franchise():

    print("\nChoose an NBA franchise.")
    print("Type a team name, 'list' to see teams, or 'r' for random.")

    while True:

        choice = input("Franchise: ").strip()

        if choice.lower() == "list":
            print("\nAvailable franchises:")
            for team in franchises:
                print(team)

        elif choice.lower() in ["r", "ran", "random"]:
            chosen_franchise = random.choice(franchises)
            print(f"\nRandomly selected: {chosen_franchise}")
            return chosen_franchise

        else:
            for team in franchises:
                if choice.lower() == team.lower():
                    return team

            print("I didn't recognize that franchise.")

def filter_by_franchise(player_pool, franchise):
    filtered_players = []

    for player in player_pool:
        if franchise in player["teams"]:
            filtered_players.append(player)

    return filtered_players           

def choose_draft_mode():

    print("Here are your options:")
    print(
        "1) Choose by Position\n"
        "2) Choose by Franchise\n"
        "3) Choose by Era or ABA\n"
        "4) Choose by Franchise & Era\n"
        "5) Random Team"
    )

    while True:

        choice = input("Which would you like to do? ")

        if choice == "1":
            player_pool = undrafted_players
            player_team = draft_players(player_pool)

            player_team["name"] = input(
                "Now name this team, or hit enter to get a random name: "
            )

            if player_team["name"] == "":
                player_team["name"] = random_team_name()

            return player_team

        elif choice == "2":
            franchise = choose_franchise()
            player_pool = filter_by_franchise(
                undrafted_players,
                franchise
            )

            player_team = draft_players(player_pool)
            player_team["name"] = franchise

            return player_team

        elif choice == "3":
            eras = choose_eras()
            player_pool = filter_by_era(
                undrafted_players,
                eras
            )

            player_team = draft_players(player_pool)

            player_team["name"] = input(
                "Now name this team, or hit enter to get a random name: "
            )

            if player_team["name"] == "":
                player_team["name"] = random_team_name()

            return player_team

        elif choice == "4":
            player_pool = choose_team_and_era()
            player_team = draft_players(player_pool)

            player_team["name"] = input(
                "Now name this team, or hit enter to get a random name: "
            )

            if player_team["name"] == "":
                player_team["name"] = random_team_name()

            return player_team

        elif choice == "5":
            return choose_random_team()

        else:
            print("Please choose a number from 1-5.")

def choose_eras():

    era_options = {
        "1": "1950s",
        "2": "1960s",
        "3": "1970s",
        "4": "1980s",
        "5": "1990s",
        "6": "2000s",
        "7": "2010s",
        "8": "2020s",
        "9": "ABA"
    }

    chosen_eras = []

    print("\nChoose one or more eras.")
    
    for number, era in era_options.items():
        print(f"{number}) {era}")

    print("Type 'done' when finished.")

    while True:

        choice = input("Era choice: ").lower()

        if choice == "done":
            break

        if choice.lower() == 'aba':
            choice = "ABA"     
            
        if choice in era_options:
            chosen_era = era_options[choice]

            if chosen_era not in chosen_eras:
                chosen_eras.append(chosen_era)
                print(f"Added {chosen_era}")

            else:
                print("You already selected that era.")

        else:
            print("Please choose a number 1-8 or type done.")

    player_pool = []

    for player in undrafted_players:
        for era in player["eras"]:
            if era in chosen_eras:
                player_pool.append(player)
                break

    return chosen_eras

def choose_team_and_era():
    franchise = choose_franchise()
    eras = choose_eras()
    player_pool = filter_by_franchise_and_era(
        undrafted_players,
        franchise,
        eras
    )
    return player_pool

def filter_by_franchise_and_era(player_pool, franchise, eras):

    filtered_players = []

    print("LOOKING FOR:", franchise, eras)

    for player in player_pool:

        franchise_match = franchise in player["teams"]

        era_match = False

        for era in player["eras"]:
            if era in eras:
                era_match = True

        if franchise_match and era_match:
            
            filtered_players.append(player)

    print("TOTAL MATCHES:", len(filtered_players))

    return filtered_players

def filter_by_era(player_pool, eras):

    filtered_players = []

    print("LOOKING FOR ERAS:", eras)

    for player in player_pool:

        era_match = False

        for era in player["eras"]:
            if era in eras:
                era_match = True

        if era_match:
            print("MATCH:", player["name"])
            filtered_players.append(player)

    print("TOTAL MATCHES:", len(filtered_players))

    return filtered_players


def draft_players(player_pool):
    chosen_team = {}

    for position in positions:

        available_players = []

        for player in player_pool:
            if position in player["positions"]:
                available_players.append(player)

        print(f"\nAvailable {position}s:")

        player_list = []

        for player in available_players:
            player_list.append(
                f"{player['name']}, '{random.choice(player['nicknames'])}'"
            )

        for i in range(0, len(player_list), 4):
            for player in player_list[i:i + 4]:
                print(f"{player:<40}", end="")
            print()

        print()

        # Emergency fallback if no players exist for this position
        if len(available_players) == 0:
            print(f"No available {position}s found in this player pool.")

            while position not in chosen_team:
                choice = input(
                    "Type 'reg' for a random NBA player, "
                    "'as' for an All-Star, or press Enter for random: "
                )

                if choice.lower() == "reg":
                    chosen_team[position] = create_average_player(position)

                elif choice.lower() == "as":
                    chosen_team[position] = create_all_star_player(position)

                elif choice == "":
                    chosen_team[position] = create_average_player(position)

                else:
                    print("Sorry, I didn't understand that.")

            announce_pick(position, chosen_team[position])
            continue

        while position not in chosen_team:

            choice = input(
                "Enter a player's name, 'reg' for an average starter, "
                "'as' for an All-Star, or press Enter for random: "
            )

            if choice.lower() == "reg":
                chosen_team[position] = create_average_player(position)
                announce_pick(position, chosen_team[position])

            elif choice.lower() == "as":
                chosen_team[position] = create_all_star_player(position)
                announce_pick(position, chosen_team[position])

            elif choice == "":
                chosen_team[position] = random.choice(available_players)
                announce_pick(position, chosen_team[position])

                player_pool.remove(chosen_team[position])

            else:
                for player in available_players:
                    if (
                        choice.lower() == player["name"].lower()
                        or choice.lower() == player["name"].split()[0].lower()
                    ):
                        chosen_team[position] = player
                        announce_pick(position, chosen_team[position])

                        player_pool.remove(player)

                        break

                if position not in chosen_team:
                    print("Sorry, I didn't understand that.")

    return chosen_team

def choose_opponent():

    print("\nNow choose an opposing team.")
    print(
    "1) Totally Random Team\n"
    "2) Easy Opponent\n"
    "3) Hard Opponent\n"
    "4) Franchise All-Stars\n"
    "5) Choose by Position"
)

    while True:
        choice = input("What kind of opponent would you like? ")

        if choice == "1":
            return choose_random_team()

        elif choice == "2":
            return create_opponent("easy")

        elif choice == "3":
            return create_opponent("hard")

        elif choice == "4":
            return choose_franchise_opponent()

        elif choice == "5":
            opponent_team = draft_players(undrafted_players.copy())

            opponent_team["name"] = input(
                "Now name this team, or hit enter to get a random name: "
            )

            if opponent_team["name"] == "":
                opponent_team["name"] = random_team_name()

            return opponent_team
        else:
                    print("Please choose a number from 1-5.")

def create_opponent(difficulty):

    if difficulty == "easy":
        average_chance = 50
        all_star_chance = 25

    elif difficulty == "hard":
        average_chance = 20
        all_star_chance = 30

    opponent_team = {}
    opponent_team['name'] = random.choice(random_cities) + " " + random.choice(random_team_names)
    print(f"This team is the {opponent_team['name']}.")

    for position in positions:

        roll = random.randint(1, 100)

        if roll <= average_chance:
            player = create_average_player(position)

        elif roll <= average_chance + all_star_chance:
            player = create_all_star_player(position)

        else:
            available_players = []

            for player in undrafted_players:
                if position in player["positions"]:
                    available_players.append(player)

            if len(available_players) > 0:
                player = random.choice(available_players)
                undrafted_players.remove(player)

            else:
                player = create_all_star_player(position)

        opponent_team[position] = player

    return opponent_team

def choose_franchise_opponent():

    print("\nChoose the franchise for your opponent.")

    while True:

        choice = input(
            "Enter a franchise name, 'list' for a list of franchises, "
            "'random' or press Enter for a random franchise: "
        )

        if choice == "" or choice.lower() == "random":
            franchise = random.choice(franchises)
            print(f"\nYour opponent will be the {franchise}!")
            break

        elif choice.lower() == "list":
            print("\nAvailable franchises:")
            for franchise in franchises:
                print(franchise)

        else:
            for team in franchises:
                if choice.lower() == team.lower():
                    franchise = team
                    print(f"\nYour opponent will be the {franchise}!")
                    break

            if "franchise" in locals():
                break

            print("Sorry, I didn't recognize that franchise.")

    return create_franchise_opponent(franchise)

def create_franchise_opponent(franchise):


    opponent_team = {}
    opponent_team = {
            "name": franchise
        }
    for position in positions:

        available_players = []

        for player in undrafted_players:
            if franchise in player["teams"] and position in player["positions"]:
                available_players.append(player)

        if len(available_players) > 0:
            player = random.choice(available_players)
            opponent_team[position] = player
            undrafted_players.remove(player)

        else:
            print(
                f"No {position} players remain for the {franchise}. "
                f"Using an All-Star replacement."
            )
            opponent_team[position] = create_all_star_player(position)

    return opponent_team

def get_expected_team_stats(team):
       
    team['exp_pts'] = 0
    team['exp_trb'] = 0
    team['exp_ast'] = 0
    team['exp_def'] = 0

    for position in positions:
        team['exp_pts'] += team[position]['pts']
        team['exp_trb'] += team[position]['trb']
        team['exp_ast'] += team[position]['ast']
        team['exp_def'] += team[position]['defense']

    team['exp_def'] /= 5

    team['exp_pts'] = round(team['exp_pts'], 1)
    team['exp_trb'] = round(team['exp_trb'], 1)
    team['exp_ast'] = round(team['exp_ast'], 1)
    team['exp_def'] = round(team['exp_def'], 1)

    print(f"The {team['name']} will, on average, score {team['exp_pts']} points, generate {team['exp_ast']} assists,")
    print(f"pull down {team['exp_trb']} rebounds,"
    f"and have an average defensive rating of {team['exp_def']}/10.")

def announce_team(team):
    print("--------------------------------------------")
    print(f"Presenting the {team['name']}:")
    for position in positions:
        print(f"At {position} is {team[position]['name']}, "
              f"drafted from the {random.choice(team[position]['eras'])} "
              f"{random.choice(team[position]['teams'])}, now playing for your {team['name']}!")
        print(f"{team[position]['name'].split()[0]} '{random.choice(team[position]['nicknames'])}' "
              f"{team[position]['name'].split()[-1]} averages "
              f"{team[position]['pts']} points, "
              f"{team[position]['trb']} rebounds, and "
              f"{team[position]['ast']} assists, "
              f"with a defensive rating of {team[position]['defense']}/10.")
        print()
    get_expected_team_stats(team)
    print("--------------------------------------------")
    print()

def normal_action(team):
    player = team[random.choice(positions)]
    if random.randint(1,4) == 1:
        nick = random.choice(player['nicknames'])
        print(f"{nick} {random.choice(all_actions)}!")
    else:
        print(f"{player['name']} {random.choice(all_actions)}!")

def special_action(player_team, opp_team, half):

    players = []

    for position in positions:
        players.append(player_team[position])
        players.append(opp_team[position])

    category = random.randint(1, 4)

    if category == 1:
        player = max(players, key=lambda player: player[f"{half}_pts"])
        action = random.choice(scoring_actions)

    elif category == 2:
        player = max(players, key=lambda player: player[f"{half}_trb"])
        action = random.choice(rebound_actions)

    elif category == 3:
        player = max(players, key=lambda player: player[f"{half}_ast"])
        action = random.choice(assist_actions)

    else:
        player = max(players, key=lambda player: player[f"{half}_def"])
        action = random.choice(defense_actions)

    nickname = random.choice(player["nicknames"])
    
    if random.randint(1,2) == 1:
        print(f"{nickname} {action}!")
    else:
        print(f"{player['name']} {action}!")

def play_half(half):

    calculate_nonscoring_stats(player_team, half)
    calculate_nonscoring_stats(opp_team, half)

    calculate_scoring_stats(player_team, opp_team, half)
    calculate_scoring_stats(opp_team, player_team, half)

    time.sleep(.75)
    normal_action(random.choice([player_team, opp_team]))

    time.sleep(.75)
    special_action(player_team, opp_team, half)

    time.sleep(.75)
    print("And that's the end of the quarter...")

    time.sleep(.75)
    normal_action(random.choice([player_team, opp_team]))

    time.sleep(.75)
    special_action(player_team, opp_team, half)


def performance_randomizer():

    roll = random.random()

    if roll < 0.80:
        return random.uniform(
            weights["normal_min"],
            weights["normal_max"]
        )

    elif roll < 0.89:
        return random.uniform(
            weights["bad_min"],
            weights["bad_max"]
        )

    elif roll < 0.98:
        return random.uniform(
            weights["exceptional_min"],
            weights["exceptional_max"]
        )

    else:
        return random.uniform(
            weights["extreme_min"],
            weights["extreme_max"]
        )

def calculate_nonscoring_stats(team, half):

    if half == "first_half":
        trb = "first_half_trb"
        ast = "first_half_ast"
        defense = "first_half_def"
        team_trb = "first_half_trb"
        team_ast = "first_half_ast"
        team_def = "first_half_def"

    elif half == "second_half":
        trb = "second_half_trb"
        ast = "second_half_ast"
        defense = "second_half_def"
        team_trb = "second_half_trb"
        team_ast = "second_half_ast"
        team_def = "second_half_def"

    else:
        print("Half must be 'first' or 'second'.")
        return

    for position in positions:

        player = team[position]

        player[trb] = round(
            player["trb"] * 0.55 * random.uniform(0.8, 1.25)
        )

        player[ast] = round(
            player["ast"] * 0.55 * random.uniform(0.8, 1.25)
        )

        player[defense] = round(
            player["defense"] * random.uniform(0.8, 1.25),
            1
        )

    team[team_trb] = 0
    team[team_ast] = 0
    team[team_def] = 0

    for position in positions:

        player = team[position]

        team[team_trb] += player[trb]
        team[team_ast] += player[ast]
        team[team_def] += player[defense]

def calculate_scoring_stats(team, opponent, half):

    # Calculate team-level modifiers

    rebound_differential = (
        team[f"{half}_trb"] - weights["avg_half_trb"]
    )

    rebound_variance = (
        1 + rebound_differential * weights["trb_modifier"]
    )

    assist_differential = (
        team[f"{half}_ast"] - weights["avg_half_ast"]
    )

    assist_variance = (
        1 + assist_differential * weights["ast_modifier"]
    )

    defense_differential = (
    opponent[f"{half}_def"] - weights["avg_team_defense"]
    )   

    defense_variance = (
        1 - defense_differential * weights["defense_modifier"]
    )

    # Calculate individual scoring

    for position in positions:

        player = team[position]

        performance_variance = performance_randomizer()

        expected_points = player["pts"] * 0.5

        player[f"{half}_pts"] = round(
            expected_points
            * performance_variance
            * rebound_variance
            * assist_variance
            * defense_variance
        )

    # Add individual scoring into team scoring

    team[f"{half}_pts"] = 0

    for position in positions:
        team[f"{half}_pts"] += team[position][f"{half}_pts"]

def display_stats(player_team, opp_team, half):

    print()
    print(f"==================== {half.upper()} STATS ====================")
    print()

    for team in [player_team, opp_team]:

        print(team["name"])
        print("-" * 50)
        print(f"{'Player':25} {'PTS':>6} {'TRB':>6} {'AST':>6}")

        for position in positions:
            player = team[position]

            pts = player[f"{half}_pts"]
            trb = player[f"{half}_trb"]
            ast = player[f"{half}_ast"]

            print(f"{player['name']:25} {pts:>6} {trb:>6} {ast:>6}")

        print("-" * 50)

        team_pts = team[f"{half}_pts"]
        team_trb = team[f"{half}_trb"]
        team_ast = team[f"{half}_ast"]

        print(f"{team['name']:25} {team_pts:>6} {team_trb:>6} {team_ast:>6}")
        print()

def calculate_game_score(player_team, opp_team):

    for team in [player_team, opp_team]:

        for position in ["PG", "SG", "SF", "PF", "C"]:

            player = team[position]

            total_pts = player["first_half_pts"] + player["second_half_pts"]
            total_trb = player["first_half_trb"] + player["second_half_trb"]
            total_ast = player["first_half_ast"] + player["second_half_ast"]

            player["game_score"] = (
                total_pts
                + (total_trb * 0.7)
                + (total_ast * 0.7)
            )

def display_final_box_score(player_team, opp_team):

    print("\n==================== FINAL BOX SCORE ====================\n")

    all_players = []
    team_results = []

    for team in [player_team, opp_team]:

        print(team["name"])
        print("-" * 105)

        print(
            f"{'Pos':<5}"
            f"{'Player':<25}"
            f"{'PTS':>13}"
            f"{'REB':>13}"
            f"{'AST':>13}"
            f"{'Game Score':>16}"
            f"{'DEF':>10}"
        )

        print("-" * 105)

        # Team totals
        team_pts = 0
        team_trb = 0
        team_ast = 0
        team_def = 0
        team_game_score = 0

        for position in ["PG", "SG", "SF", "PF", "C"]:

            player = team[position]

            # Combine the two halves
            total_pts = (
                player["first_half_pts"]
                + player["second_half_pts"]
            )

            total_trb = (
                player["first_half_trb"]
                + player["second_half_trb"]
            )

            total_ast = (
                player["first_half_ast"]
                + player["second_half_ast"]
            )

            total_def = (
                player["first_half_def"]
                + player["second_half_def"]
            )

            # Add to team totals
            team_pts += total_pts
            team_trb += total_trb
            team_ast += total_ast
            team_def += total_def

            # Difference from player's averages
            pts_diff = total_pts - player["pts"]
            trb_diff = total_trb - player["trb"]
            ast_diff = total_ast - player["ast"]

            # Game Score
            game_score = player["game_score"]

            expected_game_score = (
                player["pts"]
                + (player["trb"] * 0.7)
                + (player["ast"] * 0.7)
            )

            game_score_diff = (
                game_score - expected_game_score
            )

            # Defensive performance
            expected_def = player["defense"] * 2
            def_diff = total_def - expected_def

            team_game_score += game_score

            # Save player information for later analysis
            all_players.append({
                "name": player["name"],
                "position": position,
                "team": team["name"],
                "pts": total_pts,
                "trb": total_trb,
                "ast": total_ast,
                "def": total_def,
                "game_score": game_score,
                "game_score_diff": game_score_diff,
                "def_diff": def_diff
            })

            print(
                f"{position:<5}"
                f"{player['name']:<30}"
                f"{total_pts:>5} ({pts_diff:+.1f})"
                f"{total_trb:>5} ({trb_diff:+.1f})"
                f"{total_ast:>5} ({ast_diff:+.1f})"
                f"{game_score:>8.1f} ({game_score_diff:+.1f})"
                f"{total_def:>7.1f} ({def_diff:+.1f})"
            )

        # --------------------------------------------------
        # TEAM TOTALS
        # --------------------------------------------------

        team_pts_diff = team_pts - team["exp_pts"]

        expected_team_trb = weights["avg_half_trb"] * 2
        expected_team_ast = weights["avg_half_ast"] * 2

        team_trb_diff = team_trb - expected_team_trb
        team_ast_diff = team_ast - expected_team_ast

        # Team Game Score
        expected_team_game_score = 0

        for position in ["PG", "SG", "SF", "PF", "C"]:

            player = team[position]

            expected_team_game_score += (
                player["pts"]
                + (player["trb"] * 0.7)
                + (player["ast"] * 0.7)
            )

        team_game_score_diff = (
            team_game_score - expected_team_game_score
        )

        # Team defense
        expected_team_def = team["exp_def"] * 2
        team_def_diff = team_def - expected_team_def

        print("-" * 105)

        print(
            f"{'ALL':<5}"
            f"{team['name']:<25}"
            f"{team_pts:>5} ({team_pts_diff:+.1f})"
            f"{team_trb:>5} ({team_trb_diff:+.1f})"
            f"{team_ast:>5} ({team_ast_diff:+.1f})"
            f"{team_game_score:>8.1f} ({team_game_score_diff:+.1f})"
            f"{team_def:>7.1f} ({team_def_diff:+.1f})"
        )

        print()

        # Save team information for later analysis
        team_results.append({
            "name": team["name"],
            "pts": team_pts,
            "trb": team_trb,
            "ast": team_ast,
            "def": team_def,
            "game_score": team_game_score,
            "pts_diff": team_pts_diff,
            "trb_diff": team_trb_diff,
            "ast_diff": team_ast_diff,
            "game_score_diff": team_game_score_diff,
            "def_diff": team_def_diff
        })

    # ======================================================
    # GAME ANALYSIS
    # ======================================================

    print("==================== GAME ANALYSIS ====================\n")

    # Player of the Game
    player_of_game = max(
        all_players,
        key=lambda player: player["game_score"]
    )

    print(
        f"PLAYER OF THE GAME: {player_of_game['name']} "
        f"({player_of_game['team']})"
    )
    print(
        f"Game Score: {player_of_game['game_score']:.1f}"
    )
    print()

    # Top scorer
    top_scorer = max(
        all_players,
        key=lambda player: player["pts"]
    )

    print(
        f"TOP SCORER: {top_scorer['name']} "
        f"({top_scorer['team']})"
    )
    print(
        f"Points: {top_scorer['pts']}"
    )
    print()

    # Top rebounder
    top_rebounder = max(
        all_players,
        key=lambda player: player["trb"]
    )

    print(
        f"TOP REBOUNDER: {top_rebounder['name']} "
        f"({top_rebounder['team']})"
    )
    print(
        f"Rebounds: {top_rebounder['trb']}"
    )
    print()

    # Top assister
    top_assister = max(
        all_players,
        key=lambda player: player["ast"]
    )

    print(
        f"TOP ASSIST MAN: {top_assister['name']} "
        f"({top_assister['team']})"
    )
    print(
        f"Assists: {top_assister['ast']}"
    )
    print()

    # Overachiever
    overachiever = max(
        all_players,
        key=lambda player: player["game_score_diff"]
    )

    print(
        f"OVERACHIEVER: {overachiever['name']} "
        f"({overachiever['team']})"
    )
    print(
        f"Performance vs. Expected: "
        f"{overachiever['game_score_diff']:+.1f}"
    )
    print()

    # Underachiever
    underachiever = min(
        all_players,
        key=lambda player: player["game_score_diff"]
    )

    print(
        f"UNDERACHIEVER: {underachiever['name']} "
        f"({underachiever['team']})"
    )
    print(
        f"Performance vs. Expected: "
        f"{underachiever['game_score_diff']:+.1f}"
    )
    print()

    # Best defensive performance
    best_defender = max(
        all_players,
        key=lambda player: player["def"]
    )

    print(
        f"TOP DEFENSIVE PERFORMANCE: {best_defender['name']} "
        f"({best_defender['team']})"
    )
    print(
        f"Defense: {best_defender['def']:.1f} "
        f"({best_defender['def_diff']:+.1f})"
    )
    print()

    # Triple-doubles
    triple_doubles = []

    for player in all_players:

        categories = [
            player["pts"],
            player["trb"],
            player["ast"]
        ]

        if sum(stat >= 10 for stat in categories) >= 3:
            triple_doubles.append(player)

    if triple_doubles:

        print("TRIPLE-DOUBLE ALERT!")

        for player in triple_doubles:
            print(
                f"{player['name']} ({player['team']}): "
                f"{player['pts']} PTS, "
                f"{player['trb']} REB, "
                f"{player['ast']} AST"
            )

        print()

    # Team statistical comparison
    player_result = team_results[0]
    opponent_result = team_results[1]

    print("TEAM STATISTICAL BATTLES")
    print("------------------------")

    if player_result["trb"] > opponent_result["trb"]:
        print(
            f"Rebounds: {player_result['name']} "
            f"+{player_result['trb'] - opponent_result['trb']:.0f}"
        )
    elif opponent_result["trb"] > player_result["trb"]:
        print(
            f"Rebounds: {opponent_result['name']} "
            f"+{opponent_result['trb'] - player_result['trb']:.0f}"
        )
    else:
        print("Rebounds: Even")

    if player_result["ast"] > opponent_result["ast"]:
        print(
            f"Assists: {player_result['name']} "
            f"+{player_result['ast'] - opponent_result['ast']:.0f}"
        )
    elif opponent_result["ast"] > player_result["ast"]:
        print(
            f"Assists: {opponent_result['name']} "
            f"+{opponent_result['ast'] - player_result['ast']:.0f}"
        )
    else:
        print("Assists: Even")

    if player_result["def"] > opponent_result["def"]:
        print(
            f"Defense: {player_result['name']} "
            f"+{player_result['def'] - opponent_result['def']:.1f}"
        )
    elif opponent_result["def"] > player_result["def"]:
        print(
            f"Defense: {opponent_result['name']} "
            f"+{opponent_result['def'] - player_result['def']:.1f}"
        )
    else:
        print("Defense: Even")

    print("\n========================================================")

def who_won(player_team, opp_team):

    player_score = player_team["first_half_pts"] + player_team["second_half_pts"]
    opp_score = opp_team["first_half_pts"] + opp_team["second_half_pts"]

    if player_score > opp_score:
        winner = player_team
        winner_score = player_score
        loser_score = opp_score

        input(
            f"The {winner['name']} win, "
            f"{winner_score} to {loser_score}! "
            f"Press enter for full final box score."
        )

    elif opp_score > player_score:
        winner = opp_team
        winner_score = opp_score
        loser_score = player_score

        input(
            f"And the {winner['name']} win, "
            f"{winner_score} to {loser_score}! "
            f"Press enter for full final box score."
        )

    else:
        input(
            f"We have a tie! "
            f"{player_score} to {opp_score}. "
            f"And we rejoice in shared victory! "
            f"Press enter for full final box score."
        )

# Program starts here

print("-------------------------------------------------------------------")
print("Welcome to Ezra's ultimate NBA Simulator!")
print("-------------------------------------------------------------------")

# The player chooses their team
player_team = choose_draft_mode()
announce_team(player_team)

# An opponent team is created
opp_team = choose_opponent()
announce_team(opp_team)

playing = True

while playing:

    # Reset all game-specific stats
    create_categories(player_team)
    create_categories(opp_team)

    # Some pregame analysis
    input("Let's go to Inside the NBA for some pregame analysis.  Press enter to see what Ernie, Kenny, Chuck, and Shaq think of this matchup... ")
    pregame_analysis(player_team, opp_team)

    # Now we play basketball
    nothing = input("Now let's play some basketball!  Hit enter to continue")
    center = random.choice([player_team["C"], opp_team["C"]])
    print(f"{center['name']} wins the opening tip...")
    play_half("first_half")

    print(
        f"Halftime! The score at halftime is "
        f"{player_team['name']}: {player_team['first_half_pts']} "
        f"to {opp_team['name']}: {opp_team['first_half_pts']}."
    )

    input("Press Enter to see first half stats \n ")
    display_stats(player_team, opp_team, "first_half")

    print()
    input("Start of the third quarter!  Press Enter to continue...")
    play_half("second_half")

    print("And that's the game!")
    who_won(player_team, opp_team)
    display_stats(player_team, opp_team, "second_half")
    calculate_game_score(player_team, opp_team)
    display_final_box_score(player_team, opp_team)

    # Replay menu
    print()
    print("What would you like to do?")
    print("1) Same team, same opponent")
    print("2) Same team, different opponent")
    print("3) Different teams")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pass

    elif choice == "2":
        opp_team = choose_opponent()
        announce_team(opp_team)

    elif choice == "3":
        player_team = choose_draft_mode()
        announce_team(player_team)

        opp_team = choose_opponent()
        announce_team(opp_team)

    elif choice == "4":
        playing = False
        print("Good-bye, it's been a pleasure playing Ezra's Ultimate NBA Simulator with you.")