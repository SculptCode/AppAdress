import psutil
import time
import requests

def list_network_connections(process_name):
    connections = psutil.net_connections()
    filtered_connections = {}
    
    for conn in connections:
        if conn.status == 'ESTABLISHED':
            pid = conn.pid
            name = psutil.Process(pid).name()
            
            if process_name in name:
                if name not in filtered_connections:
                    filtered_connections[name] = []
                filtered_connections[name].append((pid, conn.laddr, conn.raddr))
    
    return filtered_connections

def display_connections(connections):
    for name, conn_list in connections.items():
        print(f"Bağlantılar: {name}")
        for conn in conn_list:
            print(f"PID: {conn[0]}, LADDR: {conn[1]}, RADDR: {conn[2]}")
        print()

def main():
    process_name = input("Enter the name of the programme you want to watch: ")
    
    while True:
        connections = list_network_connections(process_name)
        
        if len(connections) == 0:
            print("No active links to the specified programme were found.")
        else:
            display_connections(connections)
        
        time.sleep(5)

def get_active_processes():
    active_processes = set()
    for conn in psutil.net_connections(kind='tcp'):
        if conn.status == 'ESTABLISHED':
            active_processes.add(conn.pid)
    return active_processes

def print_active_processes():
    active_processes = get_active_processes()
    print("Active Programmes:")
    for pid in active_processes:
        try:
            process = psutil.Process(pid)
            print("(+) "+process.name())
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    print_active_processes()
    main()

##https://github.com/SculptCode