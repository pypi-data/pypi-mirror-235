# Open BOBJ

Simple Python Package to open `.obj` files in Blender.

## Install

You can simply install it using

```
pip install open-bobj
```

or if you have `pipx` use

```
pipx install open-bobj
```

## Usage

To open any number of `.obj` files in the terminal, run

```
open-bobj /path/to/file.obj
```

You can also open multiple at ones. This is going to open all
of the `.obj` objects in the same blender instance.

```
open-bobj /path/to/file.obj /another/file.obj /and/another/one.obj
```

There is also a short handle

```
bobj /path/to/file.obj
```
