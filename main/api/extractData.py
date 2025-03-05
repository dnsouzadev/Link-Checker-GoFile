from proccessUrl import get_request
from generate import generate_random_string
import concurrent.futures
import threading

total_tested = 0
live_count = 0
dead_count = 0
lock = threading.Lock()

def update_status():
    with lock:
        print(f"\rTestados: {total_tested} | Live: {live_count} | Dead: {dead_count}", end="", flush=True)

def extract_data(randomData, authorization, live_file, dead_file):
    global total_tested, live_count, dead_count
    url = f'https://api.gofile.io/contents/{randomData}?wt=4fd6sg89d7s6&contentFilter=&page=1&pageSize=1000&sortField=name&sortDirection=1'
    response = get_request(url, authorization=authorization)

    with lock:
        total_tested += 1

    if response.status_code == 200:
        json = response.json()
        status = json['status']

        if status == "ok":
            result = f"[+] {randomData} -> Link Encontrado | Data -> canAccess: {json['data']['canAccess']} | type: {json['data']['type']} | name: {json['data']['name']} | totalDownloadCount: {json['data']['totalDownloadCount']}\n"
            with lock:
                live_count += 1
                live_file.write(result)
                live_file.flush()
        else:
            result = f"[x] {randomData} -> Error: {status}\n"
            with lock:
                dead_count += 1
                dead_file.write(result)
                dead_file.flush()
    elif response.status_code == 401:
        result = f"[x] {randomData} -> Problema com a autorização, verifique o token. {response.status_code}\n"
        with lock:
            dead_count += 1
            dead_file.write(result)
            dead_file.flush()
    else:
        result = f"[x] {randomData} -> Problema com a requisição. {response.status_code}\n"
        with lock:
            dead_count += 1
            dead_file.write(result)
            dead_file.flush()

    update_status()

def main():
    authorization = "mf1lRWSoPlc7LU89VWx1mq5J4ZmOuLuu"

    with open("live.txt", "w") as live_file, open("dead.txt", "w") as dead_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            while True:
                random_data = generate_random_string()
                executor.submit(extract_data, random_data, authorization, live_file, dead_file)

if __name__ == "__main__":
    main()
