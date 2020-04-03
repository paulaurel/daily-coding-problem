import random

NUM_CARDS = 52

def get_random_number(k):
    return random.randint(1, k)

def shuffle_card_deck():
    card_deck = [idx for idx in range(NUM_CARDS)]
    for end_idx in range(NUM_CARDS - 1, -1, -1):
        random_idx = get_random_number(end_idx + 1) - 1
        tmp_value = card_deck[end_idx]
        card_deck[end_idx] = card_deck[random_idx]
        card_deck[random_idx] = tmp_value
    return card_deck


for _ in range(10):
    assert all(x in shuffle_card_deck() for x in range(NUM_CARDS))
