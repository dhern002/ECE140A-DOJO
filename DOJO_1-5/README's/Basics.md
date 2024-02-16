# DOJO 1:

## Env Basics:
### Git and Github:
#### Initializing a git repo:
Do this in the root of the project directory which you want to track. When you use git clone on an existing repo, you don't need to do this.
a git repo will be initialized automatically.
```bash
git init
```
#### Adding files to the staging area:
This is adding files to the staging area, not the repo itself. The staging area is where you can add files to be commited
to the repo. Think about it as just placing some items in a box, but not sealing it or shipping it.
```bash
git add <file>
```
To add all files and folders in the working directory, run the below command.
```bash
git add .
```
#### Commiting files to the repo:
This is commiting the files in the staging area to the repo. It is a checkpoint you create in your local git tree.
Think about it as sealing the box that you placed items in.
```bash 
git commit -m "commit message"
```
#### Pushing files to a remote repo:
This is pushing the files in the local repo to a remote repo. This is for syncing your local repo with a remote repo.
Generally good idea to pull before push to make sure you are incorporating remote changes. Think about it as shipping 
the box that you sealed to a remote location. 
```bash
git push
```

#### Pulling files from a remote repo:
This is pulling the files from a remote repo to your local repo. This is for syncing your local repo with a remote repo.
```bash
git pull
```

#### Checking the status of your local repo:
This command is very useful for checking the status of your local repo. It will tell you what files are staged, what files
are not tracked, and what files are modified.
```bash
git status
```

#### Side Note:
.gitignore is a file that you can create in your project directory. This file will tell git to ignore certain files or
directories. This is useful for not tracking files that you don't want to track. For example, you don't want to track
your virtual environment directory, any credentials or database files.

We included a .gitignore file in this repo. Please add your virtual environment and the text file you created to this



### Python:
#### Creating a virtual environment:
This is creating a virtual environment for your project. This is a good idea because it will keep your project dependencies
separate from your global python installation. This is also a good idea because it will allow you to easily share your
project with others. Think about it as creating a box for your project to live in.

Great News! Python 3 comes with a built in virtual environment manager. No need to install any program.
You can create a virtual environment by running
```bash
python3 -m venv <name of virtual environment>
```
Once you run this command you should see a new directory in your project directory called <name of virtual environment>.
This directory will include a bin directory which will have a python executable. This is the python executable that you
will use for your project. You can activate the virtual environment by running the following command on Unix (MacOS, Linux):
```bash
source <name of virtual environment>/bin/activate
```
On Windows machines, run:
```bash
.\<name of virtual environment>\Scripts\activate
```
Once you run this command you should see the name of your virtual environment in parenthesis in your terminal. This means
that you have successfully activated your virtual environment. You can deactivate your virtual environment by running the
following command:
```bash
deactivate
```
#### Conda:
Conda is a package manager for python. it has multiple flavors: most common are conda and miniconda. Conda is might be
necessary over pip if you are installing complex packages that require a lot of dependencies.
##### Anaconda:
Anaconda is a full package manager for python. It comes with a lot of packages pre-installed. It is a good choice if you
are just starting out with python and don't want to worry about installing packages. 
##### Miniconda:
Miniconda is a minimal package manager for python. It comes with a few packages pre-installed. It is a good choice if you
are more experienced with python and want to have more control over what packages are installed.
##### Conda commands:
```bash
conda create -n <name of virtual environment> python=<python version>
```
This command will create a virtual environment with the name <name of virtual environment> and the python version <python version>.
```bash
conda activate <name of virtual environment>
```
This command will activate the virtual environment with the name <name of virtual environment>.
```bash
conda deactivate
```
This command will deactivate the virtual environment.
```bash
conda install <package name>
```
This command will install the package <package name> in the virtual environment.

