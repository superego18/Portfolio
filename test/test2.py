from matplotlib.patches import FancyBboxPatch
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Generate word cloud
text = "some text data to generate a word cloud"
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

# create a rectangle with rounded corners
rect = FancyBboxPatch((0, 0), 800, 800, boxstyle="round, pad=0.1", ec="gray", lw=1, fc="lightgray")

# create a figure and add the rectangle and word cloud to it
fig, ax = plt.subplots(figsize=(8, 8))
ax.add_patch(rect)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')

plt.show()

# save word cloud
wordcloud.to_file('wordcloud.png')
