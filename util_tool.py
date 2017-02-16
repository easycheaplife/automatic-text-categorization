import os

def search_directory(path,word = ''):
	files = []
	for file_name in os.listdir(path):
		fp = os.path.join(path,file_name)
		if os.path.isfile(fp) and word in file_name:
			files.append(fp)
		elif os.path.isdir(fp):
			search_directory(fp,word)
	return files

