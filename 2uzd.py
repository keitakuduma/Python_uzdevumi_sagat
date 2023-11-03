""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1) Kas ir RSS? REALLY SIMPLE SYNDICATION
jaunumi un saturs, satura agregatori(abonēšana)
2) plūsmu no google.lv
pats par sevi ir vietne, bet nav satura radītāja. google izmanto RSS.


pip install feedparser
...pip upgrade ... 

"""
import feedparser

#URL uz RSS plūsmu 
rss_url='https://news.google.com/home?hl=en-LV&gl=LV&ceid=LV:en'
# iegūstam RSS plūsmas datus un veicam analizi
kkk=feedparser.parse(rss_url)

#noformēšana
for entry in kkk.entries:
    print("Virsraksts", entry.title)
    print("Saite", entry.link)
    #print("Publicēšanas datums", entry.published)
    print("\n")
