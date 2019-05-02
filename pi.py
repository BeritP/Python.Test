from os import path 

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS
STOPWORDS.add('said')

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'alice in Wonderland.txt')).read()



alice_mask = np.array(Image.open(path.join(d,'alice_mask.png')))

STOPWORDS = set(STOPWORDS)
STOPWORDS.add("said")

wordcloud = WordCloud(background_color="white", max_words=200, mask=alice_mask, contour_width=3, contour_color='steelblue')
wordcloud.generate(text)
wordcloud.to_file(path.join("alice.png"))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.axis("off")
plt.show()



