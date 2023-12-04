import re

symbols_cords = []
each_number_cords = {}


def calculate_ans():
    f = open("../day_three_data.txt", "rt", encoding="utf8")

    ans_sum = 0

    for line_coiner, line in enumerate(f):
        for ch_counter, ch in enumerate(line):
            if ch == "*":
                symbols_cords.append([int(line_coiner), int(ch_counter)])

    first_index_of_digit = -1
    is_counting_digit = False
    digit_as_string = ""
    f.close()

    f = open("../day_three_data.txt", "rt", encoding="utf8")
    for line_coiner, line in enumerate(f):
        for ch_counter, ch in enumerate(line):
            regexp = re.compile('[0-9]')
            if regexp.search(ch):
                if first_index_of_digit == - 1:
                    first_index_of_digit = ch_counter
                is_counting_digit = True
                digit_as_string += ch
            else:
                if is_counting_digit:
                    last_index_of_digit = ch_counter - 1
                    add_number_cords(first_index_of_digit, last_index_of_digit, line_coiner, digit_as_string)
                    first_index_of_digit = -1
                    is_counting_digit = False
                    digit_as_string = ""

    for symbols_cord in symbols_cords:
        value1 = 0
        value2 = 0
        star_neighbors_cords = get_possible_number_locations(symbols_cord[1], symbols_cord[0])

        for (cord_pair, number) in each_number_cords.items():
            if cord_pair in star_neighbors_cords:
                if value1 == 0:
                    value1 = number
                elif value2 == 0:
                    if value1 != number:
                        value2 = number
        ans_sum += value2 * value1
        continue
    f.close()

    return ans_sum


def add_number_cords(first_index_of_digit, last_index_of_digit, line_coiner, digit_as_string):
    list_of_pos_char_cords_loc = calculate_number_cords(first_index_of_digit, last_index_of_digit, line_coiner)
    for pair in list_of_pos_char_cords_loc:
        each_number_cords[str(pair)] = int(digit_as_string)


def calculate_number_cords(first_index_of_digit, last_index_of_digit, line_coiner):
    list_of_possible_characters_locations = []

    for i in range(first_index_of_digit, last_index_of_digit + 1):
        list_of_possible_characters_locations.append([line_coiner, i])
    return list_of_possible_characters_locations


def get_possible_number_locations(star_x_cord, line_coiner):
    possible_number_locations = [[line_coiner - 1, star_x_cord - 1], [line_coiner, star_x_cord - 1],
                                 [line_coiner + 1, star_x_cord - 1], [line_coiner - 1, star_x_cord],
                                 [line_coiner + 1, star_x_cord], [line_coiner, star_x_cord],
                                 [line_coiner - 1, star_x_cord + 1], [line_coiner, star_x_cord + 1],
                                 [line_coiner + 1, star_x_cord + 1]]
    return list(map(lambda x: str(x), possible_number_locations))


print(calculate_ans())
