# CS 6161: Algorithms Term Project

# Git Workflow 

As we add more and more code to the project, we must agree upon some basic rules to avoid stepping on each other's work. There are tools in place to make this easier (e.g. Git, linters,TravisCI, etc) but at the end of the day, it’s all about communication. If in doubt, use one of the communication channels to talk to someone.

### Commit Often  

Think of it like hitting save. Your last commit for the feature/fix/etc should be VERY detailed. Don’t use -m for it. Write a subject line (a single sentence summary of what you did), followed by an empty line, followed by a paragraph describing what you solved/fixed, followed by an empty line, followed by a paragraph describing how you solved it. Follow this format **strictly** for the **last** commit. This makes the code changes amazingly traceable using git blame (e.g. someone can see who changed a given line, when, why, and how).

[More details here][https://www.conventionalcommits.org/en/v1.0.0/#summary]

### Branch often 

Think of it like copy-pasting the source code into a new folder. Branches are very lightweight and an amazing way to isolate different works. Don’t be afraid to have many branches; you can quickly delete them if you need to. By using branches to isolate your work, you can avoid merge conflicts for the most part. Here are a few rules related to branches:

1. Name your branches using the following format: *theme_area_firstName*. The theme should be something like bugfix or refactoring. The area should be more specific to what you are fixing, refactoring, etc; e.g. viz or data. And, ofcourse, the firstname should be your first name.

2. You can’t push to the branches *master* and *development*. You need to make a pull request and at least 1 person needs to review and approve it, and TravisCI must green light it, before it gets merged into either of those branches. This is because master should always be stable and development should be stable enough for us to branch off of when we do work. 

3. Related to (2) above, use the Git Workflow. Branch off of development, do your work, write your unit tests, then push it to Travis to get the green light. If you are working with someone else on the same problem/feature, you should create a different branch to combine your works once you both finish working on your own and handle your merge conflicts there. Then make a pull request from the combined branch into development. **Pull request into development only** only the scrum master should directly touch the master branch. 


### Use Issues

Issues are the team’s todo list. Once we decide on a user story, we can break it down into issues and move it GitHub. Issues make it really easy to discuss code, progress, and larger goals. For example, if you have a line like Issue #12 in your commit, GitHub will link that commit in the issue comments. GitHub also provides a board for Agile development. All new issues go into the Backlog. When we decide to work on a given issue, we move it into Todo. It’s then moved into In Progress once someone starts working on it. When the issue is closed, Automation will put the issue into the Done column. This makes it easy to see who’s doing what and how much time we need to finish whatever feature/fix.

# Pip

Pip is a package manager. It grabs packages from https://pypi.org/ and 
install it on your system or env. 

- To search: 
```
pip search <package name>
```

- To install manually 
```
pip install <package1> <package2>
```

- To install from a req file
```
pip install -r <req filename>
```

- To uninstall 
```
pip uninstall <package1> <package2>
```
***
# Virtual Environment

Virtual environments provide consistency by providing all the package
requirments of a project. If it runs in your env, it should
run in my env too (assuming no system dep).

To create a virtual environment for python, make sure you have python3
installed with venv support (some systems split venv into its own package).
Then run: 

```
python3 -m venv <virtual env name>
```

- To start you env [on POSIX systems]

```
source <virtual env name>/bin/activate
```

- To stop using your env

```
deactivate
```
