from threading import Thread
from  queue import Queue


def producer(n):
	for i in range(2):
		print('producer{} release a task {}'.format(n, q.put(i)))


def comsumer(n):
	print('comsuer {} carry out a task {}'.format(n, q.get()))
	q.task_done()


if __name__ == "__main__":
	q = Queue()
	comsumer1 = Thread(target=comsumer, args=('comsumer1',))
	comsumer2 = Thread(target=comsumer, args=('comsumer2',))
	producer1 = Thread(target=producer, args=('producer1',))
	producer2 = Thread(target=producer, args=('producer2',))
	comsumer1.start()
	comsumer2.start()
	producer1.start()
	producer2.start()
