import time
import sympy

# SymPyを使用して素因数分解を行う関数
def prime_factors(n):
    return sympy.primefactors(n)

# 数値のリスト
numbers = []

# 結果を格納するリスト
results = []
execution_times = []

# リスト内の各数について素因数分解を行う（複数回実行）
for num in numbers:
    times = []
    for _ in range(10):  # 10回実行
        start_time = time.perf_counter()
        factors = prime_factors(num)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # ミリ秒単位
        times.append(execution_time)
    average_execution_time = sum(times) / len(times)
    results.append(factors)
    execution_times.append(average_execution_time)

# 各数の素因数分解の平均実行時間を求める
overall_average_time = sum(execution_times) / len(execution_times)

# 結果をファイルに保存
with open("sympy.txt", "a") as f:
    for i, num in enumerate(numbers):
        f.write(f"{num} の素因数: {results[i]}\n")
        f.write(f"平均実行時間: {execution_times[i]:.6f} ミリ秒\n")
    f.write(f"\n全体の平均実行時間: {overall_average_time:.6f} ミリ秒\n")
