# encoding=utf-8
obj = {}
obj.setdefault('a')
obj['a'] = 10
obj.setdefault('a')
obj['b'] = 30
obj.setdefault('a')
obj['c'] = 1

print obj
print obj.keys()

# every thing is object, pass value is reference or adress
def param_test(obj):
	obj['d'] = 34

param_test(obj)

obj['本报记者'] = 2
print obj
print sorted(obj.iteritems(), key = lambda a:a[1])

