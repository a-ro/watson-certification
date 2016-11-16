import os
from os import listdir

import pandas
from watson_developer_cloud import VisualRecognitionV3

from config import VISUAL_RECOGNITION_API_KEY, VISUAL_RECOGNITION_CLASSIFIER_ID

def vision_custom_classifier_example():
    file_names = listdir(__get_file_path('images'))
    image_paths = [__get_file_path('images/{}'.format(file_name)) for file_name in file_names]
    visual_classifier = VisualRecognitionV3(api_key=VISUAL_RECOGNITION_API_KEY, version='2016-05-20')
    results = __predict_all_images(VISUAL_RECOGNITION_CLASSIFIER_ID, visual_classifier, image_paths)
    dataframe = pandas.DataFrame(results)
    dataframe.to_csv(__get_file_path('fruit-vs-non-fruit.csv'))
    print('All images have been classified. Verify the results in fruit-vs-non-fruit.csv')


def __predict_all_images(classifier_id, visual_classifier, image_paths):
    results = []
    for image_path in image_paths:
        prediction = __predict(classifier_id, visual_classifier, image_path)
        image_prediction_result = __format_result(prediction, image_path)
        results.append(image_prediction_result)
    return results


def __predict(classifier_id, visual_classifier, image_path):
    with open(image_path, 'rb') as image_file:
        prediction = visual_classifier.classify(images_file=image_file, classifier_ids=[classifier_id])
    return prediction


def __format_result(prediction, image_path):
    classifier_results = prediction['images'][0]['classifiers']
    image_name = image_path.split('/')[-1]
    if len(classifier_results) > 0:
        score = classifier_results[0]['classes'][0]['score']
        image_result = {'image_name': image_name, 'class': 'fruit', 'score': score}
        print('Fruit!! {}'.format(image_name))
    else:
        image_result = {'image_name': image_name, 'class': 'not a fruit', 'score': '?'}
        print('Not a fruit :( {}'.format(image_name))
    return image_result


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    vision_custom_classifier_example()