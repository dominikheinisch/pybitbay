import pandas as pd
from requests import Session
from typing import Generator


class BitbayApi:
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
        trades = Session().get(f'https://bitbay.net/API/Public/{ticker}/trades.json?since={since}').json()
        return pd.json_normalize(trades)
