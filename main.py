import threading
import time
import random

class SharedResource:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        with self.lock:
            self.value += 1

    def get_value(self):
        with self.lock:
            return self.value

class Worker(threading.Thread):
    def __init__(self, shared_resource, name):
        threading.Thread.__init__(self)
        self.shared_resource = shared_resource
        self.name = name

    def run(self):
        for _ in range(10000):
            self.shared_resource.increment()
            time.sleep(random.uniform(0.001, 0.01))

def main():
    shared_resource = SharedResource()
    workers = [
        Worker(shared_resource, "Worker1"),
        Worker(shared_resource, "Worker2"),
        Worker(shared_resource, "Worker3"),
    ]

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

    print(f"Final value: {shared_resource.get_value()}")

if __name__ == "__main__":
    main()
```

Kodda `SharedResource` klassi mavjud bo'lib, u bir xususiyatga (value) va ikkita metodga ega: `increment` va `get_value`. `increment` metodida xususiyatni o'zgartirish uchun `lock` ni qo'llaniladi, bu esa bir vaqtda faqat bir thread xususiyatni o'zgartirishga imkon beradi. `get_value` metodida ham `lock` ni qo'llaniladi, lekin faqat o'qish uchun, chunki xususiyatni o'zgartirish uchun `lock` ni qo'llash zarur emas.

`Worker` klassi threadlarni simulyatsiya qilish uchun ishlatiladi. Har bir worker 10 000 marta `increment` metodini chaqiradi va keyin 0.001 dan 0.01 gacha vaqt o'tkazadi.

`main` funktsiyada uchta worker yaratiladi, ular boshlanadi va keyin bekor qilinadi. Keyin final xususiyat qiymati konsolga chiqariladi.
