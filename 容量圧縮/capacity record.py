import os

#1と2のファイルから素数を読み込む関数
def read_primes(file_path):
   with open(file_path, 'r') as file:
        primes = file.read().strip().split(',')
   return [int(prime) for prime in primes]

#素数を10万個ずつ区切ってファイルに保存する関数
def save_primes(primes, batch_size, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    total_primes = len(primes)
    batch_files = []
    for i in range(1000000, total_primes, batch_size):
        batch = primes[:i]
        batch_file = os.path.join(output_dir, f'primes_batch_{i//batch_size + 1}.txt')
        with open(batch_file, 'w') as file:
            file.write(','.join(map(str, batch)))
        batch_files.append(batch_file)

    return batch_files

#ファイルサイズを取得する関数
def get_file_size(file_path):
    return os.path.getsize(file_path)

#ファイルの最後の数字を取得する関数
def get_last_number(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().strip().split(',')
    return int(numbers[-1])

#10万個ずつ素数が書かれたファイルの容量と最後の数字を別のファイルに保存する関数
def write_summary_file(batch_files, summary_file):
    with open(summary_file, 'w') as file:
        for batch_file in batch_files:
            size = get_file_size(batch_file)
            last_number = get_last_number(batch_file)
            file.write(f'{batch_file}: {size} bytes, last number: {last_number}\n')

def main():
    input_file = 'sosuu.txt'  #１と２のファイル名
    output_dir = 'primes_batches'   #10万個ずつ素数を区切ったファイルを保存するディレクトリ
    summary_file = 'summary.txt'    #容量を記録するファイル名
    batch_size = 1000000             #10万個ずつ区切る

    #1と2のファイルから素数を読み込む
    primes = read_primes(input_file)

    #ファイルに素数を10万個ずつ保存する
    batch_files = save_primes(primes, batch_size, output_dir)

    #保存した容量と最後の数字を記録する
    write_summary_file(batch_files, summary_file)

if __name__ == "__main__":
    main()
