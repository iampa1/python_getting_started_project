# %load q01_read_data/build.py
import yaml
data = 7

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    ##data = '../data/ipl_match.yaml'
    data = yaml.load(open('./data/ipl_match.yaml'))
    


    # return data variable
    return data







