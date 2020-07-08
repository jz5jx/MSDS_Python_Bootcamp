# load pandas package
import pandas as pd
df =  pd.read_csv("andre.csv")

# Part 2: remove data from 1976 and after 1993
df = df[ df.Year > 1976 ]
df = df[ df.Year < 1994 ]

# Part 3: make a histogram
df.hist("H",bins=100)