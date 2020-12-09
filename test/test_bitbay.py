import pytest
import pandas as pd

from pybitbay import BitBayAPI


TICKER = 'btcpln'
JSON_DATA = [
    {"date": 1396094988, "price": 4500.0, "type": "buy", "amount": 0.0129, "tid": "0"},
    {"date": 1396096603, "price": 4400.0, "type": "sell", "amount": 0.011364, "tid": "1"},
]
COLUMNS = JSON_DATA[0].keys()
EXPECTED_DF = pd.DataFrame(
    data=JSON_DATA,
    columns=COLUMNS
)


class MockResponse:
    def json(self):
        return JSON_DATA


class EmptyMockResponse:
    def json(self):
        return {}


def test_BitBayAPI(mocker):
    mocker.patch('requests.Session.get', side_effect=[MockResponse(), EmptyMockResponse()])
    trades = BitBayAPI().get_all_trades(ticker=TICKER)
    assert next(trades).equals(EXPECTED_DF)
    with pytest.raises(StopIteration):
        next(trades)


def test_bitbay_public_api():
    df = BitBayAPI().get_trades(ticker=TICKER, since=-1)
    print(COLUMNS)
    assert list(COLUMNS) == df.columns.tolist()
    assert df[0:2].equals(EXPECTED_DF)
