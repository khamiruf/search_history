import browserhistory as bh
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


class BHistory():
    def __init__(self):
        self.bh = bh.get_browserhistory()
        self.browsers = self.bh.keys() # shows type of browsers
            
    def get_history(self):
        # chrome -- others cant test atm
        searches = self.bh['chrome']

        search_history = []
        # process the searches
        for search in searches:
            if 'google' and 'search' in search[0]:
                if "Google Search" in search[1]:
                    new_search = search[1].rsplit('-', 1)
                    print(new_search)
                    search_history.append(new_search[0])
        searches = ''.join(search_history)
        return searches

def plot_wordcloud(searches):
    # create wc obj
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(searches)
    # plot
    plt.imshow(wordcloud, interpolation='bilInear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    BHist = BHistory()
    searches= BHist.get_history()
    plot_wordcloud(searches)


