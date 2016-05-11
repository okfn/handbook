---
title: Working with Git
---

GitHub is a "free" hosting service based on Git, assuming the role of a control version system. In simple terms, this allows 
the collaboration of multiple users without having issues with versions. 
Even though GitHub is easier working with the terminal, it also has graphical solutions. However, if you want to increase 
your productivity with GitHub, the rest of this guide will help you perform the basic commands of Git to create, publish 
online.

In any case, GitHub has a really comprehensive documentation which can help you resolve any issues not covered here.

The following guide is for Ubuntu users. We try to cover Windows commands as much as possible, even though Windows has a neat 
graphical interface that can surely help you get your things were you wanted.

### Installing Git

The first to do is, of course, install Git. You can download the latest version of Git [here](https://git-scm.com/downloads).
Next, you need to configure Git. 
To do so, open your terminal and let Git know your name and your email:

```
$ git config --global user.name "YOUR NAME"
$ git config --global user.email "YOUR EMAIL"
```

You can then authenticate using some security protocols. You can learn more about it [here](https://help.github.com/articles/set-up-git/#next-steps-authenticating-with-github-from-git), but that is a bit more advanced - easy to do, still.

### New Repository

Now!, let's create your first repository:

In the terminal, go to a new directory (`mkdir newDirectory` and then ` cd newDirectory`- same commands in Linux and Windows) 
and, once you are in there, you can create a new GitHub repository by writing `git init`.

Now you have to go to https://github.com and create a new repository through the web interface.

1. In the upper right menu, click plus and select `New Repository` ![image]({{ site.url }}/images/repo-create.jpg)
2. Repeat the name of the repository - so `newDirectory` should be it ![image]({{ site.url }}/images/create-repository-name.jpg)
3. Optionally, you can add a license and a readme file. Both are recommended, but you can add both later. ![image]({{ site.url }}/images/create-repository-init-readme.jpg)
4. In the bottom of the page, click `Create Repository`.

At this point, you have created a repository online and locally, but they are not connect.

5. If you open the repository page in your browser, under the status bar you have a dropdown menu saying SSH or HTTPS. Choose HTTPS if you did not configured SSH. 
![image]({{ site.url }}/images/remote-v-links.jpg)

6. In the same repository, you then write `git remote add origin`. To confirm your changes, you can tyoe `git remote -v` and it should show your link under "origin".
7. If you then finally write `git status`, you will see both repositories are connected because it will say there are some changes online that are not present in your local repository. To update it, run `git pull origin` and it will take care of things for you.

From here on, your changes will be tracked but not synced immediately. So you did your changes and what is next?

8. In the same repository, in the terminal, if you write `git status`, you should see all the changes as unstaged. To add them, you can either do `git add FILENAME` or just `git add -A`. Optionally, you can run `git add .`, which will only add file additions and file edits - it will not add, for instance, files you have removed locally.
9. Once you have pushed, the next command to run is `git commit -m "some commentary about your changes"`. This will prepare a commit from you.
10. Finally, if you run `git push origin` it will publish your changes online!

Voilá, your changes are online.

### Forking a repository

Forking a repository is key, specially when you are working on a project with other people. How to do it is equally easy.
In the repository page on GitHub, there is a fork menu at the top. If you click on Fork, you will have menu asking to which 
page you want to fork that - you, any organization you control, etc. ![image]({{ site.url }}/images/remote-v-links.jpg)
Clicking in yourself will create that repository in your account - but not locally. How can you then create it locally?

First pick a directory you want to have that repository - again, the command is `cd ~/directory` (in windows you have to write the full directory). 

Then, picking the repository auth URL (either as HTTPS or SSH, as you have it configured), run `git clone link-of-the-repository`.
This will create (or clone) the repository locally. 

You can then do the changes you want and then perform the same `git status - git add - git commit -m - git pish` routine previously described.

