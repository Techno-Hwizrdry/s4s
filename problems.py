from   get_csv_files import get_zipped_csv_files
from   wins_and_salaries_graph import graph
import numpy
import pandas
import matplotlib.pyplot as plt

ZIP_URL = "http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip"

csv_files = ['Salaries.csv', 'Teams.csv']

salary_data = pandas.read_csv('Salaries.csv') #None
teams_data  = pandas.read_csv('Teams.csv')  #None

def problem_1a():
    #salary_data = pandas.read_csv('Salaries.csv')
    #teams_data  = pandas.read_csv('Teams.csv')

    salary_data.head()
    teams_data.head()

def problem_1b():
    salary_totals = salary_data.groupby(['yearID', 'teamID'])['salary'].sum()
    salary_totals.head()

    return salary_totals

def problem_1c(salary_totals):
    wins_and_salaries = pandas.merge(salary_totals, teams_data[['yearID', 'teamID', 'W']], on=['yearID', 'teamID'], how='inner')
    wins_and_salaries.head()

    return wins_and_salaries

def main():
    get_zipped_csv_files(url=ZIP_URL, csv_files=csv_files)

    problem_1a()
    sal_totals = problem_1b()
    wins_and_salaries = problem_1c(sal_totals)

    graph(wins_and_salaries, 'OAK', 2000, 2010)

if __name__ == '__main__':
	main()
