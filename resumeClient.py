keywords = ['the','teaching'] #TODO how are we acquiring these keywords
keyweights = [1,3]
applicantScore = 0.0
skills = []

import PyPDF2
import re
pdfFileObject = open('test.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
#import theasauraus
#filter out emails and phone numbers
#self-train the model based on people who get jobs (can have employers rate applicants)

page = 0
numPages = pdfReader.getNumPages()
while (page < numPages):
    pageObj = pdfReader.getPage(page)
    text = pageObj.extractText()
    words = text.split(' ')
    print (text)
    for a in range(len(words)):
        words[a] = re.sub(r'\W+', '', words[a]).lower()
    for word in words:
        if word in keywords and word not in skills:
            applicantScore += keyweights[keywords.index(word)]
            skills.append(word)
    page += 1

maxScore = sum(keyweights)

percentScore = (applicantScore/maxScore) * 100
print (percentScore)