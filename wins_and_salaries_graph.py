# Author:  Alexan Mardigian
from   itertools import cycle
import matplotlib.pyplot as plt
import numpy as np

Y_AXES = ['salaries', 'wins']

#  This function will return a list of salaries formatted by a factor of ten.
#  1000000 is the default factor that will be used if no salary_factor is passed in.
def get_formatted_salaries(team_data_by_years, salary_factor=1000000):
    return [x/salary_factor for x in team_data_by_years['salary'].tolist()]  # Format the Salaries axis in millions.

#  This function will return a filtered data frame of total salaries and total wins,
#  based on a team (teamID) and a range of years.
def filter_team_data_by_years(salaries_and_wins, teamID, start_year, end_year):
    # Get all the rows, indexed by teamID, from salaries_and_wins.
    # If the index of salaries_and_wins was previously set to 'teamID'
    # then skip executing the set_index() method.  Otherwise a KeyError
    # will crash the script.

    try:
        salaries_and_wins.set_index('teamID', inplace=True)
    except KeyError:
        pass

    team_data = salaries_and_wins.loc[teamID]

    # Then trim down and return those results based on the year range.
    team_data.set_index('yearID', inplace=True)

    return team_data.loc[start_year:end_year]

#  Problem 1(d).  To display the relationship between total wins and total salaries for a given year,
#  I would use two different axes that share the same x axis.  Since wins and salaries share the year range (x-axis),
#  I can plot the second series (total salaries) against the secondary Y axis on the right side of the graph.

def graph_dual_y(salaries_and_wins, teamID, start_year=1871, end_year=2013):
    team_data_by_years = filter_team_data_by_years(salaries_and_wins, teamID, start_year, end_year)

    #  Separte the wins from the total salaries.  These will be our y-axes.
    #  t is our x-axis, labeling the year range.
    t = np.arange(start_year, end_year + 1)
    y_wins = team_data_by_years['W'].tolist()
    y_salaries = get_formatted_salaries(team_data_by_years)

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

#  This method will plot a line graph of total salaries (or total wins) over a give range of years
#  for a given team.  The string parameter, y_axis, can be set to either 'salaries' or 'wins'.
#  if y_axis is not 'salaries' or 'wins', then an error will printed to standard out to the user.
def graph_xy_line(salaries_and_wins, teamID, column, start_year=1871, end_year=2013):
    if column.lower() not in Y_AXES:
        print("ERROR wins_and_salaries_graph.graph_xy_line(): %s is not a column in the salaries_and_wins data frame" % (column))
    else:
        team_data_by_years = filter_team_data_by_years(salaries_and_wins, teamID, start_year, end_year)

        t = np.arange(start_year, end_year + 1)  #  t is our x-axis, labeling the year range.
        y_plot  = None
        color   = ''
        y_label = ''

        if column.lower() == 'salaries':
            color   = 'tab:blue'
            y_label = 'Total Salaries (in millions of USD)'
            y_plot  = get_formatted_salaries(team_data_by_years)
        else:
            color   = 'tab:red'
            y_label = 'Wins' 
            y_plot  = team_data_by_years['W'].tolist()

        fig, ax1 = plt.subplots()

        ax1.set_xlabel('Years for ' + teamID)
        ax1.set_ylabel(y_label, color=color)
        ax1.plot(t, y_plot, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.show()

#  This function will graph boxplots of the total salaries or wins of all the teams
#  listed in teamIDs, over a given range of years. 
def graph_boxplots(salaries_and_wins, teamIDs, column, start_year=1871, end_year=2013):
    if column.lower() not in Y_AXES:
        print("ERROR in wins_and_salaries_graph.graph_boxplot(): %s is not a column in the salaries_and_wins data frame" % (column))
    else:
        data_to_plot = []
        title  = ''

        if column.lower() == 'salaries':
            title  = 'Total Salaries (in millions of USD) between %d and %d' % (start_year, end_year)
        else:
            title  = 'Wins between %d and %d' % (start_year, end_year)

        #  Get the total salaries (or wins) for each team in teamIDs ready for the box plots.
        for teamID in teamIDs:
            team_data_by_years = filter_team_data_by_years(salaries_and_wins, teamID, start_year, end_year)

            if column.lower() == 'wins':
                data_to_plot.append(team_data_by_years['W'].tolist())
            else:
                data_to_plot.append(get_formatted_salaries(team_data_by_years))


        fig, ax1 = plt.subplots()
        box = ax1.boxplot(data_to_plot, vert=False, labels=teamIDs, patch_artist=True)
        ax1.set_title(title)

        #  Cycle through the list of colors (or through the list of teamIDs) to make the boxplots more colorful.
        colors = ['magenta', 'yellow', 'cyan', 'green']
        colored_boxes = zip(box['boxes'], cycle(colors)) if len(box['boxes']) > len(colors) else zip(cycle(box['boxes']), colors)

        fig.tight_layout()

        plt.show()

def xy_scatter_wins_totalsalaries(salaries_and_wins, teamIDs, start_year=1871, end_year=2013):
    wins_to_plot = []
    salaries_plot = []

    for teamID in teamIDs:
        team_data_by_years = filter_team_data_by_years(salaries_and_wins, teamID, start_year, end_year)
        wins_to_plot.append(team_data_by_years['W'].tolist())
        salaries_plot.append(get_formatted_salaries(team_data_by_years))
