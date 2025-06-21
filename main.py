leaders = [
    ("Ваня", 6, 20),
    ("Егор", 7, 30),
    ("Андрей", 7, 50),
]
def print_leaders(leaders: list[tuple[str, int, int]], formatted: bool = True, file_name: str = None) -> None:
    if formatted:
        a = "Имя\t   Игры\tОчки\n"
        a += "-" * 20 + "\n"
        for name, games, points in leaders:
            a += f"{name}\t{games}\t{points}\n"
    else:
        a = "\n".join(f"{name},{games},{points}" for name, games, points in leaders)

    print(a)

    if file_name:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(a)
# Вывод в файл в формате с форматированием
print_leaders(leaders, formatted=True, file_name='leaders_formatted.txt')