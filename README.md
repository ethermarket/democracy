# Democracy
A democratic governance system for dapps.

For now, just a collection of useful smart contracts.

## Requirements

To run the unit tests, you'll need [PyEthereum](https://github.com/ethereum/pyethereum) and [EtherTDD.py](https://github.com/ethermarket/ethertdd.py).

Running the unit tests can be done via command line from the project's root:

    python tests

This will run all the unit tests using whatever unit testing framework you have installed, falling back to the stock `unittest` module if one cannot be found.

As of right now, some of the tests trigger a bug in PyEthereum, so be aware of that.
