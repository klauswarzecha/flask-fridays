# Day 1

## Install flask
John Elder suggested to create a virtual environment using 

`python -m venv virt`, activate it and install `flask` there with `pip install flask`.

I always liked to use [conda](https://docs.conda.io/en/latest/), and I still do.    
Nevertheless I have recently switched to [mamba](https://github.com/mamba-org/mamba). You might want to have a look at the [mamba documentation](https://mamba.readthedocs.io/en/latest/index.html) and read this article about [Open Software Packaging for Science](https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23) on Medium.

So, for me it was 

```mamba create --name flask python=3.11 flask ipython```

## Minimal example

John outlined a minimal example that does **not** contain a an `app.run()` command, but is started from the terminal via 

    1. export FLASK_ENV=development
    2. export FLASK_APP=hello.py
    3. flask run

With the current version of flask (2.2.2) this still works, but when you do, there is a warning 

```'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.```


## A dynamic URL - Pass an argument to a website

When an argument in pointed brackets is part of the route, as in 

```python
@app.route('/user/<name>')
```

it can be passed to the corresponding function 

```python
def user(name):
```

## Render a first template

Flask looks for HTML templates in the `templates` directory. These templates can be returned using the `render_template` method.