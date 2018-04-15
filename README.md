<h1 align="center">
	<img width="400" src="https://xix.ph0x.me/vitelogo.png" alt="Vite">
</h1>

> A simple and mnml static site generator; pronounced as /vit/

[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)

Installation
------------

Clone this repo and:
```console
$ pip3 install -r requirements.txt
```
**NOTE**: Don't delete the cloned repo, since `make.py` is symlinked upon project creation.

Usage
-----

```console
$ ./vite.py new <project-path>
```
Write your Markdown files in the `pages` directory and execute:
```console
$ ./make.py   # in project directory
```
Rendered HTML will be in the `build` directory.

Finally, run:
```console
$ ./make.py serve
```
to serve the contents of the `build` directory.

Configuration
-------------

Not very sophisticated, but basic configuration can be acheived using
  `config.py` found in the project directory.
Example config:

```python
# config.py 
title = ''
author = ''
header = ''
footer = '' 
template = 'index.html'  # default is index.html
```

Templating
----------

Vite uses Jinja2 templating.  
**NOTE**: Stylesheets, images and JS can be accessed from the `static` folder.

A basic example would be:
```html
<title> {{ title }} </title>

<body>
{{ body }}
</body>

<footer>
{{ footer }}
</footer>
```

Directory tree
--------------

    example
    ├── build
    ├── config.py
    ├── make.py -> /home/icyphox/code/vite/make.py
    ├── pages
    ├── static
    └── templates
        └── index.html

TODO
----

- [x] Templating
- [x] CSS support
- [x] Implement a simple HTTP server (*later*)
- [x] Add example site
- [x] Basic config (`config.py`)


## Credits
_Logo credits_: <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>  
_Hue_: [UltimateHackers/hue](https://github.com/UltimateHackers/hue)

