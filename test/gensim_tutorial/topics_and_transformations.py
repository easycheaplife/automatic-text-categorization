import os
from gensim import corpora, models, similarities
from pprint import pprint  # pretty-printer
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO) 

if (os.path.exists("/tmp/deerwester.dict")):
	dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
	corpus = corpora.MmCorpus('/tmp/deerwester.mm')
	print("Used files generated from first tutorial")
else:
	print("Please run first tutorial to generate data set")

pprint(corpus.__dict__)
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
pprint(tfidf.__dict__)

doc_bow = [(0, 1), (1, 1)]
print(tfidf[doc_bow]) # step 2 -- use the model to transform vectors

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	print doc

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) # initialize an LSI transformation
pprint(lsi.__dict__)
pprint(lsi.id2word.__dict__)

corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
pprint(corpus_lsi.__dict__)

lsi.print_topics(2)

for doc in corpus_lsi: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
	print doc

lsi.save('/tmp/model.lsi') # same for tfidf, lda, ...
lsi = models.LsiModel.load('/tmp/model.lsi')

model = models.TfidfModel(corpus, normalize=True)
print model.__dict__

model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=300)
print model.__dict__

model = models.RpModel(corpus_tfidf, num_topics=500)
print model.__dict__

model = models.LdaModel(corpus, id2word=dictionary, num_topics=100)
print model.__dict__

model = models.HdpModel(corpus, id2word=dictionary)
print model.__dict__


