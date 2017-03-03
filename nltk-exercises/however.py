import nltk

emma=nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

emma.concordance("However")
