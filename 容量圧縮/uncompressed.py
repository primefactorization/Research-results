import sympy
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
                    
                    print(get_file_size(file_path))
                    print(count)
                    file.close()
                    return prime_str
                clear_console()
                file.write(prime_str + ',')
                file_size = get_file_size(file_path)
                print(f"{file_size} bytes")
                prime_list = []
print(generate_primes(stop)[-20:-1])


abc =decimal.Decimal(1024)

with open("results.txt","a") as f:
    f.write(str(stop) + "個の素数\n")
    f.write(f"{str(get_file_size('sosuu.txt')/abc/abc)}\n")
    f.write("\n")
