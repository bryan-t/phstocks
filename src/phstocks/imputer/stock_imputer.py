import sys
import pandas as pd
import numpy as np


def impute_stock_data (data):
    for i in range(0, len(data.columns)):
        before = np.nan
        after = np.nan
        for j in range (0, len(data)):
            try:
                if not np.isnan(data.iloc[j, i]):
                    after = np.nan
                    before = data.iloc[j, i]
                    continue
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                print('data in exception: ', data.iloc[j, i])
                sys.exit(1)

            if not np.isnan(before):
                data.iloc[j, i] = before
                continue
            if np.isnan(after):
                for k in range(j + 1, len(data)):
                    if not np.isnan(data.iloc[k, i]):
                        after = data.iloc[k, i]
                        break
            
            if np.isnan(after):
                print(data.columns[i],' column has no data at all. Exiting...')
                sys.exit(3)

            before = after
            data.iloc[j, i] = after
    return data
