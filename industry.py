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

def swapElements(list,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
  
#lists to retrieve csv file information
cat = [] 
rows = [] 
  
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
    cat = next(csvreader) 
    for row in csvreader: 
        rows.append(row) 

#defines columns of interest
indNum = 16 #column number
reqInd = 7

#these arrays are populated parallelly with the most important skills ranked for the different fields
fields = [] #1D array containing names of industries
skills = [] #3D array containing lists of most important skills in parallel with their weight 
            #(frequency of appearance in postings for respective industry)

for entry in rows:
    c = cleanup(entry[reqInd])
    k = "".join(list(keywordExtraction(c))).split("\n")
    if entry[indNum] in fields:
        ind = fields.index(entry[indNum])
        for word in k:
            if skills[ind]!=[] and (word in skills[ind][0]):
                i = skills[ind][0].index(word)
                skills[ind][1][i] += 1
                if (i!=0 and skills[ind][1][i-1]<skills[ind][1][i]):
                    swapElements(skills[ind][0],i,i-1)
                    swapElements(skills[ind][1],i,i-1)
            else:
                skills[ind][0].append(word)
                skills[ind][1].append(1)
    else:
        fields.append(entry[indNum])
        aL = len(k)
        skills.append([k,[1]*aL])

resKey = "".join(list(keywordExtraction(resume_text))).split("\n")
fieldRank = []
fieldScores = []

for i in range(len(skills)):
    [_,s] = skills[i]
    total = sum(s)
    for v in range(len(s)):
        skills[i][1][v] = round(1000*(float(skills[i][1][v])/total),2)

for f in range(len(fields)):
    currentScore = 0
    for k in resKey:
        if k in skills[f][0]:
            indK = skills[f][0].index(k)
            currentScore += skills[f][1][indK]
    fieldScores.append(currentScore)
    fieldRank.append(fields[f])

#output of top three fields with their respective scores
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [(x,y) for y, x in sorted(zipped_pairs)]
    z.reverse()
    return z

sortedFR = sort_list(fieldRank,fieldScores)
print(*sortedFR[1:4], sep = "\n")



