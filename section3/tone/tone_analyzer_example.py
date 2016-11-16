import os

import pandas
from watson_developer_cloud import ToneAnalyzerV3

from config import TONE_ANALYZER_USERNAME, TONE_ANALYZER_PASSWORD


def tone_analyzer_example():
    tone_analyzer = ToneAnalyzerV3(username=TONE_ANALYZER_USERNAME, password=TONE_ANALYZER_PASSWORD,
                                   version='2016-05-19')
    text = __read_text()
    document_tone = tone_analyzer.tone(text=text)
    __save_to_csv(document_tone)


def __read_text():
    file_path = __get_file_path('angry-text.txt')
    with open(file_path, 'r') as text_file:
        text = text_file.read()
    print('Text to analyze:')
    print(text)
    print()
    return text


def __save_to_csv(document_tone):
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
    dataframe.to_csv(__get_file_path('analyzed-tone.csv'))
    print('Results were saved in analyzed-tone.csv')


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    tone_analyzer_example()