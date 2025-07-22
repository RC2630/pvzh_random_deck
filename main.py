from io import TextIOWrapper as File
from random import randint

HEROES: dict[str, tuple[str, str]] = {}
CARDS_BY_CLASS: dict[str, list[str]] = {}

heroes_file: File = open("data/heroes.txt", "r")
heroes_lines: list[str] = heroes_file.read().split("\n")
for line in heroes_lines:
    heroes_parts: list[str] = line.split(": ")
    hero_name: str = heroes_parts[0]
    classes: list[str] = heroes_parts[1].split(" ")
    HEROES[hero_name] = (classes[0], classes[1])
heroes_file.close()

cards_file: File = open("data/cards.txt", "r")
cards_lines: list[str] = cards_file.read().split("\n")
for line in cards_lines:
    cards_parts: list[str] = line.split(": ")
    class_name: str = cards_parts[0]
    cards: list[str] = cards_parts[1].split(", ")
    CARDS_BY_CLASS[class_name] = cards
cards_file.close()

hero: str = input("\nEnter hero: ")
while hero not in HEROES:
    hero = input("This is not a valid hero. Try again: ")

available_cards: list[str] = CARDS_BY_CLASS[HEROES[hero][0]] + CARDS_BY_CLASS[HEROES[hero][1]]
count_so_far: int = 0
deck: dict[str, int] = {}

while count_so_far < 40:
    random_index: int = randint(0, len(available_cards) - 1)
    random_count: int = randint(1, 4)
    if count_so_far + random_count > 40:
        random_count = 40 - count_so_far
    deck[available_cards[random_index]] = random_count
    count_so_far += random_count
    del available_cards[random_index]

print()
for card, count in deck.items():
    print(f"{count}x {card}")