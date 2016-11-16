import os

import pandas
from watson_developer_cloud import VisualRecognitionV3

from config import VISUAL_RECOGNITION_API_KEY

FRUIT_MAN_URL = "https://www.colourbox.com/preview/2742446-fruit-man.jpg"
CHUCK_NORRIS_URL = 'http://cdn.business2community.com/wp-content/uploads/2016/03/Vd3MJo.jpg'
CAT_URL = 'https://grumpycatgoesgreen.files.wordpress.com/2013/09/grumpy-cat-d0b3d180d183d181d182d0bdd18bd0b9-d0bad0bed182-d0bad0b0d180d182d0b8d0bdd0bad0b8-d0bfd0b5d181d0bed187d0bdd0b8d186d0b0-632538.jpeg'
UNICORN_MAN_URL = 'https://imgflip.com/s/meme/Unicorn-MAN.jpg'


def vision_ibm_default_classifier_example():
    image_urls = [FRUIT_MAN_URL, CHUCK_NORRIS_URL, CAT_URL, UNICORN_MAN_URL]
    visual_classifier = VisualRecognitionV3(api_key=VISUAL_RECOGNITION_API_KEY, version='2016-05-20')
    results = __classify_all_images(image_urls, visual_classifier)
    dataframe = pandas.DataFrame(results)
    dataframe.to_csv(__get_file_path('ibm-classifier-predictions.csv'))
    print('All images have been classified. Verify the results in ibm-classifier-predictions.csv')


def __classify_all_images(image_urls, visual_classifier):
    results = []
    for image_url in image_urls:
        prediction = visual_classifier.classify(images_url=image_url)
        classifier_results = prediction['images'][0]['classifiers']
        image_result = __format_results(image_url, classifier_results[0])
        results.append(image_result)
    return results


def __format_results(image_url, default_classifier_results):
    classes = []
    scores = []
    image_result = {'url': image_url}
    for category in default_classifier_results['classes']:
        classes.append(str(category['class']))
        scores.append(str(category['score']))
    image_result['classes'] = ','.join(classes)
    image_result['score'] = ','.join(scores)
    return image_result


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    vision_ibm_default_classifier_example()