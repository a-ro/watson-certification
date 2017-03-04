import os

import matplotlib
import numpy
import pandas
import seaborn
from matplotlib import pyplot
from watson_developer_cloud.personality_insights_v3 import PersonalityInsightsV3

from config import PERSONALITY_INSIGHTS_PASSWORD, PERSONALITY_INSIGHTS_USERNAME


def trump_personality_example():
    personality_insights = PersonalityInsightsV3(version='2016-10-20', username=PERSONALITY_INSIGHTS_USERNAME,
                                                 password=PERSONALITY_INSIGHTS_PASSWORD)
    trump_text = __read_text()
    response = personality_insights.profile(text=trump_text, accept='text/csv', csv_headers=True)
    profile = response.content.decode('utf-8')
    dataframe = __create_dataframe(profile)
    __save_to_csv(dataframe)
    __create_bar_plot(dataframe)


def __read_text():
    file_path = __get_file_path('trump.txt')
    with open(file_path, 'r') as text_file:
        text = text_file.read()
    text = text.encode('utf-8')
    print('Text trump.txt will be analyzed.')
    return text


def __create_dataframe(profile):
    lines = profile.split('\n')
    header = lines[0].split(',')
    row = lines[1].split(',')
    dataframe = pandas.DataFrame(data=[row], columns=header)
    return dataframe


def __save_to_csv(dataframe):
    file_path = __get_file_path('trump-personality-results.csv')
    dataframe.to_csv(file_path)
    print('CSV file created with trump personality results! Read results in trump-personality-results.csv')


def __create_bar_plot(dataframe):
    personality_results, column_names = __get_sorted_personality_traits_and_columns(dataframe)
    pyplot.subplots(figsize=(16, 20))
    colors = __create_colors_and_legend(column_names)
    # Use palette instead of hue in barplot because seaborn renders super thin bars when using hue (seaborn bug)
    seaborn.barplot(x=personality_results, y=column_names, orient="h", palette=colors)
    pyplot.savefig(__get_file_path('trump-personality-results.png'))
    print('Bar plot created with trump personality results! View results in trump-personality-results.png')
    pyplot.show()


def __get_sorted_personality_traits_and_columns(dataframe):
    NUMBER_OF_TRAITS = 52
    personality_results = numpy.array(dataframe.values[0][:NUMBER_OF_TRAITS], dtype=numpy.float)
    column_names = dataframe.columns[:NUMBER_OF_TRAITS]
    sorted_indexes = numpy.argsort(-personality_results)
    personality_results = personality_results[sorted_indexes]
    column_names = column_names[sorted_indexes]
    return personality_results, column_names


def __create_colors_and_legend(columns):
    category_names = [column_name.split('_')[0] for column_name in columns]
    unique_category_names = numpy.unique(category_names)
    palette = seaborn.color_palette("deep", len(unique_category_names))
    unique_colors = [palette[i] for i in range(len(unique_category_names))]
    category_to_color = dict(zip(unique_category_names, unique_colors))
    colors = [category_to_color[category] for category in category_names]
    legend_patches = [matplotlib.patches.Patch(color=color, label=category) for category, color in
                      category_to_color.items()]
    pyplot.legend(handles=legend_patches)
    return colors


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    trump_personality_example()
