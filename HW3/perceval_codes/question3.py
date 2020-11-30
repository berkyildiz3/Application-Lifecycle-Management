import datetime
from perceval.backends.core.git import Git

repo = Git(uri="https://github.com/eclipse", gitpath="/tmp/clonedir5")
noOfCommitsLastThreeMonths = 0
dateListOfCommits = []
listOfContributors = []
noOfTotalCommits = 0
noOfContributors = 0;

#count number of commits in past three months
for commit in repo.fetch(from_date=datetime.datetime(2020, 1, 8, 0, 0)):
	noOfCommitsLastThreeMonths +=1 

#fetch contributors and dates of the commits
for commit in repo.fetch():
	noOfTotalCommits += 1
	dateListOfCommits.append(commit['data']['CommitDate'])
	if commit['data']['Author'] not in listOfContributors:
		listOfContributors.append(commit['data']['Author'])

print("Number of commits in past three months: ", noOfCommitsLastThreeMonths)
print("Number of total commits: ", noOfTotalCommits)
print("Date of first commit: ", dateListOfCommits[0])
print("Date of last commit: ", dateListOfCommits[noOfTotalCommits-1])
dateOfFirstCommit = datetime.datetime.strptime(dateListOfCommits[0], '%a %b %d %H:%M:%S %Y %z')
dateOfLastCommit = datetime.datetime.strptime(dateListOfCommits[noOfTotalCommits-1], '%a %b %d %H:%M:%S %Y %z')
dateDifference = dateOfLastCommit - dateOfFirstCommit
print("Number of days between last and first commits: ", dateDifference)
print("Number of contributors: ", len(listOfContributors))
print("Contributors: ", listOfContributors)
