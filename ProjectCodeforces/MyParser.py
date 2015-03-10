from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	flag = 0
	infile = open('codeforces_testcases.txt', 'w')

	def handle_starttag(self, tag, attrs):
		if tag == 'script' and self.flag == 1:
		    #exit()
		    self.flag = 0

	def handle_data(self, data):        
		data = data.strip()
		h_s_data = data

		if data == 'Note' and self.flag == 1:
		    #exit()
		    self.flag = 0

		if data == 'Sample test(s)':
			self.flag = 1

		elif self.flag == 1:
			#self.flag = 1
			self.infile.write(data)
			self.infile.write('\n')

