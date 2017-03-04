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
For seaborn to work, you need to install tkinter
``` shell
sudo apt-get install python3-tk
```
# Examples
To run the examples, you need to change the credentials in [config.py](https://github.com/a-ro/watson-certification/blob/master/config.py) with your own credentials.

## Personality Insights
Run the example to analyze Trump personality with the following command:
``` shell
python section3/personality/personality_insights_example.py
```
### Trump Personality Analysis
The code uses this [Donald Trump speech](https://github.com/a-ro/watson-certification/blob/master/section3/personality/trump.txt) in text format as input.

We can obtain the results in a CSV format that shows a percentage for each personality trait: 

 |**big5\_agreeableness**|**facet\_altruism**|**facet\_cooperation**|**facet\_modesty**|**facet\_morality**|**facet\_sympathy**|**facet\_trust**|**big5\_conscientiousness**|**facet\_achievement\_striving**|**facet\_cautiousness**|**facet\_dutifulness**|**facet\_orderliness**|**facet\_self\_discipline**|**facet\_self\_efficacy**|**big5\_extraversion**|**facet\_activity\_level**|**facet\_assertiveness**|**facet\_cheerfulness**|**facet\_excitement\_seeking**|**facet\_friendliness**|**facet\_gregariousness**|**big5\_neuroticism**|**facet\_anger**|**facet\_anxiety**|**facet\_depression**|**facet\_immoderation**|**facet\_self\_consciousness**|**facet\_vulnerability**|**big5\_openness**|**facet\_adventurousness**|**facet\_artistic\_interests**|**facet\_emotionality**|**facet\_imagination**|**facet\_intellect**|**facet\_liberalism**|**need\_liberty**|**need\_ideal**|**need\_love**|**need\_practicality**|**need\_self\_expression**|**need\_stability**|**need\_structure**|**need\_challenge**|**need\_closeness**|**need\_curiosity**|**need\_excitement**|**need\_harmony**|**value\_conservation**|**value\_hedonism**|**value\_openness\_to\_change**|**value\_self\_enhancement**|**value\_self\_transcendence**|**behavior\_sunday**|**behavior\_monday**|**behavior\_tuesday**|**behavior\_wednesday**|**behavior\_thursday**|**behavior\_friday**|**behavior\_saturday**|**behavior\_0000**|**behavior\_0100**|**behavior\_0200**|**behavior\_0300**|**behavior\_0400**|**behavior\_0500**|**behavior\_0600**|**behavior\_0700**|**behavior\_0800**|**behavior\_0900**|**behavior\_1000**|**behavior\_1100**|**behavior\_1200**|**behavior\_1300**|**behavior\_1400**|**behavior\_1500**|**behavior\_1600**|**behavior\_1700**|**behavior\_1800**|**behavior\_1900**|**behavior\_2000**|**behavior\_2100**|**behavior\_2200**|**behavior\_2300**|**word\_count**|**processed\_language**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
0|0.4268979029309932|0.8588535687537024|0.7044867158268264|0.5960736895707534|0.9676444453908276|0.9965335147666688|0.3998040334289172|0.9797657117581102|0.9070143051529225|0.9869915635122488|0.873983697434251|0.5488031217574947|0.9124250982342645|0.8090432365930695|0.6096825298389489|0.8828473589475007|0.9857260415356135|0.11637254228155247|0.01331810918980908|0.5959055919648221|0.16756739770553347|0.9505346628850558|0.02812768408642924|0.02455406377266378|0.168454469161186|0.05865378787277559|0.05754389444307567|0.015989819272919148|0.975519694665306|0.8328642953776038|0.654203608334551|0.24646836689211954|0.05370347126940961|0.9915865625089948|0.7792134600310711|0.01694074812415025|0.04771121338963841|0.0030600042610637868|0.023556425868524244|0.05084809704946042|0.23156088075382475|0.6470820764350991|0.028222045621644876|0.15436495592219218|0.3881229129662421|0.03816743693922564|0.035899020822038996|0.11167207177920224|0.01957680225835251|0.37441584209106304|6.717299135493016E-4|0.11547777255812258|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|6832|en

With a bit of seaborn magic, we can visualize Trump's personality results a bit more clearly:

![Image of Yaktocat](https://github.com/a-ro/watson-certification/blob/master/section3/personality/trump-personality-results.png)

According to the Personality Insights documentation, people who score high on __Sympathy__ are tender-hearted and compassionate.
Seriously Watson, Trump's highest personality trait is SYMPATHY? ;) 
But hey, I do agree he clearly doesn't need love.

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