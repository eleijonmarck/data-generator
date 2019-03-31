# Example of training a destination generator
import os

from textgenrnn import textgenrnn

sample_dir = os.path.join(os.path.curdir, 'sample-datasets')
filename = os.path.join(sample_dir, 'destination_icao.csv')

#---------- destinations ------- #
destination_gen = textgenrnn()

destination_gen.train_from_file(filename, num_epochs=1)

destination_gen.generate()
