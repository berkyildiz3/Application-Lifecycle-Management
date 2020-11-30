import datetime
from collections import Counter
from perceval.backends.core.git import Git

repo = Git(uri="https://github.com/chaoss/grimoirelab-perceval.git", gitpath="/tmp/clonedir5")

authorListOfCommits = []

#fetch contributor names of the commits
for commit in repo.fetch():	
	authorListOfCommits.append(commit['data']['Author'])

counter = Counter(authorListOfCommits)
personWithMostCommits = counter.most_common(1)
print("Person with most commits and number of commits: ", personWithMostCommits)


