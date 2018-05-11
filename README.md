# Wine Master Webapp
#### APMA E4990 Class Final Project
#### Team Members: Xiaojing Dong, Keran Li, Zhen Li, Zihan Yi
#### Our Webapp Link: http://www.winemaster.ml (http://www.winemaster.pythonanywhere.com)
#### Python Notebook Summary: https://github.com/zy2292/Wine-Master/blob/master/Final_Project_Wine_Master.ipynb

## Data Preprocessing & Feature Analyzation
#### Clean data
#### Select combination of features as primary keys
#### Use LDA to find topic groups behind 'descriptions'
#### Scrape Wine Labels from Internet to train & test the labels


## Image Label Recognition
#### Image preprocessing to improve OCR performance
Convert images to grayscale
Modified a pre-trained CTPN (Connectionist Text Proposal Network) and used it on text detection
#### Read training wine labels with Tesseract OCR

## Text Matching using Tversky index
#### String preprocessing
i. Remove the non-alphanumeric characters
ii. Remove whitespace and line breaks
iii. Convert all characters to uppercase
#### Implement approximate string matching algorithm
Tokenizer: n-gram
Similarity measure: Tversky index¶
Use weighted average of Tversky indices as the overall similarity score
#### Model Selection
Select the optimal weights when calculating the weighted Tversky index


## Content-Based Recommendation Engine
#### String preprocessing
#### Calculate TF-IDF (term frequency–inverse document frequency) and cosine similarity
Unigram TF-IDF indicates the importance of word in the wine description

## Webapp Design
#### Develop/host the Flask webapp with PythonAnywhere
#### Build a SQL database (MySQL) to store and retrieve data



