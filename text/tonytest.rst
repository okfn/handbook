Getting Started With Git
========================

A recipe for working with Git repositories if you've know idea what git is...

TO DO - some sort of preamble about file version control

TO DO  - something about installing git on your computer?


In the browser:

- create your own clone of the datapatterns repository on github
- the URL will be something like 'github.com/YOUR_USER_NAME/datapatterns'

Open a terminal
Go to a directory you want to store a local copy of the git archive

  git clone git@github.com:YOUR_USER_NAME/datapatterns

This will create a directory 'datapatterns' and pull down all the associated files.

Add your own file, eg myfile.rst in the text directory. (.rst is blah..TO DO..)

Add the file to the actual local repository (git add) along with a message that says something about the creation of this file or the edits/changes you have made to it. You should also use /git add/ to add an updated copy of the file to the repository whenever you have made chages to the file and saved them:

  git add myfile.rst
  git commit -m 'first commit'

To synch the versions of your files that have been committed in your own local directory, use:

  git push

