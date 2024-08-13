import time
import gzip
import numpy as np

def get_bases(bit_length):
    # ビット数に応じた確定的な基底数リストを返す
    if bit_length <= 32:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif bit_length <= 64:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    elif bit_length <= 128:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
    elif bit_length <= 256:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
                157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
                239, 241, 251]
    elif bit_length <= 512:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
                157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
                239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
                331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 
                421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 
                509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 
                613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
                709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 
                821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 
                919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    else:
        return False

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    def miller_rabin_test(d, n, a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    bit_length = n.bit_length()
    bases = get_bases(bit_length)
    if not bases:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in bases:
        if a >= n:
            continue
        if n == a:
            return True
        if not miller_rabin_test(d, n, a):
            return False

    return True

def prime_factors_small(n):
    factors = []
    i = 2
    while (n % i) == 0:
        factors.append(i)
        n //= i
    i = 3
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return factors

def prime_factors(n, prime_list, max_prime):
    factors = []
    if is_prime(n):
        factors.append(n)
        return factors
    for prime in prime_list:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
            if n == 1:
                break
            if is_prime(n):
                factors.append(n)
                return factors
    # 素数リストが足りない場合、次の素数を探す
    candidate = max_prime + 2
    while candidate * candidate <= n:
        if n % candidate == 0:
            while n % candidate == 0:
                n //= candidate
                factors.append(candidate)
                if n == 1:
                    return factors
                if is_prime(n):
                    factors.append(n)
                    return factors
        candidate += 2
    if n != 1:
        factors.append(n)
    return factors

def send_program(n):
    digit_len = len(str(n))

    # 数値の桁数に応じた素数リストのフィルタリング
    if digit_len in [1, 2, 3, 4]:
        return prime_factors_small(n)
    elif digit_len in [5]:
        filtered_primes = prime_list[:25]
    elif digit_len in [6, 7, 8, 9]:
        filtered_primes = prime_list[:125]
    elif digit_len in [10, 11]:
        filtered_primes = prime_list[:1229]
    elif digit_len == 12:
        filtered_primes = prime_list[:9592]
    elif digit_len == 13:
        filtered_primes = prime_list[:78498]
    elif digit_len in [14, 15]:
        filtered_primes = prime_list[:664579]
    elif digit_len in [16, 17]:
        filtered_primes = prime_list[:5761455]
    else:
        filtered_primes = prime_list
    max_prime = filtered_primes[-1]
    return prime_factors(n, filtered_primes, max_prime)

def decompress_and_decode_gzip_with_timing(input_file):
    with gzip.open(input_file, 'rb') as f_in:
        decoded_data = f_in.read().decode('utf-8').split(",")
    decoded_data = np.array(decoded_data).astype(int)
    decoded_data = np.cumsum(decoded_data).tolist()
    return decoded_data

# 素数リストファイルのパス
prime_file = "sosuu.gz"
prime_list = decompress_and_decode_gzip_with_timing(prime_file)

# 数値のリスト
numbers = []

# 結果を格納するリスト
results = []
execution_times = []

# リスト内の各数について素因数分解を行う（複数回実行）
for num in numbers:
  factors = send_program(num)
  results.append(factors)
   
# 結果をファイルに保存
with open("results.txt", "a") as f:
    for i, num in enumerate(numbers):
        f.write(f"{num} の素因数: {results[i]}\n")

