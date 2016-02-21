# TapeBagel Interpreter
An *extremely* simple interpreter for the esoteric programming language [TapeBagel](http://esolangs.org/wiki/TapeBagel), implemented in Python 2.

Written as part of the Internetwache CTF 2016, full challenge writeup [here](https://github.com/ctfs/write-ups-2016/tree/master/internetwache-ctf-2016/reversing/eso-tape-80)

## Usage
 ```python tapebagel.py path-to-tb-file```

## Under the hood
The interpret function expects a single input string, with operations separated by a single space character. The string is split into a list, then iterated through and interpreted against the program environments state array and idx pointer.
