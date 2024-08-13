import sympy
import time
import os
import decimal


stop = #素数の個数を入力

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
            #素数リストの文字数が10000を超えた場合にファイルに保存
            prime_str = ', '.join(prime_list)
            if count % 10000== 0:
                if count >= stop:
                    prime_str = ', '.join(prime_list)
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


def delta_encoding(primes):
    if not primes:
        return []
    deltas = [primes[0]]
    for i in range(1, len(primes)):
        deltas.append(primes[i] - primes[i-1])
    return deltas

def read_prime(file_path):
    with open(file_path, 'r') as file:
        prime = file.read().strip().split(',')
        prime = [int(p) for p in prime]
    return prime

#素数の読み込み
file_path = 'sosuu.txt'
prime_numbers = read_prime(file_path)

#実行
deltas_num = delta_encoding(prime_numbers)
with open("sosuu_angou.txt","w") as f:
    f.write(str(deltas_num)[1:-1])

#復元
def delta_decoding():
    with open("sosuu_angou.txt","r") as f:
        deltas_num = str(f.read()).split(",")
    if not deltas_num:
        return []
    prime_befor = int(deltas_num[0])
    primes = [prime_befor]
    for i in deltas_num[1:]:
        prime_befor += int(i)
        primes.append(prime_befor)
    return primes

time_list = []
for _ in range(5):
  start_time = time.perf_counter()
  reconstruction_primers = delta_decoding()
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  time_list.append(elapsed_time)
b = 0
for a in time_list:
    b = b+ a
b = b / 5

abc =decimal.Decimal(1024)

with open("results.txt","a") as f:
    f.write(str(stop) + "個の素数\n")
    f.write(f"{str(get_file_size('sosuu_angou.txt')/abc/abc)}\n")
    f.write(f"Elapsed time: {b} seconds\n
