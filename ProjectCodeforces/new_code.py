from sys import argv
import subprocess


script, pyfile = argv

py = open(pyfile)
prob = py.readline()
prob = list(prob)
prob = ''.join(prob[1:len(prob) - 1])

subprocess.call('python master.py {}'.format(prob), shell = True)

testcases = open('codeforces_testcases.txt', 'r+')

list_testcase = testcases.read()
list_testcase = list_testcase.split('\n')
list_testcase = list_testcase[:list_testcase.index('')]
list_testcase.append('Input')
testcases.close()

#print list_testcase

flag = 0

temp = []
for i in xrange(list_testcase.count('Output')):
	infile = open('text_in.txt', 'w')
	outfile = open('text_out.txt', 'w')

	temp  = list_testcase[list_testcase.index('Input')+1 : list_testcase.index('Output')]
	infile.write('\n'.join(temp))
	infile.write('\n')
	list_testcase = list_testcase[list_testcase.index('Output'):]
	
	tempo = list_testcase[1: list_testcase.index('Input')]
	outfile.write('\n'.join(tempo))
	outfile.write('\n')
	list_testcase = list_testcase[list_testcase.index('Input'):]

	infile.close()
	outfile.close()
	
	subprocess.call('python {} <text_in.txt >outfile.txt'.format(pyfile), shell = True)

	outputfile = open('outfile.txt')
	outfile = open('text_out.txt')

	con1 = outfile.read()
	con2 = outputfile.read()

	if con1 == con2:
		print 'Testcase {} passed sucessfully!'.format(i+1)
	else:
		print 'Testcase {} failed!'.format(i+1)

	print 'Expected Output: \n{}'.format(con1)
	print 'Your Output: \n{}'.format(con2)