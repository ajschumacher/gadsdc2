### gadsdc2

Repository to collect (some but not all) student work for General Assembly's Data Science course in DC. To contain many great things!

#### Initial setup

 1. Fork the [main gadsdc2 repo](https://github.com/ajschumacher/gadsdc2) on GitHub
 2. `git clone URL_of_your_fork`: copy your fork to your local computer (and automatically add URL_of_your_fork as the remote origin)
 3. `cd gadsdc2`: change into the gadsdc2 subdirectory that was just created
 4. `git remote add upstream URL_of_main_gadsdc2_repo`: add URL_of_main_gadsdc2_repo as the remote upstream

#### Recipe for submitting assignments

 1. `git checkout master`: switch to the master branch of your local repo
 2. `git pull upstream master`: fetch changes from the master branch of upstream, and merge those changes into your working branch (which is currently master)
 3. `git checkout -b name_of_branch`: create a new topic branch and switch to it
 4. Do your assignment
 5. `git add .` or `git add name_of_file`: stage file modifications, additions, and deletions
 6. `git commit -m "message about commit"`: commit any changes that have been staged
 7. `git push origin name_of_branch`: push your branch (and its commits) to the origin
 8. Switch to name_of_branch on your GitHub account and submit a [pull request](https://help.github.com/articles/using-pull-requests): ask the upstream to merge your changes into its master branch

#### Other useful commands

 * `git status`: view the status of files in your repo (untracked, modified, staged)
 * `git log`: view the detailed commit history (type `q` to quit)
   * `git log -1`: only show the last commit (you can use any number)
   * `git log --oneline`: show each commit on a single line
 * `git branch`: view the list of local branches
 * `git remote -v`: view your remotes
 * [Detailed reference guide](http://gitref.org/)
