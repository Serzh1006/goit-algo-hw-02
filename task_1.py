from queue import Queue
import time
import random


def generate_request(request_queue, request_id):
    new_application = f"Заявка № {request_id}"
    request_queue.put(new_application)
    print(f"\nСгенеровано нову заявку: {new_application}")

def process_request(request_queue,request_id):
    if not request_queue.empty():
        data = request_queue.get()
        print(f"\nЗаявку оброблено -> {data}")
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
                process_request(request_queue,request_id)
    
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")



if __name__ == "__main__":
    main()