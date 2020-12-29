#imported libraries
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv
import PyPDF2

#input file definitions
pdfFileObject = open('test1.pdf','rb')
filename = "demo.csv"
industry = "Internet"

#resume text extraction
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
resume_text = ""

page = 0
numPages = pdfReader.getNumPages()
while (page < numPages):
    pageObj = pdfReader.getPage(page)
    text = pageObj.extractText()
    resume_text += text
    page += 1

#resume text cleanup
for a in range(len(resume_text)):
    resume_text = resume_text.lower()

def cleanup(t):
    return (re.sub(". . ", ". ",re.sub(' +', ' ',t.replace("\n","").replace("\t","").replace("  "," "))))

resume_text = cleanup(resume_text)

#extracts keywords from string input
def keywordExtraction(t):
    return (keywords(t, ratio=0.25, lemmatize=True))

#the below two arrays work in parallel
indPostings = [] #job entry in csv
score = [] #scores for indPostings
  
#lists to retrieve csv file information
fields = [] 
rows = [] 
  
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
    fields = next(csvreader) 
    for row in csvreader: 
        rows.append(row) 

#defines columns of interest
indNum = 16 #column number
reqInd = 8

for entry in rows:
    if entry[indNum] == industry:
        c = cleanup(entry[reqInd])
        k = keywordExtraction(c)
        text_list = [resume_text, k]
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text_list)

        matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        matchPercentage = round(matchPercentage, 2) # round to two decimal

        score.append(matchPercentage)
        indPostings.append(entry)

#output of top three postings with their respective scores
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [[x,y] for y, x in sorted(zipped_pairs)]
    z.reverse()
    return z

sortedFR = sort_list(indPostings,score)

print('\n',sortedFR[0][0][2])
print(sortedFR[0][1])
print(sortedFR[0][0][6])

print('\n',sortedFR[1][0][2])
print(sortedFR[1][1])
print(sortedFR[1][0][6])

print('\n',sortedFR[2][0][2])
print(sortedFR[2][1])
print(sortedFR[2][0][6])