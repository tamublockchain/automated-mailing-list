# Automated Mailing List

In order to maintain our clubs mailing list, I designed a Python script that takes emails from our google form and preprocesses them into an easy
copy/paste format. Below are prerequistes and directions on how to use

### Prerequisites
1. Python 3.X
2. Anaconda/Miniconda 

### Directions 
1. Clone this repository locally via `git clone <link>` and ensure that the mailing list is the same. If not, you will have to change the form ID 
2. Create a virtual environment and install the requirements.txt file via `pip install -r requirements.txt`
3. Go to the executive drive and grab the token and credientials and copy them into the corresponding files 
4. Make sure you have access to the club email 
5. Run the python script via `python automated_mailing_list.py` and grab the emails from add.txt
6. Open Google Groups and copy and paste the add.txt contents into group members and submit
7. Clear the google form 
