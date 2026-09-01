import torch
import time

from modules.configs.Configs import(
    GPU_WORK as gpu_wrk,
    GPU_SLEEP as gpu_slp
)

def heat_my_gpu():
    device = torch.device("cuda")
    
    a = torch.randn((4096, 4096), device = device)
    b = torch.randn((4096, 4096), device = device)
                
                
    while True:
        start = time.perf_counter()
    
        while time.perf_counter() - start < gpu_wrk:
            torch.matmul(a, b)
            
        torch.cuda.synchronize()
        time.sleep(gpu_slp)