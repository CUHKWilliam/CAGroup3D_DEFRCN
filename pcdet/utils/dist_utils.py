import torch.distributed as dist
import torch

def is_distributed():
    return dist.is_available() and dist.is_initialized()

def get_rank():
    if not dist.is_available():
        return 0
    if not dist.is_initialized():
        return 0
    return dist.get_rank()

def is_main_process():
    return get_rank() == 0

def update_cnt():
    global cnt
    if is_main_process():
        cnt += 1
cnt = 0
def is_debug():
    # return False
    return is_main_process() and cnt % 2000 == 0

def is_debug2():
    # return False
    return is_main_process() and cnt % 2000 == 0

