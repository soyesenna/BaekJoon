import sys
import itertools
import psutil
import os

def before_memory():
    # BEFORE code
    # general RAM usage
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

def after_memory():
    # AFTER  code
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    print("--"*30)

before_memory()
n = int(sys.stdin.readline())
li = tuple(map(int, sys.stdin.readline().split()))
if li[0] == 1:
    nums = [i for i in range(li[0] * len(li), n + 1)]
print(nums)
permutation = list(itertools.permutations(nums, n))
print(permutation)
idx = permutation.index(li)

after_memory()
if idx == 0:
    print(-1)
else:
    for num in permutation[idx - 1]:
        print(num, end=' ')