import random

# ◯桁の乱数を10個生成（重複なし）
random_numbers = []
while len(random_numbers) < 10:
    num = random.randint(1000000000000000000000000000000000000000, 9999999999999999999999999999999999999999)
    if num not in random_numbers:
        random_numbers.append(num)

print(random_numbers)
