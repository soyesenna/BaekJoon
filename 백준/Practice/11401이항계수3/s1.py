import sys
import psutil
import os
from memory_profiler import profile

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

sys.setrecursionlimit(5000000)

@profile
def factorial(n, k, cnt):
    if cnt == k:
        return 1
    return n * factorial(n - 1, k, cnt + 1)

before_memory()
n, k = map(int, sys.stdin.readline().split())
if k == 0:
    print(1)
    sys.exit()

k = min(k, n - k)

c = factorial(n, k, 0) / k

after_memory()
print(int(c % 1000000007))