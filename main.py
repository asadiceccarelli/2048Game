import tkinter as tk
import random

window = tk.Tk()
window.title('2048')

intro = tk.Label(
    text='Welcome to the 2048 game.'
)
intro.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
zero_zero = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
zero_zero.grid(row=2, column=1, padx=5, pady=5)
zero_one = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
zero_one.grid(row=2, column=2, padx=5, pady=5)
zero_two = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
zero_two.grid(row=2, column=3, padx=5, pady=5)
zero_three = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
zero_three.grid(row=2, column=4, padx=5, pady=5)
one_zero = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
one_zero.grid(row=3, column=1, padx=5, pady=5)
one_one = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
one_one.grid(row=3, column=2, padx=5, pady=5)
one_two = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
one_two.grid(row=3, column=3, padx=5, pady=5)
one_three = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
one_three.grid(row=3, column=4, padx=5, pady=5)
two_zero = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
two_zero.grid(row=4, column=1, padx=5, pady=5)
two_one = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
two_one.grid(row=4, column=2)
two_two = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
two_two.grid(row=4, column=3, padx=5, pady=5)
two_three = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
two_three.grid(row=4, column=4, padx=5, pady=5)
three_zero = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
three_zero.grid(row=5, column=1, padx=5, pady=5)
three_one = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
three_one.grid(row=5, column=2, padx=5, pady=5)
three_two = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
three_two.grid(row=5, column=3, padx=5, pady=5)
three_three = tk.Label(width=4, height=2, font=('Helvetica bold', 40), bg='white')
three_three.grid(row=5, column=4, padx=5, pady=5)

game_over = tk.Label(width=8, height=4)
game_over.grid(row=1, column=0, columnspan=5)

tiles = [zero_zero, zero_one, zero_two, zero_three,
         one_zero, one_one, one_two, one_three,
         two_zero, two_one, two_two, two_three,
         three_zero, three_one, three_two, three_three]


def get_tile_value(tile):
    if tile['text'] == '':
        tile_value = 0
    else:
        tile_value = int(tile['text'])
    return tile_value


def only_empty_tiles(udlr, first, second, third, forth):
    if udlr == 'up':
        options = [12, 13, 14, 15]
        if first != 0:
            options.remove(12)
        if second != 0:
            options.remove(13)
        if third != 0:
            options.remove(14)
        if forth != 0:
            options.remove(15)
        return options
    if udlr == 'down':
        options = [0, 1, 2, 3]
        if first != 0:
            options.remove(0)
        if second != 0:
            options.remove(1)
        if third != 0:
            options.remove(2)
        if forth != 0:
            options.remove(3)
        return options
    if udlr == 'left':
        options = [3, 7, 11, 15]
        if first != 0:
            options.remove(3)
        if second != 0:
            options.remove(7)
        if third != 0:
            options.remove(11)
        if forth != 0:
            options.remove(15)
        return options
    if udlr == 'right':
        options = [0, 4, 8, 12]
        if first != 0:
            options.remove(0)
        if second != 0:
            options.remove(4)
        if third != 0:
            options.remove(8)
        if forth != 0:
            options.remove(12)
        return options


def tile_colour(tile):
    if tile == 2:
        return '#fffcf2'
    elif tile == 4:
        return '#fef2c9'
    elif tile == 8:
        return '#ffe799'
    elif tile == 16:
        return '#ffdb68'
    elif tile == 32:
        return '#ffd037'
    elif tile == 64:
        return '#ffc406'
    elif tile == 128:
        return '#d4a200'
    elif tile == 256:
        return '#a37d00'
    elif tile == 512:
        return '#725700'
    elif tile == 1024:
        return '#413200'
    elif tile == 2048:
        return '#100c00'
    else:
        return 'white'


