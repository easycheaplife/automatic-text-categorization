from __future__ import division  
import os
import sys
import chardet
import math
import copy
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
	# keys is word, value is word times
	all_words = {}
	all_words.setdefault('test',1)
	word_pages = {}
	for input_name in files:
		lines = open(input_name,"r")
		for line in lines:
			if 0 != len(line.strip()):
				try:
					filter_text(line.decode('cp936'),all_words,word_pages,input_name)
				except Exception as err:
					continue
		lines.close()
	all_words = sorted(all_words.iteritems(), key = lambda test:test[1], reverse = True)
	sample_stat_handle = open(sample_prefix + '.stat','w')
	sample_dat_handle = open(sample_prefix + '.dat','w')
	separator = "\t"
	length = len(all_words)
	index = 0
	vocabulary_list = []
	for word in all_words:
		tf_value = round(word[1]/length,4)
		idf_value,count_word_in_page = compute_idf(word_pages,len(files),word[0])
		tf_idf_value = round(tf_value * idf_value,4)
		index += 1
		# sort first in cache
		tmp = [word[0],index,count_word_in_page,len(files),word[1],length,tf_value,idf_value,tf_idf_value]
		vocabulary_list.append(tmp)

	vocabulary_list = sorted(vocabulary_list,key = lambda x:x[8],reverse=True)
	vocabulary_list_copy = copy.copy(vocabulary_list)
	for voc in vocabulary_list: 
		sample_stat_handle.write(
			voc[0] + separator +
			str(voc[1]) + separator +
			str(voc[2]) + separator + 
			str(voc[3]) + separator + 
			str(voc[4]) + separator + 
			str(voc[5]) + separator + 
			str(voc[6]) + separator + 
			str(voc[7]) + separator + 
			str(voc[8]) + separator + 
			"\n"	
				)
	# get to N sample word which sort by tf/idf value
	sample_word_list = []
	for data in vocabulary_list_copy[0:1000]:
		sample_word_list.append(data[0])
	sample_dat_handle.write(" ".join(sample_word_list))
	sample_stat_handle.close()
	sample_dat_handle.close()

def filter_text(buf,all_words,word_pages,file_name):
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
		
		# map word to files
		if word_pages.has_key(word):
			tmp = word_pages.get(word)
			tmp[file_name] = file_name  
		else:
			word_pages.setdefault(word,{})


def count_word_in_pages(word_pages,word):
	count = 1
	if word_pages.has_key(word):
		tmp = word_pages[word]
		if tmp:
			count = len(tmp)
	return count


def compute_idf(word_pages,total_page,word):
	count_page = count_word_in_pages(word_pages,word)	
	return round(math.log(total_page/count_page,2),4),count_page 


transfer_text("./SogouC.reduced/Reduced",'./text/statistics')
transfer_text("./SogouC.reduced/Reduced/C000008",'./text/C000008')
transfer_text("./SogouC.reduced/Reduced/C000010",'./text/C000010')
transfer_text("./SogouC.reduced/Reduced/C000013",'./text/C000013')
transfer_text("./SogouC.reduced/Reduced/C000014",'./text/C000014')
transfer_text("./SogouC.reduced/Reduced/C000016",'./text/C000016')
transfer_text("./SogouC.reduced/Reduced/C000020",'./text/C000020')
transfer_text("./SogouC.reduced/Reduced/C000022",'./text/C000022')
transfer_text("./SogouC.reduced/Reduced/C000023",'./text/C000023')
transfer_text("./SogouC.reduced/Reduced/C000024",'./text/C000024')
