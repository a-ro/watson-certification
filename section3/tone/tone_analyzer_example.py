import os

import numpy
import pandas
import seaborn
from matplotlib import pyplot
from watson_developer_cloud import ToneAnalyzerV3

from config import TONE_ANALYZER_USERNAME, TONE_ANALYZER_PASSWORD


def tone_analyzer_example():
    tone_analyzer = ToneAnalyzerV3(username=TONE_ANALYZER_USERNAME, password=TONE_ANALYZER_PASSWORD,
                                   version='2016-05-19')
    text = __read_text()
    document_tone = tone_analyzer.tone(text=text)
    dataframe = __create_dataframe(document_tone)
    __save_csv(dataframe)
    __create_heatmap(dataframe)


def __read_text():
    file_path = __get_file_path('angry-text.txt')
    with open(file_path, 'r') as text_file:
        text = text_file.read()
    print('Text to analyze:')
    print(text)
    print()
    return text


def __create_dataframe(document_tone):
    formatted_sentence_tones = []
    for sentence_tone in document_tone['sentences_tone']:
        current_tones = {'sentence': sentence_tone['text']}
        for tone_category in sentence_tone['tone_categories']:
            category = tone_category['category_name']
            tones = tone_category['tones']
            category_tones = {'{}:{}'.format(category, tone['tone_name']): tone['score'] for tone in tones}
            current_tones.update(category_tones)
        formatted_sentence_tones.append(current_tones)
    dataframe = pandas.DataFrame(formatted_sentence_tones)
    return dataframe


def __save_csv(dataframe):
    dataframe.to_csv(__get_file_path('analyzed-tone.csv'))
    print('Results were saved in analyzed-tone.csv')


def __create_heatmap(dataframe):
    tone_values, tone_names = __get_tone_values_and_tone_names(dataframe)
    pyplot.subplots(figsize=(12, 8))
    heatmap = seaborn.heatmap(tone_values)
    heatmap.set(ylabel='Tone', xlabel='Sentence')
    heatmap.set_yticklabels(labels=tone_names, rotation=0)
    pyplot.savefig(__get_file_path('analyzed-tone.png'))
    print('Heatmap created with tone results per sentence! View results in analyzed-tone.png')
    pyplot.show()


def __get_tone_values_and_tone_names(dataframe):
    tone_values_without_sentences = numpy.array(dataframe.values[:, :-1], dtype=numpy.float)
    transposed_tone_values = numpy.transpose(tone_values_without_sentences)
    tone_names = [column_name.split(':')[1] for column_name in dataframe.columns[:-1]]
    transposed_tone_names = list(reversed(tone_names))
    return transposed_tone_values, transposed_tone_names


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    tone_analyzer_example()
