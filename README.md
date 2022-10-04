_nordplotlib_: Nord meets Matplotlib
====================================

 + [Available variants](#art-available-variants)
 + [Building and installing](#nut_and_bolt-building-and-installing)
 + [Credits and dependencies](#gem-credits-and-dependencies)

# :art: Available variants

## PNG variant for screen viewing

```python
from nordplotlib.png import install; install()
```

![PNG variant sample](/assets/demo_png.svg)

## PDF variant for print viewing

```python
from nordplotlib.pdf import install; install()
```

![PDF variant sample](/assets/demo_pdf.svg)

# :nut_and_bolt: Building and installing

To build and install this package with `pip`, the same procedure can be
followed as for most pure Python packages that use `setuptools`.

## Building a wheel

The Python `build` package will create a wheel and source distribution;
without additional options, both files are created in the `dist/` subdirectory,
which will be created if it does not already exist.

```sh
python3 -m build
```

## Installing from local files

Some optional flags are given below in brackets that can be
useful for a non-root build (`--user`) or for active development
(`--ignore-installed --force-reinstall`), but these are not strictly
necessary to install the package itself. The following command works
from the repository root directory.

```sh
pip3 install [--user] [--ignore-installed --force-reinstall] $PWD
```

## Installing from GitHub

Installing from GitHub directly is even easier!

```sh
pip3 install [--user] [--ignore-installed --force-reinstall] git+https://github.com/emprice/nordplotlib
```

# :gem: Credits and dependencies

 + [Matplotlib](https://matplotlib.org) is probably the most popular
   way to generate scientific plots in Python.
 + The [Nord](https://www.nordtheme.com) colorscheme is a beautiful set
   of color palettes with a frosty blue feel. Many ports are available if
   you like these colors and want to see them in your own tools.

<!-- vim: set ft=markdown: -->
