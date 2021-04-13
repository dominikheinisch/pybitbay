# pybitbay

[![Build Status](https://github.com/dominikheinisch/pybitbay/workflows/Python%20package/badge.svg)](https://github.com/dominikheinisch/pybitbay/actions?query=workflow%3A"Python+package")

## Introduction

Unofficial API for Bitbay cryptocurrency exchange

Simple interface for collection public data.

## Installation
    
    -e git+https://github.com/dominikheinisch/pybitbay@#egg=pybitbay                         # HEAD
    -e git+https://github.com/dominikheinisch/pybitbay@v0.1.0#egg=pybitbay                   # v0.1.0
    pip3 show pybitbay

## Requirements

* Python >=3.8
* Requires Requests, Pandas

## BitBay API

### Data pulling

Getting single batch for ticker: 'btcpln', since transaction id (tid): 1234.
Returns pandas.DataFrame with data from https://bitbay.net/API/Public/btcpln/trades.json?since=1234

    from pybitbay import BitBayAPI

    df = BitBayAPI().get_trades(ticker='btcpln', since=1234)

Getting batch by batch (generator) of all trades, for ticker: 'btcpln', since transaction id (tid): -1, to the newest trade:

    from pybitbay import BitBayAPI

    for df in BitBayAPI().get_all_trades(ticker='btcpln', since=-1):
        print(df)

## Contribution

### Installation

    pip3 install -r requirements.txt
    pip3 install -e .

### Testing

    pytest -vs
