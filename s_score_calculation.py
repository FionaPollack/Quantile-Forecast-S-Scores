'''
Quantile forecasts can be read from a csv file or can be input manually.
If read from a csv file (e.g. one including multiple forecasters' quantile estimates), a new csv file be generated with s-scores for all the forecasters in the dataset.
If quantile forecasts are input manually, the script prints a list of the five s-scores for that particular forecaster.
'''

import sys
import pandas as pd

realized_value = int(input("What is the realized value? "))

quantile_forecasts = []

def s_score(forecast, quant, x):
    score = quant*(max(x-forecast, 0)) + (1-quant)*(max(forecast-x, 0))
    return score

if (len(sys.argv) == 2):
    forecasts_file = sys.argv[1]
    forecasts = pd.read_csv(forecasts_file)
    forecasts.set_index("Forecaster", inplace=True)
    print(forecasts)
    for forecaster in forecasts.index:
        quants = list(forecasts.loc[forecaster, '5th':'95th'])
        # Pull out the five forecasts from that person and put them in a list.
        # Performing the correct s-score calculation on each element in the list, in order.
        # Write the new s-scores into the new s_score CSV file.
else:
    s_scores = []

    quant1 = int(input("What is your 5th percentile forecast? "))
    s_score1 = s_score(quant1, 0.05, realized_value)
    s_scores.append(s_score1)

    quant2 = int(input("What is your 25th percentile forecast? "))
    s_score2 = s_score(quant2, 0.25, realized_value)
    s_scores.append(s_score2)

    quant3 = int(input("What is your 50th percentile forecast? "))
    s_score3 = s_score(quant3, 0.5, realized_value)
    s_scores.append(s_score3)

    quant4 = int(input("What is your 75th percentile forecast? "))
    s_score4 = s_score(quant4, 0.75, realized_value)
    s_scores.append(s_score4)

    quant5 = int(input("What is your 95th percentile forecast? "))
    s_score5 = s_score(quant5, 0.95, realized_value)
    s_scores.append(s_score5)

    print(s_scores)