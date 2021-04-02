import requests
import re
import pandas as pd
#import logging
#import http.client

#http.client.HTTPConnection.debuglevel = 1

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True


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
