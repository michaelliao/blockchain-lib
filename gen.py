#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, subprocess

EXPORTS = ['bitcoinjs-lib', 'bigi', 'rlp', 'ethereumjs-tx', 'ethereumjs-util', 'bs58', 'bs58check', 'bip38', 'bip39', 'wif', 'bech32', 'create-hash', 'randombytes']

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def run(cmd, cwd=None, stdout=None):
    kw = {}
    kw['cwd'] = cwd if cwd else CURRENT_DIR
    if stdout:
        kw['stdout'] = stdout
    subprocess.call(cmd.split(' '), **kw)

def main():
    run('rm -rf node_modules')
    run('npm install')
    run('npm install -g browserify')
    with open(os.path.join(CURRENT_DIR, 'index.js'), 'w') as f:
        f.write('// auto-generated index.js:\n\n')
        f.write('window.Buffer = require("buffer").Buffer;\n')
        for name in EXPORTS:
            f.write('require("%s");\n' % name)
    genCmd = 'browserify -r buffer %s index.js' % ' '.join(map(lambda s: '-r ' + s, EXPORTS))
    with open(os.path.join(CURRENT_DIR, 'blockchain-lib.js'), 'w') as f:
        run(genCmd, stdout=f)
    print('generated ok.')

if __name__ == '__main__':
    main()
