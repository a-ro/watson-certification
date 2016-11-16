# watson-certification
Study Guide for Watson Certification

I made this guide to study before the Watson certification exam. I was following this [guide](http://public.dhe.ibm.com/partnerworld/pub/certify/Study_Guide_C7020_230.pdf)  released by IBM which details the exam objectives. Note that these answers are my own and have not been validated by IBM.

Due to a lack of time, I only coded examples with Watson Services I've never used before. I already passed my certification so I won't add anything more.

# Sections
- [Section 1 - Fundamentals of Cognitive Computing](https://github.com/a-ro/watson-certification/blob/master/section1/section1.md)
- [Section 3 - Fundamentals of IBM Watson Developer Cloud](https://github.com/a-ro/watson-certification/blob/master/section3/section3.md)

# Installation
``` shell
pip install -r requirements.txt
```

# Examples
To run the examples, you need to change the credentials in [config.py](https://github.com/a-ro/watson-certification/blob/master/config.py) with your own credentials.

## Personality Insights
``` shell
python section3/personality/personality_insights_example.py
```
## Tone Analyzer
``` shell
python section3/tone/tone_analyzer_example.py
```
## Visual Recognition
Classify images with the default ibm classifier:
``` shell
python section3/vision/predict_ibm_classifier.py 
```
Train a custom fruit classifier.
``` shell
python section3/vision/train_fruit_classifier.py 
```
Use your custom fruit classifier to classify images. You must add the classifier_id in the config.py file.
``` shell
python section3/vision/predict_custom_classifier.py 
```