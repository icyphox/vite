.. raw:: html

   <h1 align="center">

::

    <img width="400" src="https://xix.ph0x.me/vitelogo.png" alt="Vite">

.. raw:: html

   </h1>

    A simple and mnml static site generator; pronounced as /vit/

Usage
-----

.. code:: console

    $ vite.py new <project-path>

Write your Markdown files in the ``pages`` directory and execute

.. code:: console

    $ vite.py build <project-path>

**OR**

.. code:: console

    $ make.py  # at the project directory

Rendered HTML will be in the ``build`` directory.

Configuration
-------------

Not very sophisticated, but basic configuration can be acheived using
``config.py`` found in the project directory. Example config:

.. code:: python

    # config.py 
    title = ''
    author = ''
    header = ''
    footer = '' 

Templating
----------

Vite uses Jinja2 templating. A basic example would be:

.. code:: html

    <title> {{ title }} </title>

    <body>
    {{ body }}
    </body>

    <footer>
    {{ footer }}
    </footer>

Directory tree
--------------

::

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

-  [x] Templating
-  [ ] CSS support
-  [ ] Implement a simple HTTP server (*later*)
-  [x] Add example site
-  [x] Basic config (``config.py``)

Credits
-------

*Logo credits*: Freepik from www.flaticon.com is licensed by CC 3.0 BY
