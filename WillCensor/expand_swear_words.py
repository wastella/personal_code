import gensim.downloader as api
wv = api.load('word2vec-google-news-300')

with open('swear_words.txt', 'r') as f:
    profanity_list = f.readlines()
for bad_word in profanity_list:
    stripped_bad_word = bad_word.strip()
    print(stripped_bad_word)
    try:
        most_similar = wv.most_similar(positive=[stripped_bad_word], topn=5)
        for s in most_similar:
            if s[1] >= 0.6:
                print(s[0])
    except KeyError:
       pass 
        
