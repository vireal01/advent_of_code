import re

f = open("../day_four_data.txt", "rt", encoding="utf8")


def get_final_score():
    cards_log = []
    for line in f:
        cards = line.strip().split(":")[1].split("|")
        cards.append("1")
        cards_log.append([x.replace("  ", " 0").strip().split(" ") for x in cards])

    ans = 0

    for index, card_log in enumerate(cards_log):
        counter = 0
        for card_numbers in card_log[0]:
            if card_numbers in card_log[1]:
                counter += 1
        for i in range(1, counter + 1):
            if index + i <= len(cards_log):
                cards_log[index + i][2][0] = str(int(cards_log[index + i][2][0]) + int(cards_log[index][2][0]))

    for card_log in cards_log:
        print(card_log[2])
        ans += int(card_log[2][0])

    print(ans)


get_final_score()
