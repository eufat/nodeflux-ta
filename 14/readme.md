For this question I will take my small project last year I've work on as an example. The project is to classify either a person name is male or female.

1.  This is the baseline of the project, we must find a the area of project we will solve so our work can be focused and effective. From the project above, the problem is how to classify gender based on a given name stricted to Indonesian.

2.  This is where we mine data from sources, make sure one datasets have variation from the other. In this project I got relatively small data (4000 names), from try-out database held in Jabodetabek.

3.  Data preprocessing is when we need prepare our data to be train on a model. Usually we consider the format of the data (for example: in image data we need to know what extension is .jpg, .gif or .png and convert it when needed). Another thing to do is to clean-up from data outliers which will ruin our training process. In the project, the name of Balinese (like "I Made" or "I Ketut" for example) is removed.

4.  Model development is step where we choose our model to fit our data, we could choose by how our data is distributed what is the dimension of our data, how much the data we have etc. For example in the project case, I use Naive Bayes Classifier.

5.  Model Improvement is where we tune our model to get the best accuracy. In the project case, I search for features (which letter is contribute the most, which combination of letter is determine whether the name is male or female), number of test, dev and train data etc.
