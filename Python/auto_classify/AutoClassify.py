#!/usr/bin/python

class AutoClassify:
    def __init__(self,data_file,model_type):
        """
        Generates a prediction model from a CSV file using the final column for the labels

        Args:
            data_file (string): the name of the data file to be imported
            model_type (string): the type of machine learning algorithm to use
        """
        self.prep_data(data_file)
        self.prep_model(model_type)
        self.run_model()

    def fn_time(self,text,fn,*args):
        """
        Adds timing to a process

        Args:
            text (string): the label for the timing output
            fn (function): the input function to be wrapped in the timer

        Returns:
            the return value of the input function fn
        """
        from time import time
        t0 = time()
        r = fn(*args)
        print(text + ' : ' + str(round(time()-t0, 3)) + "s")
        return r

    def prep_data(self,data_file):
        """
        Prepare the data for modeling by splitting it into a training set and a test set

        Args:
            data_file (string): the name of the file to be parsed
        """
        import numpy as np
        dataset = np.genfromtxt(data_file, delimiter=",")
        rows,cols = dataset.shape
        t_len = rows/2
        self.features = dataset[:,0:(cols-1)]
        self.labels = dataset[:,(cols-1)]
        self.features_train = self.features[:t_len]
        self.labels_train = self.labels[:t_len]
        self.features_test = self.features[t_len:]
        self.labels_test = self.labels[t_len:]

    def prep_model(self,model_type):
        """
        Prepare the appropriate model according to the user input

        Args:
            model_type (string): an abbreviated model selection name
        """
        if model_type == 'logistic_regression':
            print("Using Logistic Regression")
            from sklearn.linear_model import LogisticRegression
            self.clf = LogisticRegression()

        elif model_type == 'lars':
            print ("Using LARS")
            from sklearn.linear_model import LassoLars
            self.clf = LassoLars()
 
        else:
            print("Using Naive Bayes")
            from sklearn.naive_bayes import GaussianNB
            self.clf = GaussianNB()

    def run_model(self):
        """
        Run the model according to the inputs and display the accuracy
        """
        self.fn_time("training time ",self.clf.fit,self.features_train, self.labels_train)
        self.pred = self.fn_time("testing time  ",self.clf.predict,self.features_test)
        from sklearn.metrics import accuracy_score
        print(accuracy_score(self.labels_test, self.pred))

def main():
    import sys
    try:
        data_file = sys.argv[1]
        model_type = sys.argv[2]
    except:
        print "\nThis program requires an input file and a model.\n\nExample:\n$./AutoClassify.py sample_data.csv logistic_regression\n"
        sys.exit(0)

    AutoClassify(data_file,model_type)

if __name__ == '__main__':
    main()
