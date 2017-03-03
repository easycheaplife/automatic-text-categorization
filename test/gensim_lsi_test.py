from gensim import corpora,models,similarities
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO) 

documents = ["Shipment of gold damaged in a fire",
			"Delivery of silver arrived in a silver truck",
			"Shipment of gold arrived in a truck"]
texts = [[word for word in document.lower().split()] for document in documents]
print texts

dictionary = corpora.Dictionary(texts)
print dictionary
print dictionary.token2id

corpus = [dictionary.doc2bow(text) for text in texts]
print corpus

tfidf = models.TfidfModel(corpus)
print tfidf

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	print doc

print tfidf.dfs

print tfidf.idfs

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
lsi.print_topics(2)

corpus_lsi = lsi[corpus_tfidf]
for doc in corpus_lsi:
	print doc

lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=2)
lda.print_topics(2)

corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
	print doc

# query similar document
index = similarities.MatrixSimilarity(lsi[corpus])
query = "gold silver truck"
query_bow = dictionary.doc2bow(query.lower().split())
print query_bow

query_lsi = lsi[query_bow]
print query_lsi

sims = index[query_lsi]
print list(enumerate(sims))

sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sort_sims
