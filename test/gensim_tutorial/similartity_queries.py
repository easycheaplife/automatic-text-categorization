import os
from gensim import corpora, models, similarities
from pprint import pprint  # pretty-printer
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO) 

if (os.path.exists("/tmp/deerwester.dict")):
	dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
	pprint(dictionary.__dict__)
	corpus = corpora.MmCorpus('/tmp/deerwester.mm')
	pprint(corpus.__dict__)
	print(corpus)
	print("Used files generated from first tutorial")
else:
	print("Please run first tutorial to generate data set")

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
pprint(lsi.__dict__)
pprint(lsi.id2word.__dict__)
pprint(lsi.projection.__dict__)

doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # convert the query to LSI space
print(vec_lsi)

index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
index.save('/tmp/deerwester.index')
index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')

pprint(lsi.__dict__)
sims = index[vec_lsi] # perform a similarity query against the corpus

print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples

sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sims


