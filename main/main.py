import multiprocessing
import time
import signal

from modules.configs.Configs import(
    CPU_PROCESSES as cpu_prcs,
    CPU_WORK as cpu_wrk,
    CPU_SLEEP as cpu_slp,
)

from modules.GPU import(
    heat_my_gpu
)

def heat_my_cpu():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    
    while True:
        start = time.perf_counter()
        x = 0
    
        while time.perf_counter() - start < cpu_wrk:   # im gay
            x = (x * 3 + 1) % 1000000007

        time.sleep(cpu_slp)
        
if __name__ == "__main__":
    print(cpu_prcs, cpu_wrk, cpu_slp)
    
    processes = []
    
    GPU_PROCESS = multiprocessing.Process(target = heat_my_gpu)
    GPU_PROCESS.start()
    processes.append(GPU_PROCESS)
    
    for _ in range(cpu_prcs):
        p = multiprocessing.Process(target = heat_my_cpu)
        p.start()
        processes.append(p)
        
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping ...")
        
        for p in processes:
            p.terminate()
            
        for p in processes:
            p.join()
            
        print("Stopped!")
