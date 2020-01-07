# Author:  Alexan Mardigian

import matplotlib.pyplot as plt
import numpy as np

#  Problem 1(d).  To display the relationship between total wins and total salaries for a given year,
#  I would use two different axes that share the same x axis.  Since wins and salaries share the year range (x-axis),
#  I can plot the second series (total salaries) against the secondary Y axis on the right side of the graph.

def graph(salaries_and_wins, teamID, start_year=1871, end_year=2013):
    # Get all the rows, indexed by teamID, from salaries_and_wins.
    salaries_and_wins.set_index('teamID', inplace=True)
    team_data = salaries_and_wins.loc[teamID]

    # Then trim down those results based on the year range.
    team_data.set_index('yearID', inplace=True)
    team_data_by_years = team_data.loc[start_year:end_year]

    #  Separte the wins from the total salaries.  These will be our y-axes.
    #  t is our x-axis, labeling the year range.
    t = np.arange(start_year, end_year + 1)
    y_wins = team_data_by_years['W'].tolist()
    y_salaries = [x/1000000 for x in team_data_by_years['salary'].tolist()]  # Format the Salaries axis in millions.

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Years for ' + teamID)
    ax1.set_ylabel('Wins', color=color)
    ax1.plot(t, y_wins, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Total Salaries (in millions of USD)', color=color)
    ax2.plot(t, y_salaries, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.ticklabel_format(axis='y', style='plain')

    fig.tight_layout()
    plt.show()

