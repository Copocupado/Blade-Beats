from random import randint

from Config.window_config import *
from Sprites.fruit import Fruit

side_chosen = None
delay = 0

bpm = 88

one_beat = round(60 / bpm * 1000)
half_beat = round(one_beat / 2)
quarter_beat = round(half_beat / 2)
eight_beat = round(quarter_beat / 2)


def get_last_timestamp(dict):
    if dict:
        return max(dict.keys())
    else:
        return None


def pulse_camera_timestamps(bpm=88, beats=1000):
    beat_duration_ms = 60000 / bpm
    initial_delay = 1100
    return [round(initial_delay + beat_duration_ms * i) for i in range(1, beats + 1)]


def level_increase_timestamps():
    return [delay + 33000, delay + 80000]


def chorus_timestamp():
    return (delay + 57100) / 1000


def last_timestamp():
    return get_last_timestamp(song())


def song():
    dict = {}

    dict[delay + 1100] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3))
    dict.update(first_chorus(get_last_timestamp(dict) + one_beat * 3))

    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(vou_cacar_refrao(get_last_timestamp(dict) + one_beat))

    dict[get_last_timestamp(dict)] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(23):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(7):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    side_chosen = Fruit.sides_to_spawn[randint(0, 1)]
    opposite_side = 'Left' if side_chosen == 'Right' else 'Right'
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_chosen
    }
    dict[get_last_timestamp(dict) + eight_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': opposite_side
    }
    dict[get_last_timestamp(dict) + eight_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': side_chosen
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': opposite_side
    }

    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(15):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    # vem
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(37):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(6):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(20):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(vou_cacar_refrao(get_last_timestamp(dict) + one_beat * 4 + half_beat + quarter_beat))

    # Faco do teus bracos
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(9):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(3):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(14):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(5):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(6):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    for _ in range(7):
        timestamp = get_last_timestamp(dict) + quarter_beat
        dict[timestamp] = {
            'is_long': False,
            'health': 1,
            'double': False,
            'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
        }

    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict.update(vou_cacar_refrao(get_last_timestamp(dict) + half_beat))

    return dict


def first_chorus(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    return dict


def vou_cacar_refrao(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {  # VOOOUUUUU
        'is_long': True,
        'health': one_beat / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': one_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    dict[get_last_timestamp(dict) + one_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': (one_beat + half_beat) / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }  # AIIIIII

    dict[get_last_timestamp(dict) + one_beat * 2 + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    # EEUUUUU
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': one_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': True,
        'health': half_beat / 1000,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': one_beat * 2 / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat * 2 + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': True,
        'health': (one_beat * 2) / 1000,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat * 3] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }

    return dict


"""
def apos_primeiro_refrao(timestamp, varation=1):
    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + one_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': True,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    dict[get_last_timestamp(dict) + half_beat + quarter_beat] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    return dict


def apos_segundo_refrao(timestamp, variation=1):
    dict = {}

    dict[timestamp] = {
        'is_long': False,
        'health': 1,
        'double': False,
        'side_to_spawn': Fruit.sides_to_spawn[randint(0, 1)]
    }
    return dict

"""
