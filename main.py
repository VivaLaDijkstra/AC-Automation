#! /usr/bin/env python

# Writer: wuhanghao
# Date: 2016.2.1

from Trie import Trie

with open(r'.\text.txt') as f:
	txt = f.read().decode('gb2312')

pattern = Trie()
rst = isMatched, lastPos, leng = pattern.match(txt)
print rst
if isMatched:
	print 'pattern "%s" found' % txt[lastPos-leng:lastPos]
else:
	print 'pattern notfound'