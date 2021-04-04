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

def get_all_stock_data(start, end):
    # prepare dataframe
    dates = pd.date_range(start, end).tolist()
    data = pd.DataFrame({'dt': dates})
    data.set_index('dt', inplace = True)

    # get stocks data for each symbol
    symbols = get_stock_symbols()
    for symbol in symbols:
        df = None
        try:
            df = get_stock_data(symbol, start, end)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            continue

        df = df[['close']]
        df.columns = [symbol]
        data = data.join(df)
    return data
