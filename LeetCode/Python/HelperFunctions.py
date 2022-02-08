import os
import psutil


def get_memory_used():
    process = psutil.Process(os.getpid())
    print("MAX MEMORY: " + str(process.memory_info().rss / 1000000) + "MB")  # in mb
