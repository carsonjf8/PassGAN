Descriptions of files included in source code sub directory
subsetter.py
	Reads in a file containing a large sample of generated outputs of passwords and splits them into differently sized subsets from 10^4 to 10^9.  Each subset is written to a different file.
	Can be run by "python subsetter.py"
uniquer.py
	Reads in each of the subset files created by subsetter.py and converts them to sets to remove any duplicates. These unique values are then saved to new files.
	Can be run by "python uniquer.py"
matcher.py
	Reads in each of the unique password files created by uniquer.py as well as the testing set file. For each subset of generated outputs, it calculates the number of matches with the test set and prints that to the console.
	Can be run by "python matcher.py"
passgan-train.ipynb
	Jupyter Notebook to define the PassGAN models, read in the training data, and then run the training iterations. Checkpoints are saved throughout the training so that earlier versions can be reloaded later for ease of running experiments at different iteration values.
	Can be run through a Jupyter Notebook program
create_train_and_test.ipynb
	A notebook which creates a train and test set for the rock you dataset (must read in original RockYou dataset from Kaggle).
testing.ipynb
	A notebook that will train the PassGAN for 200,000 iterations and generate 10^8 passwords every 10,000 iterations starting at 5,000. (this takes a very long time and alot of resources)
