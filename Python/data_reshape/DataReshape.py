#!/usr/bin/python

def main():
    import sys
    try:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    except:
        print "\nThis program requires an input file and an output file.\n\nExample:\n$./DataReshape.py input.csv output.csv\n"
        sys.exit(0)
    DataReshape(in_file,out_file)

class DataReshape:
    """
    Data Reshaping Tools

    Reads in a csv populated with two columns, a label column and a data column 
    and outputs a csv with only a single label for each data type and as many 
    data columns as needed.
    """
    def __init__(self,in_file,out_file):
        """
        Initialize data reshaping class

        @param in_file : the csv file containing the original data to be reshaped
        @param out_file : the output file where the reshaped data will be exported
        """
        self.in_file = in_file
        self.out_file = out_file
        self.data = self.get_file_data()
        self.dct = self.make_dict()
        self.create_csv() 

    def make_dict(self):
        """
        Make a dictionary from the imported data

        @ return : a dictionary where the key is a label pointing to a list populated with the label's data 
        """
        d = {}
        for line in self.data:
            if line[0] not in d:
                d[line[0]] = [line[1]] 
            else:
                d[line[0]].append(line[1])
        return d

    def get_file_data(self):
        """
        Read in data from the input csv file

        @ return : data from the input csv file as a list of lists where each sublist is a line from the input file
        """
        import csv
        with open(self.in_file) as csv_data:
            file_data = []
            for line in csv.reader(csv_data):
                file_data.append(line)
            return file_data

    def create_csv(self):
        """
        Write reshaped data to output csv file
        """
        o = open(self.out_file, 'w')
        for k in self.dct:
            o.write(','.join([k] + self.dct[k]) + '\n')
        print "reshaped data written to " + self.out_file

if __name__ == '__main__':
    main()
