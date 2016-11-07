# Section 3 - Fundamentals of IBM Watson Developer Cloud

## 3.7. Explain how Personality Insights service works.
Personality Insights analyzes the personality attributes of someone based on a text written by that person.

- The input is a text which could be taken from social media, blogs or emails, and must be in a JSON, Text, or HTML format.
- The service outputs a set of personality attributes in JSON or CSV format

### The personality models
From [Personality Insights Documentation](http://www.ibm.com/watson/developercloud/doc/personality-insights/basics.shtml)

- **Big Five** personality characteristics represent the most widely used model for generally describing how a person engages with the world. The model includes five primary dimensions:
    - Agreeableness is a person's tendency to be compassionate and cooperative toward others.
    - Conscientiousness is a person's tendency to act in an organized or thoughtful way.
    - Extraversion is a person's tendency to seek stimulation in the company of others.
    - Emotional Range, also referred to as Neuroticism or Natural Reactions, is the extent to which a person's emotions are sensitive to the person's environment.
    - Openness is the extent to which a person is open to experiencing a variety of activities.
  Each of these top-level dimensions has six facets that further characterize an individual according to the dimension.
- **Needs** describe which aspects of a product will resonate with a person. The model includes twelve characteristic needs: Excitement, Harmony, Curiosity, Ideal, Closeness, Self-expression, Liberty, Love, Practicality, Stability, Challenge, and Structure.
- **Values** describe motivating factors that influence a person's decision making. The model includes five values: Self-transcendence / Helping others, Conservation / Tradition, Hedonism / Taking pleasure in life, Self-enhancement / Achieving success, and Open to change / Excitement.

## 3.8. Explain how Tone Analyzer service works.
The tone analyzer service analyzes the tone of a text. It can be used for any use cases requiring to write or analyze a text where the tone of the text is important: personal and business communications, market research, automated contact-center agent.

### Tone Categories
- Emotion: Anger, Disgust, Fear, Joy, Sadness
- Language: Analytical, Confident, Tentative
- Social: Openness, Conscientiousness, Extraversion, Agreeableness, Emotional Range

### API Call
Call *tone* method with *text* or *body*. Can specify the tone category with *tones='Emotion'*. Use *sentences=False* to remove the sentence level analysis.

### Blog Post Example
Write a blog post. Send post text to tone analyzer. Verify the results and modify your text to change how people will perceive your online identity.

### Difference with Alchemy
Alchemy sentiment only analyzes whether a sentence has a positive, negative, or mixed sentiment. Alchemy emotions analyzes the emotions using the whole text (Anger, Disgust, Fear, Joy, Sadness). Tone analyzer can return the emotions for each sentence. Tone analyzer also analyzes the social and language tones.