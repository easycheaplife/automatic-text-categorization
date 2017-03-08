# encoding=utf-8
from __future__ import division  
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
corpus_file_name = './corpus.dat'

def transfer_text(path):
	files = []
	for path_, subdirs_, files_ in os.walk(path):
		for file in files_:
			if 'txt' in file:
				files.append(path_ + "/" + file)
	
	text_file_handle = open(corpus_file_name,'w')
	for input_name in files:
		lines = open(input_name,"r")
		for line in lines:
			if 0 != len(line.strip()):
				try:
					text_buf = filter_text(line.decode('cp936'),input_name)
					if len(text_buf) > 0:
						text_file_handle.write(" ".join(text_buf))
						text_file_handle.write("\n");
				except Exception as err:
					continue
		lines.close()
	text_file_handle.close()

def filter_text(buf,file_name):
	# get rid of html escape character
	buf = html_parser.unescape(buf)
	buf = buf.strip()
	buf = jieba.analyse.extract_tags(buf)
	buf = " ".join(buf)
	words = pseg.cut(buf)
	part_of_speech = ['x','d','b','m','u','t','uj','ul','c','p']
	part_of_speech = ['n','v','vn']
	texts = []
	for word, flag in words:
		if flag not in part_of_speech:
			continue	
		texts.append(word)
	return texts


from gensim import corpora,models,similarities
from pprint import pprint
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class my_corpus(object):
	def __init__(self,file_name):
		self.file_name = file_name
	def __iter__(self):
		for line in open(self.file_name):
			yield line.split()

def query_sims(corpus_file_name = 'test/gensim_tutorial/mycorpus.txt',query = "System and human",top_N = 20):
	texts = []
	corpus_data = my_corpus(corpus_file_name)
	for vec in corpus_data:
		texts.append(vec)
	'''
	texts's format  
	[['human', 'interface', 'computer'],['survey', 'user', 'computer', 'system', 'response', 'time']]
	'''
	dictionary = corpora.Dictionary(texts)
	#pprint (dictionary.token2id)

	corpus = [dictionary.doc2bow(text) for text in texts]
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]
	'''
	for doc in corpus_tfidf:
		print doc
	'''
	topic_num = top_N
	lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=topic_num)
	lsi.print_topics(topic_num)

	corpus_lsi = lsi[corpus_tfidf]
	'''
	for doc in corpus_lsi:
		print doc
	'''
	index = similarities.MatrixSimilarity(lsi[corpus])
	query_bow = dictionary.doc2bow(query.lower().split())
	query_lsi = lsi[query_bow]
	sims = index[query_lsi]
	sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sort_sims[0:10]


print query_sims()

#transfer_text("./SogouC.reduced/Reduced")
#print query_sims(corpus_file_name,"战法 演习 红军 对抗 出难题 心理战 对抗性 低能 打磨 必胜 透 演练 弱者 敌情",20)
