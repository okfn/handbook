Getting Started With Git
========================

A recipe for working with Git repositories if you've know idea what git is...

TO DO - some sort of preamble about file version control?

TO DO  - something about installing git on your computer?



In the browser:

- create a profile on github.org
- create your own clone of the datapatterns repository on github from https://github.com/okfn/datapatterns/
- the URL of the project that is created will be something like 'github.com/YOUR_USER_NAME/datapatterns'

Open a terminal on your computer [THIS IS GOING TO BE WAY OUT OF COMFORT ZONE FOR A LOT OF PEOPLE - NEED TO RECOMMEND APPS RATHER THAN COMMAND LINE?]

Go to a directory where you want to store a local copy of the git archive and the files associated with it

  git clone git@github.com:YOUR_USER_NAME/datapatterns

This will create a directory 'datapatterns' and pull down all the associated files.


??IS THIS TOO COMPLICATED? EASIER WAY FOR FOLK TO JUST WORK WITH ONLY THEIR FILES AND NOT HAVE CLONED COPIES LOCALLY OF ANY OTHER FILES?

?? WOULD AN AEASIER WAY IN TO GET FOLK TO POST A GIST TO GIST.GITHUB.COM AND TRY TO WORK FROM THERE?

Add your own file, eg myfile.rst in the datapatterns/text directory. (.rst is blah..TO DO..)

Add the file to the actual local repository (git add) along with a message that says something about the creation of this file or the edits/changes you have made to it. You should also use /git add/ to add an updated copy of the file to the repository whenever you have made chages to the file and saved them:

  git add myfile.rst
  git commit -m 'first commit'

To synch the versions of your files that have been committed in your own local directory, use:

  git push

