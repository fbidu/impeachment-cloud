from os import path
from wordcloud import WordCloud
import csv

current_dir = path.dirname(__file__)
votes = csv.reader(
    open(path.join(current_dir, 'votes.csv')),
    delimiter=',', quotechar='"')

votes_yes = []
votes_no = []
votes_men = []
votes_women = []

for row in votes:
    if row[3].lower() == 'sim':
        votes_yes.append(row[5])
    else:
        votes_no.append(row[5])

    if row[4].lower() == 'm':
        votes_men.append(row[5])
    else:
        votes_women.append(row[5])

votes_yes = ' '.join(votes_yes)
votes_no = ' '.join(votes_no)
votes_men = ' '.join(votes_men)
votes_women = ' '.join(votes_women)

blacklist = (
    'do', 'da', 'no', 'na', 'de', 'que', 'se', 'os', 'ao', 'aos'
    'um', 'uma', 'deputado', 'sr', 'em', 'presidente', 'pelo', 'pela', 'para',
    'meu')
word_cloud = WordCloud(width=1080, height=720, stopwords=blacklist)
word_cloud.generate(votes_yes).to_file('yes.png')
word_cloud.generate(votes_no).to_file('no.png')
word_cloud.generate(votes_men).to_file('men.png')
word_cloud.generate(votes_women).to_file('women.png')
