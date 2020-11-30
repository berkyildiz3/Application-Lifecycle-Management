#! /usr/bin/env python3
# Count commits
import datetime
import argparse

from perceval.backends.core.git import Git

# Read command line arguments
parser = argparse.ArgumentParser(description = "Count commits in a git repo")
parser.add_argument("repo", help = "Repository url")
parser.add_argument("dir", help = "Directory for cloning the repository")
parser.add_argument("--print", action='store_true', help = "Print hashes")
args = parser.parse_args()

# create a Git object, and count commmits
repo = Git(uri=args.repo, gitpath=args.dir)
noOfCommitsPastThreeMonths = 0
for commit in repo.fetch(from_date=datetime.datetime(2020, 1, 8, 0, 0)):
	noOfCommitsLastThreeMonths +=1 


print("Number of commits in past three months: ", noOfCommitsPastThreeMonths)
#print(commit['data']['CommitDate'])
