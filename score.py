# Import summarize from gensim
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
# Import the library to convert MSword doc to txt for processing.
import docx2txt
# RegEx
import re



# Store the resume in a variable
# Change resume name and location
resume = docx2txt.process("Varchasvi Vedula - Resume 10.10.docx")
text_resume = str(resume)#Summarize the text with ratio 0.1 (10% of the total words.)
summarize(text_resume, ratio=0.4)

# Some cleaning up

text_resume = re.sub(". . ", ". ",re.sub(' +', ' ',text_resume.replace("\n",". ").replace("\t","").replace("  "," ")))
# print(text_resume)
summarize(text_resume, ratio = 0.3)

text = input("Enter Job description : ") # Prompt for the Job description.
# Convert text to string format
text = str(text)#Summarize the text with ratio 0.1 (10% of the total words.)
summarize(text, ratio=0.50)


# recycle the text variable from summarizing
# creating A list of text
text_list = [text_resume, text]
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text_list)


from sklearn.metrics.pairwise import cosine_similarity
# get the match percentage
matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
matchPercentage = round(matchPercentage, 2) # round to two decimal
print("Your resume matches about "+ str(matchPercentage)+ "% of the job description.")
# output


print(keywords(text_resume, ratio=0.25)) 
# gives you the keywords of the job description