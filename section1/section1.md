# Section 1 - Fundamentals of Cognitive Computing

## 1.1. Define the main characteristics of a cognitive system

Cognitive systems are applications that use **artificial intelligence**. They process information and provide responses with the aim of improving human decision-making. They often use **natural language processing** methods to process **unstructured** data and to interact with the user. 

### Question Answering Example
A question-answering system is an example of a cognitive system. The user would interact with this system by asking a question, and the system would provide a part of text answering this question. 

To provide an answer, the system first needs to **understand** the question of the user in some way. For instance,  the system could find meaningful keywords in the question or classify the topic of the question. In this case, the input data (question) is **unstructured**, but cognitive systems can also deal with **structured data** like CSV files (with numbers and categories). The system then needs to **reason** to find the most appropriate answer. This reasoning could be done by comparing the keywords of the question with the keywords of predefined answers in a database. The system could then **prioritize** a set of answers based on this comparison, and form a **hypothesis** by selecting the most probable one.

### Learning
Cognitive systems use **machine learning** algorithms to **learn** from data. Often, the performances of trained machine learning models can improve as we add more training data.

**Supervised learning** algorithms can learn a function (model) from labelled data to predict the output associated with an input.  For instance, a supervised learning algorithm could learn a model that predicts the topic (output category) associated with a question (input). This algorithm would be trained on a dataset of questions where the topic of each question (label) is known. 

**Unsupervised learning** algorithms can learn a function from unlabelled data that aims to predict a good representation of an input. A clustering algorithm is an example of unsupervised learning algorithm that can group a set of documents into clusters. The model learned can then be used to map a new document (input) to the most appropriate document cluster.