Git branch status
-----------------

This is a small little utility script, to track what the current state of a branch is.

Why you say? your workflow should be indictive of this?
Well lets say, you left first thing after running a test, you want to say that this must be tested again before being merged with master.
Using your workflow rather than relying on manual notes is the best way for most things, but this allows you to quickly write little notes about each branch.

Usage
=====

For the best results, I symlink the python file to /usr/bin as follows:
ln -s <path_to_python_file> /usr/bin/git-bs

The reason for the symlink is two fold:
- Its now on your path.
- Git finds executables of the from git-<pattern> and allows you to call them like "git bs". This means it becomes part of your workflow.

Use git branch status as follows:

git bs set "some message goes here"
git bs set # This will clear all messages, and delete the config option.
git bs get # returns any messages logged.

TODO
====
- Some post commit, post merge scripts would be nice to update it automagically when it has been rebased into master.
