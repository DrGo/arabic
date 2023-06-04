import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

doc_a = "ذهب محمد الى المدرسه على دراجته. هذا اول يوم له في المدرسة"
# doc_a = doc_a.decode('utf-8')
sw = stopwords.words('arabic')
tokens = nltk.word_tokenize(doc_a)
stopped_tokens = [i for i in tokens if not i in sw]
for item in stopped_tokens:
    print(item) 
f = open("tokens.txt","w")
f.write("\n".join(stopped_tokens))
