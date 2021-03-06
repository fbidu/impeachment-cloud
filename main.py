#-*- encoding: utf-8 -*-
from os import path
from wordcloud import WordCloud, ImageColorGenerator
from csv import reader, writer
from numpy import array
from PIL import Image


def write_frequencies(frequencies, file_path):
    with open(file_path, 'w', newline='') as file:
        frequency_writer = writer(file, delimiter=',')
        frequency_writer.writerows(frequencies)


def main():
    # Getting the current directory
    current_dir = path.dirname(__file__)

    # Evaluating the path for the votes file and the Brazil's flag
    votes_file = path.join(current_dir, 'votes.csv')
    brazil_flag = path.join(current_dir, "Flag_of_Brazil.png")
    font = path.join(current_dir, "NotoSerif-Regular.ttf")

    # Reading the votes as a CSV object
    votes = reader(open(votes_file), delimiter=',', quotechar='"')

    # Creating a coloring function based on the Brazilian flag
    brazil_colors = ImageColorGenerator(array(Image.open(brazil_flag)))

    # Initializing arrays to hold the votes
    votes_all = []
    votes_yes = []
    votes_no = []
    votes_men = []
    votes_women = []

    # Looping through all the rows
    for row in votes:

        # All votes get appended to the votes_all array
        votes_all.append(row[5])

        # Now we'll check if the deputy voted yes or no
        # yes = impeach the president
        if row[3].lower() == 'sim':
            votes_yes.append(row[5])
        else:
            votes_no.append(row[5])

        # Then we'll check if the deputy was male or female
        if row[4].lower() == 'm':
            votes_men.append(row[5])
        else:
            votes_women.append(row[5])

    # All the arrays get joined together in a string
    votes_yes = ' '.join(votes_yes)
    votes_no = ' '.join(votes_no)
    votes_men = ' '.join(votes_men)
    votes_women = ' '.join(votes_women)
    votes_all = ' '.join(votes_all)

    # This is a list of the words we don't want in the word clouds
    blacklist = (
        'voto', 'srs', 'mas', 'minha', 'tão', 'portanto', 'sou', 'do', 'da',
        'no', 'na', 'de', 'que', 'se', 'os', 'ao', 'aos', 'um', 'uma',
        'deputado', 'sr', 'em', 'presidente', 'pelo', 'pela', 'para', 'meu',
        'por', 'dos', 'eu', 'com', 'como', 'das', 'nome', 'as', 'sua', 'esse',
        'este', 'seu', 'nas', 'deu', 'esta', 'tem', 'também', 'sra', 'pelas',
        'nos', 'mais', 'nesta', 'foi', 'me', 'meus', 'há', 'aqui', 'ano',
        'vou', 'ter', 'tenho', 'sras', 'são', 'neste', 'nós', 'nem', 'ser',
        'está', 'nossa', 'isso', 'já', 'muito', 'mim', 'fazer', 'aquele',
        'às', 'você', 'digo', 'vai', 'estamos', 'pelos', 'porque', 'minas',
        'gerais', 'paulo', 'vamos', 'ele', 'ela', 'quem', 'rio', 'janeiro',
        'sul', 'paraná', 'quando', 'bem', 'ano', 'anos', 'deste', 'quero',
        'desta', 'dia', 'estão', 'todo', 'grande', 'toda', 'essa', 'seus',
        'pernambuco', 'dias', 'tudo', 'maioria', 'santa', 'catarina', 'bahia',
        'favor', 'hoje', 'sem', 'querem', 'minhas', 'região', 'votando',
        'cada', 'pará', 'só', 'exa', 'mato', 'grosso', 'goiás', 'querida',
        'querido', 'muita', 'todas', 'sempre', 'nosso', 'todos', 'deputados',
        'casa', 'dizer', 'melhor', 'votar', 'fim', 'mineiro', 'primeiro',
        'temos')

    # Here we create de WordCloud object, defining its dimensions,
    # the stopwords, the coloring function, the font and how many words we want
    word_cloud = WordCloud(width=1080, height=720,
                           stopwords=blacklist, color_func=brazil_colors,
                           max_words=200, font_path=font)

    # Now we use that object to create the word clouds and save as images
    word_cloud.generate(votes_yes).to_file('yes.png')
    write_frequencies(word_cloud.words_, path.join(current_dir, 'yes.csv'))

    word_cloud.generate(votes_no).to_file('no.png')
    write_frequencies(word_cloud.words_, path.join(current_dir, 'no.csv'))

    word_cloud.generate(votes_men).to_file('men.png')
    write_frequencies(word_cloud.words_, path.join(current_dir, 'men.csv'))

    word_cloud.generate(votes_women).to_file('women.png')
    write_frequencies(word_cloud.words_, path.join(current_dir, 'women.csv'))

    word_cloud.generate(votes_all).to_file('all.png')
    write_frequencies(word_cloud.words_, path.join(current_dir, 'all.csv'))


if __name__ == "__main__":
    main()
