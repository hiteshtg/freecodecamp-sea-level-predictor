import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('~/codes/data_science/code_camp/boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin = linregress(df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    x_fit1 = pd.Series([i for i in range(1880, 2051)])
    y_fit1 = lin.slope*x_fit1 + lin.intercept
    
    plt.plot(x_fit1, y_fit1, color='red')   
    
    # Create second line of best fit
    df_cat = df.loc[df['Year'] >= 2000]
    
    lin_2 = linregress(df_cat['Year'], y=df_cat['CSIRO Adjusted Sea Level'])
    
    x_fit2 = pd.Series([j for j in range(2000, 2051)])
    y_fit2 = lin_2.slope*x_fit2 + lin_2.intercept
    
    ax.plot(x_fit2, y_fit2, color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()