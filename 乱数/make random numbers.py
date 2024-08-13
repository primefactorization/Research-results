import random

number_len =#ここに数字の桁数を入力
star = 10 ** number_len
end = 10 ** (number_len + 1)
# ◯桁の乱数を10個生成（重複なし）
random_numbers = []
while len(random_numbers) < 10:
    num = random.randint(start, end)
    if num not in random_numbers:
        random_numbers.append(num)

print(random_numbers)
