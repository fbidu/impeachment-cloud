from os import path
from wordcloud import WordCloud
import csv

current_dir = path.dirname(__file__)
votes = csv.reader(
    open(path.join(current_dir, 'votes.csv')),
    delimiter=',', quotechar='"')

votes_yes = []
votes_no = []

for row in votes:
    if row[3].lower() == 'sim':
        votes_yes.append(row[5])

    else:
        votes_no.append(row[5])

votes_yes = ' '.join(votes_yes)
votes_no = ' '.join(votes_no)

WordCloud(width=1080, height=720).generate(votes_yes).to_file('yes.png')
WordCloud(width=1080, height=720).generate(votes_no).to_file('no.png')
