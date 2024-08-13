import time

# 素因数分解を行う関数
def prime_factors(n, prime_list):
    factors = []
    max_prime = prime_list[-1][-1]
    for primes in prime_list:
        for prime in primes:
            while n % prime == 0:
                factors.append(prime)
                n //= prime
            if n == 1:
                break
    # 素数リストが足りない場合、次の素数を探す
    candidate = max_prime + 2
    while candidate * candidate<= n:
        if n % candidate == 0:
            while n % candidate == 0:
              n //= candidate
              factors.append(candidate)
              if n == 1:
                return factors
        candidate += 2
    if n != 1:
        factors.append(n)
    return factors

def get_prime_list(filename):
    with open(filename, 'r') as f:
        content = f.read()
    prime_list = []
    for line in content.strip().split('\n'):
        primes = list(map(int, line.strip().split(',')))
        prime_list.append(primes)
    return prime_list

# 素数リストファイルのパス
prime_file = ""
prime_list = get_prime_list(prime_file)

# 数値のリスト
numbers =[]
# 結果を格納するリスト
results = []
execution_times = []

# リスト内の各数について素因数分解を行う（複数回実行）
for num in numbers:
    times = []
    for _ in range(10):  # 10回実行
        start_time = time.perf_counter()
        factors = prime_factors(num, prime_list)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # ミリ秒単位
        times.append(execution_time)
    average_execution_time = sum(times) / len(times)
    results.append(factors)
    execution_times.append(average_execution_time)

# 各数の素因数分解の平均実行時間を求める
overall_average_time = sum(execution_times) / len(execution_times)

# 結果をファイルに保存
with open("results.txt", "a") as f:
    for i, num in enumerate(numbers):
        f.write(f"{num} の素因数: {results[i]}\n")
        f.write(f"平均実行時間: {execution_times[i]:.6f} ミリ秒\n")
    f.write(f"\n{len(str(numbers[1]))}  桁の全体の平均実行時間: {overall_average_time:.6f} ミリ秒\n")
    

