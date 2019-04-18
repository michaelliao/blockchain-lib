# blockchain-lib

Generate client-side library for blockchain

### HOW TO generate blockchain-lib.js

1. Install Node.js.

2. Run script `python3 gen.py`.

3. Get generated file at `blockchain-lib.js`.

### HOW TO add extra lib

1. Add lib to `package.json`.

2. Add name to `EXPORTS = ['your-lib', 'bitcoinjs-lib', ...]` in `gen.py`.

3. Run script again.
