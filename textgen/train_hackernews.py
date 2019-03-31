# Example of training a hackernews generator
import os

from textgenrnn import textgenrnn

sample_dir = os.path.join(os.path.curdir, "sample-datasets")
filename = os.path.join(sample_dir, "hacker-news-100.txt")

# ---------- titles ------- #
title_gen = textgenrnn()

title_gen.train_from_file(filename, num_epochs=1)

title_gen.generate()
