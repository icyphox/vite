# Vite
A simple and mnml static site generator.

## Usage
```console
$ vite.py new <project-path>
```
Write your Markdown files in `pages/` and  
```console
$ vite.py build <project-path>
```

*OR*

```console
$ make.py  # at the project directory
```
Rendered HTML will be in `build/`

## Templating
Vite uses Jinja2 templating. A basic example would be: 
```html
<title>{{ title }}</title>

<body>
	{{ body }}
</body>

<footer>
	{{ footer }}
</footer>
```

## TODO

- [x] Templating
- [ ] CSS support
- [ ] Implement a simple HTTP server (_later_)
- [x] Add example site
- [ ]Basic config (`config.py`)
