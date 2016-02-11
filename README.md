# gkanapass
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

__Be aware:__  gkanapass is forcing a min password length of 8.


## xkcd/936 (password strength)
https://xkcd.com/936/
![xkcd](https://raw.githubusercontent.com/yafp/gkanapass/master/doc/xkcd_936_password_strength.png)


## Supported platforms
gkanapass was tested so far on the following setups/platforms
- Linux (using python2 and python3)
