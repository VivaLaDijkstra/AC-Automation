#! /usr/bin/env python

from collections import deque

class queue(deque):

	def push(self, item):
		self.append(item)

	def pop(self):
		return self.popleft()


def test():
	q = queue()
	for i in range(10):
		q.push(i)

	while q:
		print q.pop()
	for i in range(10):
		q[i] = i * i 



if __name__ == '__main__':
	test()