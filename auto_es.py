from pathlib import Path
import subprocess
import os
from concurrent.futures import ThreadPoolExecutor
import time

if not os.path.exists('input'):
    os.mkdir('input')
if not os.path.exists('output'):
    os.mkdir('output')

input_dir = '.\input'
output_dir = '.\output'

f_list = list(Path(input_dir).glob('**/*.pcap'))

def extract_secrets(file):
    cmd = f"extract_secrets -f \"{file}\""
    try:
        print(cmd)
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("cannot find 'extract_secrets' command")

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(extract_secrets(f)) for f in f_list]

if __name__ == '__main__':
    # 処理前の時刻
    t1 = time.time()    
    main()
    # 処理後の時刻
    t2 = time.time()
    
    # 経過時間を表示
    elapsed_time = t2-t1
    print(f"Elapsed time: {elapsed_time}")
