import browserhistory as bh
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


# function to plot word cloud
def plot_cloud(wordcloud):
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud)
    plt.axis("off")


hist = bh.get_browserhistory()
browsers = hist.keys()
# print(hist['chrome'])

# chrome
searches = hist['chrome']

search_history = []
# process the searches
for search in searches:
    if 'google' and 'search' in search[0]:
        print(search[1])
        search_history.append(search[1])

# print(searches)

# Generate word cloud
text = ''.join(search_history).lower()
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
# Plot

plt.imshow(wordcloud, interpolation='bilInear')
plt.axis('off')
plt.show()
