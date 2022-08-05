# draw2Svg

*This is fork to drawSvg, in which we try to readjust its coordinate system to follow SVG standard*

A Python 3 library for programmatically generating SVG images (vector drawings) and rendering them or displaying them in a Jupyter notebook.

Most common SVG tags are supported and others can easily be added by writing a small subclass of `DrawableBasicElement` or `DrawableParentElement`.

An interactive [Jupyter notebook](https://jupyter.org) widget, `drawSvg.widgets.DrawingWidget`, is included that can update drawings based on mouse events.

# Install

draw2Svg is available on PyPI:

```
$ pip install draw2Svg
```

## Prerequisites

Cairo needs to be installed separately. When Cairo is installed, drawSvg can output PNG or other image formats in addition to SVG. See platform-specific [instructions for Linux, Windows, and macOS from Cairo](https://www.cairographics.org/download/). Below are some examples for installing Cairo on Linux distributions and macOS.

**Ubuntu**

```
$ sudo apt-get install libcairo2
```

**macOS**

Using [homebrew](https://brew.sh/):

```
$ brew install cairo
```

## Example result
This is sample application of this library to do some generative art exercise [here](https://github.com/mattdesl/workshop-generative-art/blob/master/docs/exercises.md)  

Pie poster:  
![svg](examples/exerc1.svg)

Sol Le Witt styled poster:
![svg](examples/exerc2.svg)

For more detailed manuals, go to our website:
https://draw2svg.netlify.app/
