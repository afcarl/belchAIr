from config import COLORS
from color_dict import ColorDict


def color_combinations(mana_cost):
    always = ColorDict(mana_cost)
    colorless_remaining = mana_cost['Colorless']
    del always['Colorless']
    options = fill_up_remaining_colors(colorless_remaining, COLORS, always, [])
    return options


def fill_up_remaining_colors(colorless_remaining, remaining_colors, spent_so_far, options):
    for index, color in enumerate(remaining_colors):
        newly_spent = spent_so_far.copy()
        newly_spent[color] += 1
        if colorless_remaining == 1:
            options.append(newly_spent)
        else:
            fill_up_remaining_colors(colorless_remaining-1, remaining_colors[index:],
                                     newly_spent, options)
    return options

print(fill_up_remaining_colors(1, ['R', 'G'], ColorDict(), []))