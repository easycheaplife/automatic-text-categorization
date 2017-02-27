#!/bin/bash
echo 'clear files'
rm -f text/*.final
rm -f text/*.vec
rm -f text/*.voc
rm -f text/*part
rm -f text/*.dat

echo 'copy sample file'
cp text/sample.simple text/sample.dat

echo 'participle.py'
python participle.py 
echo 'normalization.py' 
python normalization.py 
echo 'generate_feature_vector.py'
python generate_feature_vector.py 
echo 'cosine_categorize.py'
python cosine_categorize.py

echo 'success!'
