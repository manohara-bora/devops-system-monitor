
import psutil
import platform

def system_info():
    print("=== System Information ===")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print()

def cpu_usage():
    print("=== CPU Usage ===")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print()

def memory_usage():
    memory = psutil.virtual_memory()
    print("=== Memory Usage ===")
    print(f"Total: {memory.total / (1024**3):.2f} GB")
    print(f"Used: {memory.used / (1024**3):.2f} GB")
    print(f"Percentage: {memory.percent}%")
    print()

def disk_usage():
    disk = psutil.disk_usage('/')
    print("=== Disk Usage ===")
    print(f"Total: {disk.total / (1024**3):.2f} GB")
    print(f"Used: {disk.used / (1024**3):.2f} GB")
    print(f"Percentage: {disk.percent}%")
    print()

def running_processes():
    print("=== Running Processes ===")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            print(f"PID: {proc.info['pid']} | Name: {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

if __name__ == "__main__":
    system_info()
    cpu_usage()
    memory_usage()
    disk_usage()
    running_processes()