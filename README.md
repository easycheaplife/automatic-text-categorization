# automatic-text-categorization
Based on tf/idf, cosine theorem, an automatic text classifier was designed, and the system test and result analysis were made.
### step
	1 participle
		parse text and get rid of non-notional, then segmentation using jieba chinese participle;
	1 vector of word
		giving a nummber for every word and generate vector of notional word;
    2 tf/idf
		compute tf/idf for every notional word which vecotr generated;
	3 feature vector	
		generate feature vector for every article;	
	4 compute similarity
		using cosine theorem compute similarity between two article.

### to do
	1 statistics tf for all sougou document and get top N;
	2 statistics feature for every categorization;
