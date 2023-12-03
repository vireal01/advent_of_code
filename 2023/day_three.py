import re

symbols_cords = []


def calculate_ans():
    f = open("../day_three_data.txt", "rt", encoding="utf8")

    ans_sum = 0

    for line_coiner, line in enumerate(f):
        for ch_counter, ch in enumerate(line):
            regexp = re.compile('[^0-9a-zA-Z \n.]')
            if regexp.search(ch):
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
                    ans_sum += check_is_any_character_around_number(first_index_of_digit, last_index_of_digit, line_coiner, digit_as_string)
                    first_index_of_digit = -1
                    is_counting_digit = False
                    digit_as_string = ""
    return ans_sum



def check_is_any_character_around_number(first_index_of_digit, last_index_of_digit, line_coiner, digit_as_string):
    ans = 0
    print(digit_as_string)
    list_of_pos_char_cords_loc = get_possible_chars_locations(first_index_of_digit, last_index_of_digit, line_coiner)
    for pos_char_cords_loc in list_of_pos_char_cords_loc:
        if pos_char_cords_loc in symbols_cords:
            return int(digit_as_string)
    return 0


def get_possible_chars_locations(first_index_of_digit, last_index_of_digit, line_coiner):
    list_of_possible_characters_locations = []

    print((first_index_of_digit, last_index_of_digit))

    list_of_possible_characters_locations.append([line_coiner - 1, first_index_of_digit - 1])
    list_of_possible_characters_locations.append([line_coiner, first_index_of_digit - 1])
    list_of_possible_characters_locations.append([line_coiner + 1, first_index_of_digit - 1])

    # list_of_possible_characters_locations.append([line_coiner - 1, first_index_of_digit])
    # list_of_possible_characters_locations.append([line_coiner, first_index_of_digit])
    # list_of_possible_characters_locations.append([line_coiner + 1, first_index_of_digit])

    for i in range(first_index_of_digit, last_index_of_digit+1):
        list_of_possible_characters_locations.append([line_coiner - 1, i])
        list_of_possible_characters_locations.append([line_coiner + 1, i])

    list_of_possible_characters_locations.append([line_coiner - 1, last_index_of_digit + 1])
    list_of_possible_characters_locations.append([line_coiner, last_index_of_digit + 1])
    list_of_possible_characters_locations.append([line_coiner + 1, last_index_of_digit + 1])

    # list_of_possible_characters_locations.append([line_coiner - 1, last_index_of_digit])
    # list_of_possible_characters_locations.append([line_coiner, last_index_of_digit])
    # list_of_possible_characters_locations.append([line_coiner + 1, last_index_of_digit])
    print(list_of_possible_characters_locations)
    return list_of_possible_characters_locations


print(calculate_ans())
