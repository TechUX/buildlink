[![Available on Pypi](https://img.shields.io/badge/Available%20on%20-Pypi-brightgreen.svg?style=flat-square)](https://pypi.org/project/buildlink/)
[![Awesome Badges](https://img.shields.io/badge/Pypi-Install-brightgreen?logo=pypi)](https://pypi.org/project/buildlink/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/buildlink.svg?logo=pypi)](https://pypi.python.org/pypi/buildlink/)
[![PyPI license](https://img.shields.io/pypi/l/buildlink.svg)](https://pypi.python.org/pypi/buildlink) <br>
[![Downloads](https://static.pepy.tech/personalized-badge/buildlink?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20pypi.org%20Downloads)](https://pepy.tech/project/buildlink)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/TechUX/buildlink/pulls)
[![GitHub issues](https://img.shields.io/github/issues/techux/buildlink.svg)](https://github.com/techux/buildlink/issues/) <br>

[![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WKXE8MtU_e-FCayONXChE-xJaNDIgURO?usp=sharing)
[![Owner : Devesh Singh](https://img.shields.io/badge/Owner%20-Devesh%20Singh-blue.svg?style=flat-square)](https://instagram.com/devesh92744)

# buildlink
[![Last Update](https://img.shields.io/badge/dynamic/xml?color=blue&label=Readme%20Last%20Updated&query=update&url=https%3A%2F%2Fraw.githubusercontent.com%2FTechUX%2Fbuildlink%2Fmain%2Flastupdate.xml&style=flat-square&?cacheSeconds=5)](https://github.com/TechUX/buildlink)

[![Available on Pypi](https://img.shields.io/badge/Available%20on%20-Pypi-brightgreen.svg?style=flat-square)](https://pypi.org/project/buildlink/)
[![Awesome Badges](https://img.shields.io/badge/Pypi-Install-brightgreen?logo=pypi)](https://pypi.org/project/buildlink/)
[![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WKXE8MtU_e-FCayONXChE-xJaNDIgURO?usp=sharing)

buildlink is a python program which helps you to shorten link with a single command without any registration or using any API Key. Its is capable of expanding any link available on internet. with support of wide range of domain names.

# Table of Content
- [buildlink](#buildlink)
- [Installation](#installation)
    - [Download Stats](#download-stats)
- [Features](#features)
    + [Link Shortening](#link-shortening)
    + [Link Expanding](#link-expanding)
- [Functions](#functions)
  - [expand(url)](#expandurl)
  - [shorten(url, service, alias)](#shortenurl-service-alias)
  - [help()](#help)
- [Options](#options)
- [Examples](#examples)
  * [Link shortening](#link-shortening)
    + [Shortening with service specified](#shortening-with-service-specified)
    + [Shortening with alias](#shortening-with-alias)
  * [Link Expanding](#link-expanding-1)
- [Supported Domain for link shortening](#supported-domain-for-link-shortening)
- [Supported Domain for link expanding](#supported-domain-for-link-expanding)
- [Issues & Pull Requests](#issues--pull-requests)
- [About](#about)
- [Author & License](#author--license)


<br>

# Installation
This package is available on *pypi.org*, So install it using ```pip```
```bash
pip install buildlink
```
[![Awesome Badges](https://img.shields.io/badge/Pypi-Install-brightgreen?logo=pypi)](https://pypi.org/project/buildlink/)

 
## Download Stats
**Downloads** from *[pypi.org](https://pypi.org/project/buildlink)*

[![Downloads](https://static.pepy.tech/personalized-badge/buildlink?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/buildlink)
[![Downloads](https://pepy.tech/badge/buildlink/week)](https://pepy.tech/project/buildlink)
[![Downloads](https://pepy.tech/badge/buildlink/month)](https://pepy.tech/project/buildlink)


# Features
- ### Link Shortening
buildlink has ability to shorten any long url into short url using 5 different service providers along with custom alias for shorten link

 <br>**Note :** ```alias``` for link shortening must be less than 30 characters. <br>
 *i.e.* ```shorten("url", alias="less than 30 char")``` <br><br>

- ### Link Expanding
with the help of ```expand()``` , you can expand any shorten link available on internet to their long form without visiting really to that link. <br> This is helpful when you get malicious short link and you want to know actual URL behind the shorten one, without clicking on the Link.

# Functions
- #### ```expand(url)```
This function takes one input as a parameter and return the Long URL associated with the short link. <br>
**Return Type :**  string

```python
expand("https://tinyurl.com/yuxh3b37")

# Output : https://github.com/TechUX/buildlink
```
[See Examples](#examples) [![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WKXE8MtU_e-FCayONXChE-xJaNDIgURO?usp=sharing)

- #### ```shorten(url, service, alias)```
This function takes three parameters as a input, url, service for shortening, and alias . <br>
**Return Type :** list - list of shortened URL , *if no service is privided*

```python
shorten("https://github.com/TechUX/buildlink", service="tinyurl")

# Output : https://tinyurl.com/yuxh3b37
```

[See Examples](#examples) [![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WKXE8MtU_e-FCayONXChE-xJaNDIgURO?usp=sharing)

- #### ```help()```
This function display a basic help page of the package.

## Options
There are 5 options which is available for ```service```.
<br> These are as follow :

  | Service | Domain |
  |:---------: | :--------: |
  | tinyurl | tinyurl.com |
  | isgd | is.gd |
  | clckru | clck.ru |
  | chilpit | chilp.it |
  | daga | da.gd |
 
 **Note :** length of ```alias``` must be less than 30 characters.
 
# Examples
[![Run on Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WKXE8MtU_e-FCayONXChE-xJaNDIgURO?usp=sharing)
## Link shortening
```python
import buildlink as link

long_url = "https://github.com/TechUX/buildlink/blob/main/README.md"

shorten_url = link.shorten(long_url)

print(shorten_url)

# Output : ['https://tinyurl.com/2mksjsq7', 'https://is.gd/e8tsIB', 'https://clck.ru/33GnAf', 'http://chilp.it/6c70182\n', 'https://da.gd/tsttQ\n']
```

### Shortening with service specified 
for this, just add the ```service="<service_value>``` parameter.
```python
import buildlink as link

long_url = "https://github.com/TechUX/buildlink/blob/main/README.md"

shorten_url = link.shorten(long_url, service="tinyurl")

print(shorten_url)

# Output : https://tinyurl.com/2mksjsq7
```

### Shortening with alias
```python
import buildlink as link

long_url = "https://github.com/TechUX/buildlink/blob/main/README.md"

shorten_url = link.shorten(long_url, alias="pylink")

print(shorten_url)

# Output : https://is.gd/pylink

```

## Link Expanding
```python
import buildlink as link

short_url = "https://is.gd/pylink"

long_url = link.expand(short_url)

print(longurl)

# Output : https://github.com/TechUX/buildlink/blob/main/README.md
```


# Supported Domain for link shortening
this package is currently using 5 domains to short link :
These are as follow
 - [Tinyurl](https://tinyurl.com)
 - [is.gd](https://is.gd)
 - [clck.ru](https://clck.ru)
 - [chilp.it](http://chilp.it)
 - [da.gd](https://da.gd)

# Supported Domain for link expanding
Almost all the shorten domains are supported for expansion.
buildlink supports a wide range of URL shortening services, including t.co, goo.gl, bit.ly, amzn.to, tinyurl.com, ow.ly, youtu.be, rg.gy, adf.ly and many others.

# Issues & Pull Requests 

If you find any issue or bug in the package, kindly post it on [Issue page](https://github.com/TechUX/buildlink/issues) .
[Go to Issue page](https://github.com/TechUX/buildlink/issues)

New Ideas and Innovations are always welcomed. [Create a pull request](https://github.com/TechUX/buildlink/compare) if you want to add something new or have a fix of any bug.
<br>[Click here for Pull Request](https://github.com/TechUX/buildlink/pulls)


# About
A simple , lghtweight python package which have ability of shortening and expanding links.<br>
You can shorten a long URL with 5 different services and also expand any shorten URL of internet to its original Long form in a single Click.
<br>Try this package now. [Its available on pypi](https://pypi.org/project/buildlink/).

# Author & License
[![Awesome Badges](https://img.shields.io/badge/Made%20by-Devesh%20Singh-blue.svg)](https://instagram.com/code.radius) <br>
**Author** : Devesh Singh [ [GitHub: @TechUX](https://github.com/TechUX/) | Instagram : [@devesh92744](https://instagram.com/devesh92744) : [@code.radius](https://instagram.com/code.radius) | [Facebook : devesh790](https://www.facebook.com/devesh790)]

**License**
This project is under MIT License. 
<br>[Click Here for detailed License](https://github.com/TechUX/buildlink/blob/main/LICENSE)
