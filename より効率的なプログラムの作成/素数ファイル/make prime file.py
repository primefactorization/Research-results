import sympy
import time
import os

def generate_primes(stop):
    file_path = f'sosuu{str(stop)}.txt'

    def clear_console():
        os.system('clear')

    def get_file_size(path):
        return os.path.getsize(path)

    count = 0
    prime_gen = sympy.primerange(1, sympy.oo)
    prime_list = []

    with open(file_path, 'a') as file:
        while True:
            for prime in prime_gen:
                prime_list.append(str(prime))
                count += 1

                # 1000個ごとに出力して短いスリープを挟む
                if count % 1000 == 0:
                    print(f"{count}個の素数を生成しました")

                    # 素数の桁数が指定された桁数以上になったら終了
                    if len(str(prime_list[-1])) >= stop + 1:
                        prime_str = ', '.join(prime_list)
                        file.write(prime_str + ',')
                        print(get_file_size(file_path))
                        exit()

                    time.sleep(0.005)

                # 素数リストの要素数が10000を超えた場合にファイルに保存
                if count % 10000 == 0:
                    clear_console()
                    file_size = get_file_size(file_path)
                    print(f"{file_size} bytes")
                    prime_str = ', '.join(prime_list)
                    file.write(prime_str + ',')
                    prime_list = []

stop = #ここに桁数を入力
generate_primes(stop)
