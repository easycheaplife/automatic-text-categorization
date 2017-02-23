# encoding=utf-8
import sys
import jieba
import jieba.posseg as pseg
import jieba.analyse

jieba.analyse.set_stop_words("./stop_words.txt")

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
for word in seg_list:
	print word

words = pseg.cut("我来到北京清华大学")
for word,flag in words:
	print('%s %s' % (word, flag))

seg_list = jieba.cut("我来到北京清华大学")
print("Default Mode: " + "/ ".join(seg_list))

print("Search Mode:")
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") 
print(", ".join(seg_list))

seg_list = jieba.cut("会议主要议程还包括“2005中国最具影响力药企发布”、“第三终端高峰论坛等”。", cut_all=False)
print("test symbol: " + "/ ".join(seg_list))

words = pseg.cut("会议主要议程还包括“2005中国最具影响力药企发布”、“第三终端高峰论坛等”。")
for word,flag in words:
	print('%s %s' % (word, flag))

words = jieba.cut("会议主要议程还包括“2005中国最具影响力药企发布”、“第三终端高峰论坛等”。")
for word in words:
	print word


tags = jieba.analyse.extract_tags("你是我的他,停止词,会议主要议程还包括“2005中国最具影响力药企发布”、“第三终端高峰论坛等", topK=10)
print(",".join(tags))
