from collections import Counter
 
text = """
Python is great and Python is easy and Python is powerful.
Python helps in automation and AI.
"""
 
text = text.lower()
 
for ch in [".", ",", "!", "?", ";", ":"]:
    text = text.replace(ch, "")
 
words = text.split()
 
word_count = Counter(words)
 
top_5 = word_count.most_common(5)
 