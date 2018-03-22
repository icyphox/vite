<h1 align="center">
	<img width="400" src="https://xix.ph0x.me/vitelogo.png" alt="Vite">
</h1>

> A simple and mnml static site generator; pronounced as /vit/

Usage
-----

```console
$ vite.py new <project-path>
```

Write your Markdown files in the `pages` directory and execute

```console
$ vite.py build <project-path>
```

Rendered HTML will be in the `build` directory.

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
```

Templating
----------

Vite uses Jinja2 templating. A basic example would be:

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
    │   └── test_page1
    │       └── index.html
    ├── config.py
    ├── make.py -> /home/icyphox/code/vite/make.py
    ├── pages
    │   └── test_page1.md
    └── templates
        └── index.html

TODO
----

- [x] Templating
- [ ] CSS support
- [ ] Implement a simple HTTP server (*later*)
- [x] Add example site
- [x] Basic config (`config.py`)


## Credits
_Logo credits_: <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>  
_Hue_: [UltimateHackers/hue](https://github.com/UltimateHackers/hue)

