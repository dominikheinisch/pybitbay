import pandas as pd
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from typing import Generator


class BitBayAPI:
    BASE_URL = 'https://bitbay.net/API/Public/'
    TRADES_SUFFIX = '/trades.json'
    SINCE_SUFFIX = '?since='

    def __init__(self):
        retry_strategy = Retry(
            total=5,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=['GET'],
        )
        self._http = Session()
        self._http.mount(
            prefix='https://',
            adapter=HTTPAdapter(max_retries=retry_strategy)
        )

    def get_all_trades(self, ticker: str, since: int = -1) -> Generator[pd.DataFrame, int, None]:
        '''
        :param ticker: eg. 'btcpln'
        :param since: (first trade's id (tid) in a batch) - 1
        :return: Generator[pd.DataFrame, int, None]
        '''
        df = self.get_trades(ticker, since)
        while not df.empty:
            since += len(df)
            yield df
            df = self.get_trades(ticker, since)

    def get_trades(self, ticker: str, since: int) -> pd.DataFrame:
        '''
        :param ticker: eg. 'btcpln'
        :param since: first trade's id (tid) in a batch
        :return: pandas.DataFrame
            Index:
                RangeIndex
            Columns:
                Name: date, dtype: int64
                Name: price, dtype: float64
                Name: type, dtype: object
                Name: amount, dtype: float64
                Name: tid, dtype: object
        '''
        response = self._http.get(
            url=f'{self.BASE_URL}{ticker}{self.TRADES_SUFFIX}{self.SINCE_SUFFIX}{since}',
            timeout=3,
        )
        return pd.json_normalize(response.json())
