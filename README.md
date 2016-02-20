[![Code Health](https://landscape.io/github/yafp/gkanapass/master/landscape.svg?style=flat)](https://landscape.io/github/yafp/gkanapass/master)
[![License](https://img.shields.io/badge/license-GPL3-brightgreen.svg)](LICENSE)

 gkanapass
==========

![xkcd](https://raw.githubusercontent.com/yafp/gkanapass/master/doc/xkcd_936_password_strength.png)
https://xkcd.com/936/

## About
gkanapass is a python based password generator influenced by [kana](https://en.wikipedia.org/wiki/Kana)


You might ask
> why another password generator?

I was in need for a python playground, simple as that.

## Install / Uninstall
- Unpack the archive
- navigate to folder which contains this README.md
- Install by running:

> sudo make install

Uninstall by running:
> sudo make uninstall


## Usage
To display the general help:
> gkanapass -h

To generate passwords with default length (10)
> gkanapass

To generate passwords with user-defined length (14)
> gkanapass 14

![Usage](https://raw.githubusercontent.com/yafp/gkanapass/master/doc/gkanapass_usage_optimized.gif)

__Be aware:__  gkanapass is forcing a min password length of 8.


## Supported platforms
gkanapass was tested so far on the following setups/platforms
- Linux (using python2 and python3)
