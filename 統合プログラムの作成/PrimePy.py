import time
from primePy import primes

# primePyを使用して素因数分解を行う関数
def prime_factors(n):
    return primes.factors(n)
    
# 結果を格納するリスト
results = []
execution_times = []

# 数値のリスト
numbers = []

# 結果を格納するリスト
results = []
execution_times = []

# リスト内の各数について素因数分解を行う（複数回実行）
for num in numbers:
    start_time = time.perf_counter()
    factors = prime_factors(num)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # ミリ秒単位
    results.append(factors)
    execution_times.append(execution_time)
overall_average_time = sum(execution_times) / len(execution_times)

# 結果をファイルに保存
with open("results.txt", "a") as f:
    f.write(f"\n{len(str(numbers[1]))}  桁の全体の平均実行時間: {overall_average_time:.6f} ミリ秒\n")
