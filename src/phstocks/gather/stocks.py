import requests
import re
import pandas as pd
import sys

def get_stock_data(symbol, start, end):
    print('fetching: ', symbol, start, end)
    r = requests.get('https://edge.pse.com.ph/companyDirectory/search.ax',
                     params = { 'companyId': '', 'keyword':symbol, 'sector':
                               'ALL', 'subsector': 'ALL'})
    match = re.search("cmDetail\('[0-9]+','[0-9]+'\)", r.text)
    if match == None:
        raise Exception("Didn't find symbol: " + symbol)
    split = match[0].split('\'')
    company_id = split[1]
    sec_id = split[3]

    r = requests.post('https://edge.pse.com.ph/common/DisclosureCht.ax', json =
                      {"cmpy_id": company_id,"security_id": sec_id,"startDate": start, 
                       "endDate":end})
    json_data = r.json()
    df = pd.DataFrame(json_data['chartData'], columns =
                      ["OPEN","VALUE","CLOSE","CHART_DATE","HIGH","LOW"])
    df['CHART_DATE'] = pd.to_datetime(df['CHART_DATE'], format='%b %d, %Y %H:%M:%S')
    df = df.rename(columns={"OPEN" : "open", "VALUE": "value","CLOSE": "close",
                            "CHART_DATE": "dt", "HIGH": "high", "LOW":"low"})
    df.set_index('dt', inplace=True)

    return df

def get_stock_symbols():
    r = requests.get('https://www.pesobility.com/stock')
    matches = re.findall('<td><a href="/stock/.*"', r.text)
    symbols = []
    for match in matches:
        symbol = match.split('/')[2][:-1]
        symbols.append(symbol)
    return symbols

def get_all_stock_close(start, end):
    # get stocks data for each symbol
    symbols = get_stock_symbols()
    data = None
    first = True
    for symbol in symbols:
        df = None
        try:
            df = get_stock_data(symbol, start, end)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            continue

        df.reset_index(level = 0, inplace = True)
        df = df[['dt', 'close']]
        df.set_index('dt', inplace=True)
        df.columns = [symbol]
        if first:
            data = df
            first = False
        else:
            data = pd.merge(data, df, how='outer', left_index = True,
                            right_index = True)
    return data
