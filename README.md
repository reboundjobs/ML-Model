#Background

This repository contains the backend code for the "Rebound" website which was created to help people who have experienced joblessness due to COVID-19. The models provide suggestions for an applicant in terms of specific job postings that are aligned with their skills and also provide the applicant with top industries that they are qualified for if they are looking to make a bigger change in their career. On the "Rebound" website, an applicant is able to upload their resume in pdf format as well as indicate the industry they are interested in finding job postings for. Given this input and the job postings we have locally, specific job postings and other industries will be suggested that they might also be interested in.

#Setup

Several python libraries are required in order to run the scripts in this repository.
pip install can be used for the gensim, sklearn, csv and pypdf2 libraries/modules.
If you are not sure which of these modules you already have, you can go ahead and run the scripts
in terminal and the errors thrown will let you know what needs to be installed.

#Files

matching.py:
takes input of job postings as a csv file, a pdf resume, and industry of choice
outputs the top three jobs from that industry that are the best fit for the applicant

industry.py:
takes input of job postings as a csv file and a pdf resume
outputs the top three industries for which the applicant is the best fit

npl.py:
natural language processing syntax, some of which was used in the above two files

resumeClient.py:
initial code for the architecture of the client side

score.py
trial code to test the count vectorizer, cosine similarity and keyword extraction

test.pdf:
simple pdf with text to test pdf parsing functionality

test1.pdf:
example resume that can be used to observe behavior of industry.py and/or matching.py

test2.pdf:
example resume to test pdf parsing functionality

test3.pdf:
example pdf with text to test pdf parsing functionality

fjp.csv: 
large input test file for job postings

demo.csv: 
smaller input test file for job postings with some syntax adjustments for "requirements" tab

demo2.csv: 
smaller input test file for job postings

README.md:
describes the contents of the repository and provides instructions for developer

#Build and Run

python3 matching.py: this run's the matching.py file with inputs defined inside the python script
python3 industry.py: this run's the industry.py file with inputs defined inside the python script

To change inputs, change the string definitions just below the import lines in for the respective script. 
The files are locally referenced. The csv column definitions will also need to be changed further down in the script depending on which csv file is being used for testing. The developer can simply check which column represents the appropriate parameters when running a different input csv file.

But if you just want to try it out with no hastle, run with the definitions already included and it will work!
