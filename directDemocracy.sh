#!/bin/bash

# Requires Preprocessor.js
preprocess src/democracy/directDemocracy.sol src 1> build/directDemocracy.sol
cd build
solc --binary file directDemocracy.sol
solc --json-abi file directDemocracy.sol
cd ..
