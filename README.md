# vite
> A simple and mnml static site generator that Just Works™

[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)

<h1 align="center">
    <img width="750" src="https://0x0.st/swPG.png" alt="Vite demo">
</h1>

Installation
------------

```console
$ pip install vite
```
Usage
-----

```console
$ vite init path/to/project
$ vite new blog/some-post.md   # `pages/` is implied
```
This creates `pages/blog/some-post.md`.

And then:
```console
$ vite build   # in project directory
```
Rendered HTML will be in the `build` directory.

Finally, run:
```console
$ vite serve  # also in the project directory
```

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
template = 'index.html'  # default is templates/index.html
```

Templating
----------

Vite uses Jinja2 templating, so template files must be placed in a separate `templates/` directory.  
A basic example would be:
```html
<link rel="stylesheet" href="/static/sakura-earthy.css">

<title> {{ title }} </title>

<body>
{{ body }}
</body>

<footer>
{{ footer }}
</footer>
```
### Specifying per-page templates
Vite allows for specifying a unique template, per page. This is acheived by including YAML frontmatter at the top of the Markdown file, like so:

```markdown
---
template: foo.html
title: Some fancy buzzwords here
subtitle: Cool catch phrase here
date: 1 April, 2019
---

## markdown here
...
```

### Notes on templating

- Stylesheets, images and JS can be accessed from the `static` folder.
- `index.html`, i.e. your website's homepage, should be `_index.md` in the `pages/` directory.


Directory tree
--------------

    example
    ├── build
    ├── config.py
    ├── pages
    │   └── test.md
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
- [x] Parsing frontmatter (JSON, YAML, TOML) for per-page options
- [x] Better support for home page (main `index.html` page)
- [x] More powerful frontmatter (title, date, draft status, etc.) (draft status is incomplete)
- [ ] ~Deeper directories under `pages/` (supports only one level now, breaks otherwise)~ (not happening)
- [ ] ~Tagging system~ (not happening)

