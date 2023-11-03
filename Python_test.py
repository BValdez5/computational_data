#! /usr/bin python3
import pandas as pd


# we have a csv file with 6 columns
# column 1: timestep
# column 2: strain id
# column 3: line id
# column 4: growth rate replicate 1
# column 5: growth rate replicate 2
# column 6: growth rate replicate 3
# code to open this csv with pandas and parse it

# read in csv file
df = pd.read_csv("Ancestor18C_Growthrates_long_format.csv", sep=",", header=None)

# rename columns
df.columns = ['timestep', 'strain_id', 'line_id', 'growth_rate_rep1', 'growth_rate_rep2', 'growth_rate_rep3']

# sort by strain id and line id
df = df.sort_values(by=['strain_id', 'line_id'])

# write to csv
df.to_csv("Ancestor18C_Growthrates_long_format_sorted.csv", index=False)