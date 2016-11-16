import os

import pandas
from watson_developer_cloud.personality_insights_v3 import PersonalityInsightsV3

from config import PERSONALITY_INSIGHTS_USERNAME, PERSONALITY_INSIGHTS_PASSWORD


def trump_personality_example():
    personality_insights = PersonalityInsightsV3(version='2016-10-20', username=PERSONALITY_INSIGHTS_USERNAME,
                                                 password=PERSONALITY_INSIGHTS_PASSWORD)
    trump_text = __read_text()
    response = personality_insights.profile(text=trump_text, accept='text/csv', csv_headers=True)
    profile = response.content.decode('utf-8')
    __save_to_csv(profile)


def __read_text():
    file_path = __get_file_path('trump.txt')
    with open(file_path, 'r') as text_file:
        text = text_file.read()
    text = text.encode('utf-8')
    print('Text trump.txt will be analyzed.')
    return text


def __save_to_csv(profile):
    lines = profile.split('\n')
    header = lines[0].split(',')
    row = lines[1].split(',')
    dataframe = pandas.DataFrame(data=[row], columns=header)
    file_path = __get_file_path('trump-personality-results.csv')
    dataframe.to_csv(file_path)
    print('Done! Read results in trump-personality-results.csv')


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    trump_personality_example()