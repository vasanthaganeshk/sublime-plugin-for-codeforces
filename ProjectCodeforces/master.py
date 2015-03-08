from urllib2 import urlopen
from MyParser import MyHTMLParser
from sys import argv

script, tag = argv
tag = list(tag)
prob_difficulty = tag.pop()
tag = ''.join(tag)

print 'Requesting codeforces...'
target = urlopen('http://www.codeforces.com/problemset/problem/{}/{}'.format(tag, prob_difficulty))

print 'reading page...'
unparsed_text = target.read()

parser = MyHTMLParser()
parser.feed(unparsed_text)
print 'Parse sucessful'