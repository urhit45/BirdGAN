# BirdGAN
A generative adversarial network for creation of new bird images from existing Kaggle Dataset

# Dataset:
The dataset used for the implemenntation was the Kaggle's 225 Bird Species Dataset, of which I used only 1000 random images, for obvious computation reasons. As the name of the dataset suggests, it contains 225 Birds each of which has 150 images on an average.

# Motivation
The Motivation for this project was provided by moxiegushi, He has performed a similar implementation for Pokemons, which in my opinion is much cooler than birds.

# Using the Repo
 1. Download the dataset from the it's Kaggle page [here](https://www.kaggle.com/gpiosenka/100-bird-species)
 2. Clone the repo and change the source and destination variables in each file to suit your purpose
 3. Run the dataset_creation.py first
 4. Next run the resize_images.py file followed by RGB2RGB file
 5. finally run the Train_test.py file
 
Finally, as with all ML problems I would strongly recommended using a GPU to train. During this implementation I only took a subset of the dataset and it took 7 hours on a Collab notebook ( GPU runtime )
The best solution would be to use a EC2 p2.xlarge instance for the training over the entire dataset

Good luck!!!
Any feedback is appreciated
