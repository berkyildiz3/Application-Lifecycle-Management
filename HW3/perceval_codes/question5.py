import datetime
from perceval.backends.core.git import Git

repo = Git(uri="https://github.com/chaoss/grimoirelab-perceval.git", gitpath="/tmp/clonedir5")

noOfCommitsInSummer = 0
noOfCommitsInFall = 0
noOfCommitsInWinter = 0
noOfCommitsInSpring2020 = 0
noOfCommitsInSpring2019 = 0
noOfCommitsInSpringTotal = 0
maxNumberofCommits = 0

#count number of commits in summer 2019
for commit in repo.fetch(from_date=datetime.datetime(2019, 6, 21, 0, 0), to_date=datetime.datetime(2019, 9, 23, 0, 0)):
	noOfCommitsInSummer +=1 
print("Number of commits in summer: ", noOfCommitsInSummer)

maxNumberofCommits = noOfCommitsInSummer

#count number of commits in fall 2019
for commit in repo.fetch(from_date=datetime.datetime(2019, 6, 23, 0, 0), to_date=datetime.datetime(2019, 12, 21, 0, 0)):
	noOfCommitsInFall +=1 
print("Number of commits in fall: ", noOfCommitsInFall)

if(maxNumberofCommits < noOfCommitsInFall):
	maxNumberofCommits = noOfCommitsInFall

#count number of commits in winter 2019
for commit in repo.fetch(from_date=datetime.datetime(2019, 12, 21, 0, 0), to_date=datetime.datetime(2020, 3, 21, 0, 0)):
	noOfCommitsInWinter +=1 
print("Number of commits in winter: ", noOfCommitsInWinter)

if(maxNumberofCommits < noOfCommitsInWinter):
	maxNumberofCommits = noOfCommitsInWinter

#count number of commits in spring 2020, up to today
for commit in repo.fetch(from_date=datetime.datetime(2020, 3, 21, 0, 0)):
	noOfCommitsInSpring2020 +=1 
print("Number of commits in spring 2020: ", noOfCommitsInSpring2020)

#count number of commits in spring 2019, starting from March 8
for commit in repo.fetch(from_date=datetime.datetime(2019, 4, 8, 0, 0), to_date=datetime.datetime(2019, 6, 21, 0, 0)):
	noOfCommitsInSpring2019 +=1 
print("Number of commits in spring 2019: ", noOfCommitsInSpring2019)

#total number of commits in spring for last 365 days
numberOfCommitsInSpringTotal = noOfCommitsInSpring2020+noOfCommitsInSpring2019
print("Number of commits in spring (last 365 days): ", numberOfCommitsInSpringTotal)

if(maxNumberofCommits < numberOfCommitsInSpringTotal):
	maxNumberofCommits = numberOfCommitsInSpringTotal

if(maxNumberofCommits == noOfCommitsInSummer):
	print("Season with most number of commits: Summer, Number of commits: ", maxNumberofCommits) 	
elif(maxNumberofCommits == noOfCommitsInFall):
	print("Season with most number of commits: Fall, Number of commits: ", maxNumberofCommits)
elif(maxNumberofCommits == noOfCommitsInWinter):
	print("Season with most number of commits: Winter, Number of commits: ", maxNumberofCommits)
elif(maxNumberofCommits == noOfCommitsInSpringTotal):
	print("Season with most number of commits: Spring, Number of commits: ", maxNumberofCommits)

