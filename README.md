# automatic-text-categorization
Based on tf/idf, cosine theorem, an automatic text classifier was designed, and the system test and result analysis were made.
### step
	1 participle
		parse text and get rid of non-notional/stopwords, then segmentation using jieba chinese participle(dat files);
	1 bag of word
		giving a nummber for every word, and statistics times for every word(voc files); 
    2 tf/idf
		compute tf/idf for every notional word which vecotr generated(dat files);
	3 feature vector	
		statistics feature for every categorization,and give top 10 word as sample word(sample.dat),
		statistics feature for all categorization,and give top 5000 word as sample word(sample.full),
		generate feature vector for every article(vec files);	
	4 compute similarity
		using cosine theorem compute similarity between two article(final files).
	

