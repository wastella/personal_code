import gensim.downloader as api
wv = api.load('word2vec-google-news-300')

for i, word in enumerate(wv.vocab):
    if i == 10:
        break
    print(word)
