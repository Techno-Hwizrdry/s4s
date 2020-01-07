# S4S
A Jupyter notebook for plotting time (in years) vs. total salaries and wins of a baseball team. 

# Prerequisites
This jupyter notebook requires python3, python3-pip, python-virutalenv, requests, pandas, matplotlib, and jupyter.  Since this document assumes that S4S
will run on your local machine (for development only), all 3 must be installed on your local machine before the app can be used.

The prerequisites can be installed on a Debian based linux machine, like so:

`sudo apt-get update && sudo apt-get install python3 python3-pip && pip3 install virtualenv`

Once those prerequisites have been installed, git clone this repo, cd into it, and activate the virtual environment:

`cd /path/to/s4s && source udnenv/bin/activate`

Then install requests, pandas, matplotlib, and jupyter by running this command:

`pip3 install -r requirements.txt`

# Quick Start
To run this jupyter notebook, run the following command from the s4s directory:

`jupyter notebook`

Copy the URL from the terminal output and paste it into your preferred web browser.  It should look something like this:

`http://localhost:8888/?token=a7c2dc76aa7072178773e19d195cad5ef93496ca13cbd111`

Click on s4s.ipynb, and then click the "Run" button.  The graph will be rendered on the bottom of the page.

