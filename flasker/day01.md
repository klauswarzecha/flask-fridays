# Day 1

## Install flask
John Elder suggested to create a virtual environment using 

`python -m venv virt`, activate it and install `flask` there with `pip install flask`.

I always liked to use [conda](https://docs.conda.io/en/latest/), and I still do.    
Nevertheless I have recently switched to [mamba](https://github.com/mamba-org/mamba). You might want to have a look at the [mamba documentation](https://mamba.readthedocs.io/en/latest/index.html) and read this article about [Open Software Packaging for Science](https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23) on Medium.

So, for me it was 

```mamba create --name flask python=3.11 flask ipython```

