# Section 3 - Fundamentals of IBM Watson Developer Cloud

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