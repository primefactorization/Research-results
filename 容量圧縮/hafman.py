import decimal
import os
import time
import sympy

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
angou = delta_encoding(read_prime(file_path))
prime_strs = str(angou)[1:-1]


import heapq
import json
import bitarray

# ノードを作るためのクラス
class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# データの頻度を計算する関数
def calculate_frequencies(data):
    frequencies = {}
    for symbol in data:
        if symbol in frequencies:
            frequencies[symbol] += 1
        else:
            frequencies[symbol] = 1
    return frequencies

# ハフマン木を作成する関数
def build_huffman_tree(frequencies):
    heap = [Node(symbol, freq) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# コードを生成する関数
def generate_codes(node, prefix="", codebook={}):
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        if node.left is not None:
            generate_codes(node.left, prefix + "0", codebook)
        if node.right is not None:
            generate_codes(node.right, prefix + "1", codebook)
    return codebook

# データを符号化する関数
def encode_data(data, codebook):
    return ''.join(codebook[symbol] for symbol in data)

# ハフマン木をJSON形式に変換する関数
def huffman_tree_to_dict(node):
    if node.symbol is not None:
        return node.symbol
    return {
        "left": huffman_tree_to_dict(node.left),
        "right": huffman_tree_to_dict(node.right)
    }

# データをバイナリ形式で保存する関数
def save_binary(filepath, bitstring):
    bits = bitarray.bitarray(bitstring)
    with open(filepath, 'wb') as file:
        bits.tofile(file)

# データをファイルに保存する関数
def save_to_file(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file)

# 符号化処理を実行する関数
def huffman_encoding(data):
    frequencies = calculate_frequencies(data)
    huffman_tree = build_huffman_tree(frequencies)
    codebook = generate_codes(huffman_tree)
    encoded_data = encode_data(data, codebook)
    return codebook, encoded_data, huffman_tree


codebook, encoded_data, huffman_tree = huffman_encoding(prime_strs)
#符号化データをバイナリ形式で保存
save_binary('encoded_data.bin', encoded_data)
# ハフマン木をJSON形式に変換して保存
huffman_tree_dict = huffman_tree_to_dict(huffman_tree)
save_to_file('huffman_tree.json', huffman_tree_dict)


# データをバイナリ形式で読み込む関数
def load_binary(filepath):
    with open(filepath, 'rb') as file:
        bits = bitarray.bitarray()
        bits.fromfile(file)
    return bits.to01()

# データをファイルから読み込む関数
def load_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

# ハフマン木を復元する関数
def dict_to_huffman_tree(d):
    if isinstance(d, str):
        return Node(d, 0)
    node = Node(None, 0)
    if 'left' in d and 'right' in d:
        node.left = dict_to_huffman_tree(d['left'])
        node.right = dict_to_huffman_tree(d['right'])
    return node

# 複合化するための関数
def decode_data(encoded_data, huffman_tree):
    decoded_data = []
    node = huffman_tree
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.symbol is not None:
            decoded_data.append(node.symbol)
            node = huffman_tree
    return ''.join(decoded_data)  # 文字列として返す

# 複合化処理を実行する関数
def huffman_decoding(encoded_data, huffman_tree):
    
    return decode_data(encoded_data, huffman_tree)



def delta_decoding(deltas_num):
    if not deltas_num:
        return []
    prime_befor = int(deltas_num[0])
    primes = [prime_befor]
    prime_list = deltas_num.split(",")
    for i in prime_list[1:]:
        prime_befor += int(i)
        primes.append(prime_befor)
    return primes



time_list = []
for _ in range(5):
  start_time = time.perf_counter()
  # バイナリ形式の符号化データを読み込む
  encoded_data = load_binary('encoded_data.bin')
  # JSON形式のハフマン木を読み込む
  huffman_tree_dict = load_from_file('huffman_tree.json')
  huffman_tree = dict_to_huffman_tree(huffman_tree_dict)
  # 複合化を実行
  decoded_data = huffman_decoding(encoded_data, huffman_tree)
  reconstruction_primers = delta_decoding(decoded_data)
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  time_list.append(elapsed_time)
b = 0
for a in time_list:
    b = b+ a
b = b / 5
print(f"Elapsed time: {b} seconds")

abc =decimal.Decimal(1024)

with open("results.txt.txt","a") as f:
    f.write(str(stop) + "この素数\n")
    f.write(f"{str(get_file_size('huffman_tree.json')/abc/abc + get_file_size('encoded_data.bin')/abc/abc)[:8]}\n")
    f.write(f"Elapsed time: {b} seconds\n")
