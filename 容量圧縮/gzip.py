import sympy
import time
import os
import decimal


stop =  # ここに停止条件の値を設定

def clear_console():
    os.system('clear')

def get_file_size(file_path):
    return os.path.getsize(file_path)

def generate_primes(stop):
    file_path = 'sosuu.txt'
    count = 0
    prime_gen = sympy.primerange(1, sympy.oo)
    prime_list = []
    file = open(file_path, 'w')
    while True:
        for prime in prime_gen:
            prime_list.append(str(prime))
            count += 1
            # 素数リストの文字数が10000を超えた場合にファイルに保存
            prime_str = ', '.join(prime_list)
            if count % 10000 == 0:
                if count >= stop:
                    file.write(prime_str)
                    print(get_file_size(file_path))
                    print(count)
                    file.close()
                    return None
                clear_console()
                file.write(prime_str + ',')
                file_size = get_file_size(file_path)
                print(f"{file_size} bytes")
                prime_list = []
                time.sleep(0.005)

generate_primes(stop)

time.sleep(2)

import gzip

# バイト化関数
def encode_primes(input_file, output_file):
    with open(input_file, 'r') as file:
        prime_numbers = file.read().strip()
    byte_data = prime_numbers.encode('utf-8')
    with gzip.open(output_file, 'wb') as file:
        file.write(byte_data)

# 復元関数
def decode_primes(input_file, output_file):   
    with gzip.open(input_file, 'rb') as file:
        byte_data = file.read()
    prime_numbers = byte_data.decode('utf-8')

input_file = 'sosuu.txt'  # 素数のファイル
encoded_file = 'encoded_primes.gz'  # 圧縮されたファイル
decoded_file = 'decoded_primes.txt'  # 復元されたデータ

encode_primes(input_file, encoded_file)

# デコードの実行時間を測定
time_list = []
for _ in range(5):
    start_time = time.perf_counter()
    decode_primes(encoded_file, decoded_file)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    time_list.append(elapsed_time)

average_time = sum(time_list) / 5

# ファイルサイズの計算
kilobyte = decimal.Decimal(1024)

# 結果のファイルに書き込む
with open("results.txt", "a") as f:
    f.write(str(stop) + "個の素数\n")
    f.write(f"{str(get_file_size(encoded_file) / kilobyte / kilobyte)[:8]} MB\n")
    f.write(f"Elapsed time: {average_time} seconds\n")
