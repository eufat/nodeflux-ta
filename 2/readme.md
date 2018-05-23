1.  Split the data with 8:1:1 proportion of train, dev, and test dataset. Do not combine the groups, take randomly.
2.  I would use convnet, since it is hard to extract feature from unstructured data like images. Specifically VGG-16 since it is widely adopted and the accuracy relatively good.
3.  Usually is the variation of the data is not distributed well enough. Get more data, find better classifier and optimze the hyperparameters.
