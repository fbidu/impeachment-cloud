from os import path
from wordcloud import WordCloud, ImageColorGenerator
import csv
import numpy as np
from PIL import Image

current_dir = path.dirname(__file__)
votes = csv.reader(
    open(path.join(current_dir, 'votes.csv')),
    delimiter=',', quotechar='"')

brazil_colors = ImageColorGenerator(
    np.array(
        Image.open(
            path.join(current_dir, "Flag_of_Brazil.png")
        )
    )
)

votes_all = []
votes_yes = []
votes_no = []
votes_men = []
votes_women = []

for row in votes:
    votes_all.append(row[5])

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
votes_all = ' '.join(votes_all)

blacklist = (
    'voto', 'srs', 'mas', 'minha', 'tão', 'portanto', 'sou',
    'do', 'da', 'no', 'na', 'de', 'que', 'se', 'os', 'ao', 'aos',
    'um', 'uma', 'deputado', 'sr', 'em', 'presidente', 'pelo', 'pela', 'para',
    'meu', 'por', 'dos', 'eu', 'com', 'como', 'das', 'nome', 'as', 'sua',
    'esse', 'este', 'seu', 'nas', 'deu', 'esta', 'tem', 'também', 'sra',
    'pelas', 'nos', 'mais', 'nesta', 'foi', 'me', 'meus',
    'há', 'aqui', 'ano', 'vou', 'ter', 'tenho', 'sras', 'são',
    'neste', 'nós', 'nem', 'ser', 'está', 'nossa', 'isso', 'já', 'muito',
    'mim', 'fazer', 'aquele', 'às', 'você', 'digo', 'vai', 'estamos')
word_cloud = WordCloud(width=1080, height=720,
                       stopwords=blacklist, color_func=brazil_colors,
                       max_words=100)
word_cloud.generate(votes_yes).to_file('yes.png')
word_cloud.generate(votes_no).to_file('no.png')
word_cloud.generate(votes_men).to_file('men.png')
word_cloud.generate(votes_women).to_file('women.png')
word_cloud.generate(votes_all).to_file('all.png')
