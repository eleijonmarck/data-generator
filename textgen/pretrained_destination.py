# Example of serving a pretrained textmodel generator
import os

from textgenrnn import textgenrnn

model_dir = os.path.join(os.path.curdir, 'models')
weights = os.path.join(model_dir, 'destination.hd5')

#---------- destinations ------- #
destination_gen = textgenrnn(weights)

destination_gen.generate(10)
