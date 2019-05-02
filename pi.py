from wordcloud import WordCloud, STOPWORDS 
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

with open ("Alice in Wonderland.txt") as f:
    text = f.read()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open ("Alice in Wonderland.txt") as f:
    text = f.read()
alice_mask = np.array(Image.open(path.join(d,'alice_mask.png')))
WordCloud = WordCloud(with=1920, height==1200)

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()

    
wordcloud = WordCloud(width=1920, height= 1200)
STOPWORDS.add('said')
STOPWORDS.add('illustration')
wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

