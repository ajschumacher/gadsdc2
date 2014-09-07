%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

races = pd.read_csv('data/five_plus_ironman_races.csv')
ironman_florida = pd.read_csv('data/ironman_florida_m.csv')

# Get data for a sample athlete
athlete_races = races[(races.athlete_id == 1020) & (races.qualifier_id==7504)].sort('year')

print "Total athlete races =>", len(athlete_races)


ironman_florida_df = pd.DataFrame([{'year': year,
                                    'min_final_time': race_group.final_time.min(),
                                    'max_final_time': race_group.final_time.max(),
                                    'min_cycle_time': race_group.cycle_time.min(),
                                    'max_cycle_time': race_group.cycle_time.max(),
                                    'min_run_time': race_group.run_time.min(),
                                    'max_run_time': race_group.run_time.max(),
                                    'min_swim_time': race_group.swim_time.min(),
                                    'max_swim_time': race_group.swim_time.max(),
                                   } for year, race_group in ironman_florida.groupby('year', sort=True)])


ironman_florida_outcome = ironman_florida_df[ironman_florida_df.year.apply(lambda x:x in athlete_races.year.tolist())]

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(athlete_races.final_time,'b')
axes.plot(ironman_florida_outcome.max_final_time, 'r')
plt.plot(ironman_florida_outcome.min_final_time, 'g')

axes.set_xlabel('race year')
axes.set_ylabel('final time')
axes.set_title('Ironman florida');

print ironman_florida_outcome.loc[:,['max_final_time', 'min_final_time']]

print athlete_races.loc[:,['final_time']]

fig.savefig('abhi01.png')


race_split_fig = plt.figure()

race_split_axes = race_split_fig.add_axes([0.1, 0.1, 0.8, 0.8])

race_split_axes.plot(ironman_florida_df.min_cycle_time,'r')
race_split_axes.plot(ironman_florida_df.min_swim_time,'g')
race_split_axes.plot(ironman_florida_df.min_run_time,'c')

race_split_axes.set_xlabel('race year')
race_split_axes.set_ylabel('time')
race_split_axes.set_title('Ironman florida');

print ironman_florida_df.loc[:,['min_cycle_time','min_swim_time','min_run_time']]

race_split_fig.savefig('abhi02.png')

from funcy import first, last

bins = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

ironman_florida_group_data = {}


for year, group in ironman_florida.groupby('year', sort=True):
    age_bins = pd.cut(group.age, bins=bins)
    ironman_florida_group_data[year] = []

    for bin_key, bin_group in group.groupby(age_bins):
        ironman_florida_group_data[year].append({'min_final_time': bin_group.final_time.min(),
                           'min_cycle_time': bin_group.cycle_time.min(),
                           'min_swim_time': bin_group.swim_time.min(),
                           'min_run_time': bin_group.run_time.min(),
                           'age_group': bin_key})


year_df = pd.DataFrame(ironman_florida_group_data[2001])

print year_df
group_split_fig = plt.figure()

group_race_split_axes = group_split_fig.add_axes([0.1, 0.1, 0.8, 0.8])

group_race_split_axes.plot(year_df.min_final_time,'k')
group_race_split_axes.plot(year_df.min_cycle_time,'r')
group_race_split_axes.plot(year_df.min_swim_time,'g')
group_race_split_axes.plot(year_df.min_run_time,'c')

group_race_split_axes.set_xlabel('age group')
group_race_split_axes.set_ylabel('time')
group_race_split_axes.set_title('Ironman florida');


group_split_fig.savefig('abhi03.png')
