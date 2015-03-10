from urllib2 import urlopen
from MyParser import MyHTMLParser

def opener(tag):
	tag = list(tag)
	prob_difficulty = tag.pop()
	tag = ''.join(tag)

	print 'Requesting codeforces...'
	target = urlopen('http://www.codeforces.com/problemset/problem/{}/{}'.format(tag, prob_difficulty))

	print 'reading page...'
	unparsed_text = target.read()

	parser = MyHTMLParser()
	parser.feed(unparsed_text)

	# if parser.S_tag == 'script' and parser.flag == 1:
	# 	#parser.close()
	# 	#exit()
	# 	flag = 0

	# if parser.h_s_data == 'Note' and parser.flag == 1:
	# 	#parser.close
	# 	#exit()
	# 	flag = 0
	parser.infile.close()

	print 'Parse sucessful'
	return