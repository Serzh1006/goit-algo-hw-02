from queue import Queue
import time
import random


def generate_request(request_queue, request_id):
    new_application = f"Нова заявка № {request_id}"
    request_queue.put(new_application)
    print(f"\nСгенеровано нову заяку: {new_application}")

def process_request(request_queue):
    if not request_queue.empty():
        data = request_queue.get()
        print(f"\nЗаявку оброблено {data}")
        time.sleep(random.uniform(1,2))
    else:
        print("\nЧерга пуста. Немає заявок для обробки.")



def main():
    request_queue = Queue()
    request_id = 0

    try:
        while True:
            if random.choice([True,False]):
                request_id+=1
                generate_request(request_queue, request_id)
            
            if random.choice([True,False]):
                process_request(request_queue)
    
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")



if __name__ == "__main__":
    main()