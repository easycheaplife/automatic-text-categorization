import os
import sys
import chardet
import jieba
import jieba.posseg as pseg
import jieba.analyse
import HTMLParser

reload(sys)   
sys.setdefaultencoding('utf-8')
html_parser = HTMLParser.HTMLParser()
jieba.analyse.set_stop_words("./stop_words.txt")

def transfer_text(path,sample_prefix):
	files = []
	for path_, subdirs_, files_ in os.walk(path):
		for file in files_:
			if 'txt' in file:
				files.append(path_ + "/" + file)
	all_words = {}
	all_words.setdefault('test',1)
	for input_name in files:
		lines = open(input_name,"r")
		for line in lines:
			if 0 != len(line.strip()):
				try:
					filter_text(line.decode('cp936'),all_words)
				except Exception as err:
					continue
		lines.close()
	all_words = sorted(all_words.iteritems(), key = lambda test:test[1], reverse = True)
	sample_stat_handle = open(sample_prefix + '.stat','w')
	sample_dat_handle = open(sample_prefix + '.dat','w')
	separator = "\t"
	length = len(all_words)
	index = 0
	for word in all_words:
		if index <= 5000:
			sample_dat_handle.write(
					word[0] + " "
					)
			index += 1
		sample_stat_handle.write(
			word[0] + separator +
			str(word[1]) + separator + 
			str(length) + separator + 
			"\n"	
				)
	sample_stat_handle.close()
	sample_dat_handle.close()

def filter_text(buf,all_words):
	# get rid of html escape character
	buf = html_parser.unescape(buf)
	buf = buf.strip()
	buf = jieba.analyse.extract_tags(buf)
	buf = " ".join(buf)
	words = pseg.cut(buf)
	part_of_speech = ['x','d','b','m','u','t','uj','ul','c','p']
	part_of_speech = ['n','v','vn']
	for word, flag in words:
		if flag not in part_of_speech:
			continue	
		all_words.setdefault(word,0)
		all_words[word] += 1	

transfer_text("./SogouC.reduced/Reduced/C000008",'./text/C000008')
transfer_text("./SogouC.reduced/Reduced/C000010",'./text/C000010')
transfer_text("./SogouC.reduced/Reduced/C000013",'./text/C000013')
transfer_text("./SogouC.reduced/Reduced/C000014",'./text/C000014')
transfer_text("./SogouC.reduced/Reduced/C000016",'./text/C000016')
transfer_text("./SogouC.reduced/Reduced/C000020",'./text/C000020')
transfer_text("./SogouC.reduced/Reduced/C000022",'./text/C000022')
transfer_text("./SogouC.reduced/Reduced/C000023",'./text/C000023')
transfer_text("./SogouC.reduced/Reduced/C000024",'./text/C000024')
