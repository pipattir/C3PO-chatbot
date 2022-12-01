import random


def random_string():
    random_list = [
        "Sometimes, I just don’t understand human behaviour.",
        "I beg your pardon, but what do you mean?",
        "You watch your language!",
        "Don’t blame me. I’m an interpreter.",
        "I’m programmed for etiquette, not destruction!",
        "Oh my goodness! Shut me down."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
