import re

max_possible_values = {"red": 12, "green": 13, "blue": 14}


# 12 red cubes, 13 green cubes, and 14 blue cubes

def get_score(score_log: str):
    game_log = []
    rounds = score_log.strip().split(";")
    for round in rounds:
        round_stats = {"red": 0, "green": 0, "blue": 0}
        score_arr = round.strip().split(",")
        for score in score_arr:
            color = re.compile('[^a-zA-Z]').sub("", score)
            number = int(re.compile('\D+').sub("", score))
            round_stats[color] = number
        game_log.append(round_stats)
    return game_log


def get_game_data_array(set_data):
    # set_data = "Game 1: 3 green, 1 blue, 3 red; 3 blue, 1 green, 3 red; 2 red, 12 green, 7 blue; 1 red, 4 blue, 5 green; 7 green, 2 blue, 2 red"
    ans = []
    row = re.compile('\D').sub('', set_data.split(":")[0])
    set_data = set_data.split(":")[1]
    ans.append(row)
    ans.append(get_score(set_data))
    return ans


# step 1 answer
def is_game_possible(game_data_array: list[str, list]):
    for set in game_data_array[1]:
        for (color, number) in set.items():
            if number > max_possible_values[color]:
                return 0
    return int(game_data_array[0])


# step 2
def get_fewest_cubes_for_game(game_data_array: list[str, list]):
    min_cubes_required = {"red": 0, "green": 0, "blue": 0}
    for set in game_data_array[1]:
        for (color, number) in set.items():
            if number >= min_cubes_required[color]:
                min_cubes_required[color] = number
    return min_cubes_required


def get_multiplied_value(fewest_cubes_for_game):
    ans = 1
    for (color, number) in fewest_cubes_for_game.items():
        ans *= number
    return ans


f = open("../day_two_data.txt", "rt", encoding="utf8")
ans_step_one = 0
ans_step_two = 0
for line in f:
    ans_step_one += is_game_possible(get_game_data_array(line))
    ans_step_two += get_multiplied_value(get_fewest_cubes_for_game(get_game_data_array(line)))

print(ans_step_one)
print(ans_step_two)
