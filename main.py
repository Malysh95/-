def print_hollow_diamond(size=5):
    """
    Рисует пустой ромбик из символов '0'
    """
    n = size
    total_rows = 2 * n - 1

    for i in range(total_rows):
        # Определяем уровень (строку) относительно центра ромба
        if i < n:
            # Верхняя половина
            left_pos = n - i - 1
            right_pos = n + i - 1
        else:
            # Нижняя половина
            j = i - n + 1
            left_pos = j
            right_pos = total_rows - j - 1

        line = ""
        for pos in range(total_rows):
            if pos == left_pos or pos == right_pos:
                line += "0"
            else:
                line += " "
        print(line)


print_hollow_diamond(5)