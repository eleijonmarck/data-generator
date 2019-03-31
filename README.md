# Data Generator

TODO:
python dbgenerator - https://github.com/tirthajyoti/pydbgen
- creates dataframes/tables
- can populates different dbs

## Text - parameters
For generating text parameters please refer to the textgen module
Models are residing in `models/textgen`

### Text models
To use the text models we will be using [textgenrnn](https://github.com/minimaxir/textgenrnn).

This uses a RNN and Attention architecture to learn the underlying distribution of the text samples.

## Examples

```bash
$ head sample-datasets/hacker-news-100.txt
title
A Message to Our Customers
Steve Jobs has passed away.
Reflecting on one very, very strange year at Uber
Show HN: This up votes itself
Cloudflare Reverse Proxies Are Dumping Uninitialized Memory
UK votes to leave EU
Tim Cook Speaks Up
Announcing the first SHA-1 collision
2048
```

Training by file
```python
from textgenrnn import textgenrnn

textgen.train_from_file('sample-datasets/hacker-news-100.txt', num_epochs=1)
textgen.generate()
```

### Pretrained models

```bash
$ ls models/textgen
hackernews.hd5
```

Training by file
```python
from textgenrnn import textgenrnn

textgen = textgenrnn('models/textgen/destination_icao.hd5')
textgen.generate()
```


### Numerical Generators (WIP)


### Approach 1
Add noise to the signal where the value is different than zero.
https://stackoverflow.com/questions/14058340/adding-noise-to-a-signal-in-python

## Running the container

We are using `Makefile` to simplify docker commands within make commands.

Build the container and start an iPython shell

    $ make ipython

Build the container and start a bash

    $ make bash

Mount a volume for external data sets

    $ make DATA=~/mydata

Prints all make tasks

    $ make help