def up_pressed():
    first_column = [tiles[0], tiles[4], tiles[8], tiles[12]]
    first_column_values = []
    for tile in first_column:
        first_column_values.append(get_tile_value(tile))
    second_column = [tiles[1], tiles[5], tiles[9], tiles[13]]
    second_column_values = []
    for tile in second_column:
        second_column_values.append(get_tile_value(tile))
    third_column = [tiles[2], tiles[6], tiles[10], tiles[14]]
    third_column_values = []
    for tile in third_column:
        third_column_values.append(get_tile_value(tile))
    forth_column = [tiles[3], tiles[7], tiles[11], tiles[15]]
    forth_column_values = []
    for tile in forth_column:
        forth_column_values.append(get_tile_value(tile))

    tiles_reconstructed = [first_column_values, second_column_values, third_column_values, forth_column_values]

    j = 0
    while j <= 3:
        for column in tiles_reconstructed:
            i = 3
            while i >= 1:
                if column[i] == column[i - 1]:
                    column[i - 1] += column[i]
                    column[i] = 0
                elif column[i - 1] == 0:
                    column[i - 1] = column[i]
                    column[i] = 0
                i -= 1
        j += 1

    tiles_reconstructed_list = [first_column_values[0], second_column_values[0], third_column_values[0],
                                forth_column_values[0],
                                first_column_values[1], second_column_values[1], third_column_values[1],
                                forth_column_values[1],
                                first_column_values[2], second_column_values[2], third_column_values[2],
                                forth_column_values[2],
                                first_column_values[3], second_column_values[3], third_column_values[3],
                                forth_column_values[3]]

    try:
        tiles_reconstructed_list[random.choice(only_empty_tiles('up', first_column_values[3], second_column_values[3],
                                                                third_column_values[3], forth_column_values[3]))]\
            = random.choice([2, 4])
    except IndexError:
        print('Up not available')

    i = 0
    for tile_value in tiles_reconstructed_list:
        if tile_value == 0:
            tiles[i]['text'] = ''
        else:
            tiles[i]['text'] = tile_value
        tiles[i]['bg'] = tile_colour(tile_value)
        i += 1


def down_pressed():
    first_column = [tiles[12], tiles[8], tiles[4], tiles[0]]
    first_column_values = []
    for tile in first_column:
        first_column_values.append(get_tile_value(tile))
    second_column = [tiles[13], tiles[9], tiles[5], tiles[1]]
    second_column_values = []
    for tile in second_column:
        second_column_values.append(get_tile_value(tile))
    third_column = [tiles[14], tiles[10], tiles[6], tiles[2]]
    third_column_values = []
    for tile in third_column:
        third_column_values.append(get_tile_value(tile))
    forth_column = [tiles[15], tiles[11], tiles[7], tiles[3]]
    forth_column_values = []
    for tile in forth_column:
        forth_column_values.append(get_tile_value(tile))

    tiles_reconstructed = [first_column_values, second_column_values, third_column_values, forth_column_values]

    j = 0
    while j <= 3:
        for column in tiles_reconstructed:
            i = 3
            while i >= 1:
                if column[i] == column[i - 1]:
                    column[i - 1] += column[i]
                    column[i] = 0
                elif column[i - 1] == 0:
                    column[i - 1] = column[i]
                    column[i] = 0
                i -= 1
        j += 1

    tiles_reconstructed_list = [first_column_values[3], second_column_values[3], third_column_values[3],
                                forth_column_values[3],
                                first_column_values[2], second_column_values[2], third_column_values[2],
                                forth_column_values[2],
                                first_column_values[1], second_column_values[1], third_column_values[1],
                                forth_column_values[1],
                                first_column_values[0], second_column_values[0], third_column_values[0],
                                forth_column_values[0]]

    try:
        tiles_reconstructed_list[random.choice(only_empty_tiles('down', first_column_values[3], second_column_values[3],
                                                                third_column_values[3],
                                                                forth_column_values[3]))] = random.choice([2, 4])
    except IndexError:
        print('Down not available')

    i = 0
    for tile_value in tiles_reconstructed_list:
        if tile_value == 0:
            tiles[i]['text'] = ''
        else:
            tiles[i]['text'] = tile_value
        tiles[i]['bg'] = tile_colour(tile_value)
        i += 1


