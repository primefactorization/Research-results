from time import perf_counter
import concurrent.futures



def prime_factors_chunk(n, start, end):
    factors = []
    i = start
    while i <= end and i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 2
    return factors, n

def prime_factors(n, chunk_size=1000):

    # 奇数の範囲を設定
    start = 3
    step = 2
    super_2 =[]
    futures = []
    results = []

    # 2の因数を処理
    while (n % 2) == 0:
        super_2.append(2)
        n //= 2

    # チャンクごとに並列処理を実行
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while start * start <= n:
            chunk_end = start + step * chunk_size - step
            if chunk_end > n:
                chunk_end = n    
            # チャンクを分割して並列処理
            future = executor.submit(prime_factors_chunk, n, start, chunk_end)
            futures.append(future)
            start = chunk_end + step
        # タスクの順番で結果を取得
        for future in futures:
            chunk_factors, remaining_n = future.result()
            if n == remaining_n:
                continue
            if results:
                pass
            else:
                results.extend(chunk_factors)
                if remaining_n == 1:
                    if super_2:
                          results.extend(super_2)
                    return results
                continue

            if results:
                for ok in chunk_factors:
                    for tesuto in results:
                      if ok % tesuto == 0:
                          break
                      elif tesuto == results[-1]:
                          results.append(ok)
                          break
            else:
                results.extend(chunk_factors)
                 

    total = 1
    for i in results:
        total *= i
    if total < n:
        results.append(n//total)
    if super_2:
      results.extend(super_2)
    return results

# 数値のリスト
numbers = []
results = []
execution_times = []

# リスト内の各数について素因数分解を行う（複数回実行）
for num in numbers:
    times = []
    for _ in range(10):  # 10回実行
        start_time = perf_counter()
        if num <= 999999999:
            size= 10 ** len(str(num))-1
        else:
            size= 10 ** len(str(num))
        factors = prime_factors(num,chunk_size=size) # チャンクサイズ0
        end_time = perf_counter()
        execution_time = (end_time - start_time) * 1000  # ミリ秒単位
        times.append(execution_time)
    average_execution_time = sum(times) / len(times)
    results.append(factors)
    tesu = 1
    for i in factors:
        tesu *= i
    if num == tesu:
        pass
    else:
        exit("error" + str(num) + ":" + str(factors))

    execution_times.append(average_execution_time)

# 各数の素因数分解の平均実行時間を求める
overall_average_time = sum(execution_times) / len(execution_times)

# 結果をファイルに保存
with open("results.txt", "a") as f:
    for i, num in enumerate(numbers):
        f.write(f"{num} の素因数: {results[i]}\n")
        f.write(f"平均実行時間: {execution_times[i]:.6f} ミリ秒\n")
    f.write(f"\n {len(str(numbers[0]))}桁の全体の平均実行時間: {overall_average_time:.6f} ミリ秒\n")
