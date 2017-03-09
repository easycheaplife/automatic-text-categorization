from gensim import corpora
from pprint import pprint  # pretty-printer
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO) 
documents = ["Human Human machine interface for lab abc computer applications",
		"A survey of user opinion of computer system response time",
		"The EPS user interface management system",
		"System and human system engineering testing of EPS",
		"Relation of user perceived response time to error measurement",
		"The generation of random binary unordered trees",
		"The intersection graph of paths in trees",
		"Graph minors IV Widths of trees and well quasi ordering",
		"Graph minors A survey"]
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
		for document in documents]
pprint(texts)

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
	for token in text:
		frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
		for text in texts]

pprint(texts)


dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict')  # store the dictionary, for future reference
pprint(dictionary.__dict__)

print(dictionary.token2id)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)  # the word "interaction" does not appear in the dictionary and is ignored

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)  # store to disk, for later user
print(corpus)


class MyCorpus(object):
	def __iter__(self):
		for line in open('mycorpus.txt'):
			# assume there's one document per line, tokens separated by whitespace
			yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus()  # doesn't load the corpus into memory!
print(corpus_memory_friendly)

for vector in corpus_memory_friendly:  # load one vector into memory at a time
	print(vector)

from six import iteritems
# collect statistics about all tokens
dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
		if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids)  # remove stop words and words that appear only once
dictionary.compactify()  # remove gaps in id sequence after words that were removed
print(dictionary.token2id)

# create a toy corpus of 2 documents, as a plain Python list_test
corpus = [[(1, 0.5)], []]  # make one document empty, for the heck of it
corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)

corpora.SvmLightCorpus.serialize('/tmp/corpus.svmlight', corpus)
corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)
corpora.LowCorpus.serialize('/tmp/corpus.low', corpus)


corpus = corpora.MmCorpus('/tmp/corpus.mm')
print(corpus)

# one way of printing a corpus: load it entirely into memory
print(list(corpus))  # calling list() will convert any sequence to a plain Python list

# another way of doing it: print one document at a time, making use of the streaming interfacec
for doc in corpus:
	print(doc)

corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)