def left_pressed():
    first_row = [tiles[0], tiles[1], tiles[2], tiles[3]]
    first_row_values = []
    for tile in first_row:
        first_row_values.append(get_tile_value(tile))
    second_row = [tiles[4], tiles[5], tiles[6], tiles[7]]
    second_row_values = []
    for tile in second_row:
        second_row_values.append(get_tile_value(tile))
    third_row = [tiles[8], tiles[9], tiles[10], tiles[11]]
    third_row_values = []
    for tile in third_row:
        third_row_values.append(get_tile_value(tile))
    forth_row = [tiles[12], tiles[13], tiles[14], tiles[15]]
    forth_row_values = []
    for tile in forth_row:
        forth_row_values.append(get_tile_value(tile))

    tiles_reconstructed = [first_row_values, second_row_values, third_row_values, forth_row_values]

    j = 0
    while j <= 3:
        for row in tiles_reconstructed:
            i = 3
            while i >= 1:
                if row[i] == row[i - 1]:
                    row[i - 1] += row[i]
                    row[i] = 0
                elif row[i - 1] == 0:
                    row[i - 1] = row[i]
                    row[i] = 0
                i -= 1
        j += 1

    tiles_reconstructed_list = [first_row_values[0], first_row_values[1], first_row_values[2],
                                first_row_values[3],
                                second_row_values[0], second_row_values[1], second_row_values[2],
                                second_row_values[3],
                                third_row_values[0], third_row_values[1], third_row_values[2],
                                third_row_values[3],
                                forth_row_values[0], forth_row_values[1], forth_row_values[2],
                                forth_row_values[3]]

    try:
        tiles_reconstructed_list[random.choice(only_empty_tiles('left', first_row_values[3], second_row_values[3],
                                                                third_row_values[3],
                                                                forth_row_values[3]))] = random.choice([2, 4])
    except IndexError:
        print('Left not available')

    i = 0
    for tile_value in tiles_reconstructed_list:
        if tile_value == 0:
            tiles[i]['text'] = ''
        else:
            tiles[i]['text'] = tile_value
        tiles[i]['bg'] = tile_colour(tile_value)
        i += 1


def right_pressed():
    first_row = [tiles[3], tiles[2], tiles[1], tiles[0]]
    first_row_values = []
    for tile in first_row:
        first_row_values.append(get_tile_value(tile))
    second_row = [tiles[7], tiles[6], tiles[5], tiles[4]]
    second_row_values = []
    for tile in second_row:
        second_row_values.append(get_tile_value(tile))
    third_row = [tiles[11], tiles[10], tiles[9], tiles[8]]
    third_row_values = []
    for tile in third_row:
        third_row_values.append(get_tile_value(tile))
    forth_row = [tiles[15], tiles[14], tiles[13], tiles[12]]
    forth_row_values = []
    for tile in forth_row:
        forth_row_values.append(get_tile_value(tile))

    tiles_reconstructed = [first_row_values, second_row_values, third_row_values, forth_row_values]

    j = 0
    while j <= 3:
        for row in tiles_reconstructed:
            i = 3
            while i >= 1:
                if row[i] == row[i - 1]:
                    row[i - 1] += row[i]
                    row[i] = 0
                elif row[i - 1] == 0:
                    row[i - 1] = row[i]
                    row[i] = 0
                i -= 1
        j += 1

    tiles_reconstructed_list = [first_row_values[3], first_row_values[2], first_row_values[1],
                                first_row_values[0],
                                second_row_values[3], second_row_values[2], second_row_values[1],
                                second_row_values[0],
                                third_row_values[3], third_row_values[2], third_row_values[1],
                                third_row_values[0],
                                forth_row_values[3], forth_row_values[2], forth_row_values[1],
                                forth_row_values[0]]

    try:
        tiles_reconstructed_list[random.choice(only_empty_tiles('right', first_row_values[3], second_row_values[3],
                                                                third_row_values[3],
                                                                forth_row_values[3]))] = random.choice([2, 4])
    except IndexError:
        print('Right not available')

    i = 0
    for tile_value in tiles_reconstructed_list:
        if tile_value == 0:
            tiles[i]['text'] = ''
        else:
            tiles[i]['text'] = tile_value
        tiles[i]['bg'] = tile_colour(tile_value)
        i += 1


def game_over(list_of_tiles):
    if list_of_tiles.count(0) == 0:
        print('Game Over')


up_button = tk.Button(text='Up', command=up_pressed)
up_button.grid(row=6, column=2, columnspan=2)
down_button = tk.Button(text='Down', command=down_pressed)
down_button.grid(row=8, column=2, columnspan=2)
left_button = tk.Button(text='Left', command=left_pressed)
left_button.grid(row=7, column=2)
right_button = tk.Button(text='Right', command=right_pressed)
right_button.grid(row=7, column=3)

window.mainloop()
