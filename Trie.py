#! /usr/bin/env python

# Writer: wuhanghao
# Date: 2016.2.1

from queue import queue

class TrieNode(object):

	def __init__(self, d=0, iw=False):
		self.depth = d
		self.isWord = iw
		self.child = {}
		self.fail = None

class Trie(object):

	def __init__(self, dir=r'.\dictionary.txt'):
		self.root = TrieNode()
		self.num = 0

		with open(dir) as f:
			words = f.read().decode('gb2312').split()
		# for w in words:
		# 	print type(w), ' ', w

		for word in iter(words):
			self._insert(word)

		self._buildFailPoint()

	def _insert(self, word):
		"""insert a word into trie.Each word is a set of unicode character."""
		# assert word is not ''
		p = self.root

		for d, c in enumerate(word, start=1):
			if c not in p.child:
				p.child[c] = TrieNode(d)
			p = p.child[c]

		assert p is not self.root
		p.isWord = True
		assert self.root.isWord is False

	def _buildFailPoint(self):
		"""Based on bfs strategy."""
		q = queue()
		for s in self.root.child.itervalues():
			s.fail = self.root
			q.push(s)

		while q:
			p = q.pop()
			for c, s in p.child.iteritems():
				s.fail = self.transit(c, p.fail)
				q.push(s)

	def _bfs(self, oper): 
		q = queue()
		q.push(self.root)
		oper(self.root)
		while q:
			p = q.pop()
			for v in p.child.itervalues():
				oper(p)
				q.push(v)

	def transit(self, c, p):
		"""transit function of automation that c is the edge and p points to 
		current status node"""
		while p and (c not in p.child): 
			p = p.fail 
		# if no node matchs
		if p is None:
			return self.root
		else:
			return p.child[c]	

	def match(self, text):
		"""match patterns in unicode text.
		return True and the first position where a pattern matchs.
		if no pattern matchs, return False."""

		p = root = self.root

		for i, c in enumerate(text, start=1):
			# if character c doesn't match, track back to the node that matchs
			p = self.transit(c, p)
			if p.isWord:
				return True, i, p.depth

		return False, 0, 0

	def _DFS(self, p, ch):
		if p is None:
			return 

		print ch, ' ', p.depth, ' ', 
		for c in p.child:
			self._DFS(p.child[c], c)

	def _dfs(self):
		self._DFS(self.root, '')

	def visit(self, node):
		if node.child:
			print u', '.join([s+str(node.child[s].depth) for s in node.child.keys()])
		else:
			print u'#'

	def show(self):
		# self._bfs(self.visit)
		self._dfs()


if __name__ == '__main__':
	trie = Trie(r'.\dictionary.txt')
	trie.show()