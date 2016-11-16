import os

from watson_developer_cloud import VisualRecognitionV3

from config import VISUAL_RECOGNITION_API_KEY


def create_classifier():
    visual_classifier = VisualRecognitionV3(api_key=VISUAL_RECOGNITION_API_KEY, version='2016-05-20')
    with open(__get_file_path('training/fruitbowl.zip'), 'rb') as fruit_files:
        with open(__get_file_path('training/not-fruit-bowls.zip'), 'rb') as no_fruit_files:
            print('Training a fruit classifier...')
            response = visual_classifier.create_classifier('fruit-classifier', fruit_positive_examples=fruit_files,
                                                           negative_examples=no_fruit_files)
            print('Classifier has been trained. Time to classify some fruits/non-fruits! (what a useless classifier)')
            print("Don't forget to change the classifier_id in config with the following id: {}"
                  .format(response['classifier_id']))


def __get_file_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


if __name__ == '__main__':
    create_classifier()