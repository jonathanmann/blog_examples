#!/usr/bin/python
def main():
    import sys
    try:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    except:
        print "\nThis program requires an input file and an output file.\n\nExample:\n$./TableCreate.py input.csv output.csv\n"
        sys.exit(0)

    DataToTable(in_file,out_file)

class DataToTable(object):
    """
    Reads in a csv file populated headers and data and outputs a separate file containing a table of the input data.   
    """
    def __init__(self,in_file,out_file):
        """
        Initialize data reshaping class

        Args:
            in_file (string): the name of csv file containing the original data to be reshaped
            out_file (string): the name of output file where the reshaped data will be exported
        """
        self.in_file = in_file
        self.out_file = out_file
        self.data = self.get_file_data()
        self.tabbing = {'table':0,'thead':1,'tbody':1,'tr':2,'th':3,'td':3}
        self.table = self.build_table()
        self.write_table()

    def build_table(self):
        """
        Build a table by wrapping the each aspect of the CSV file with the appropriate XML style tags
        
        Returns:
          string: an XML style table containing the data from the CSV file 
        """
        headers = self.wrap('thead',self.wrap('tr',[self.wrap('th',x) for x in self.data[0]]))
        body = self.wrap('tbody',[self.wrap('tr',[self.wrap('td',z) for z in x]) for x in self.data[1:]])
        return self.wrap('table',[headers,body])

    def get_file_data(self):
        """
        Read data from the input csv file

        Returns:
            data from the input csv file as a list of lists where each sublist is a line from the input file
        """
        import csv
        with open(self.in_file) as csv_data:
            file_data = []
            for line in csv.reader(csv_data):
                file_data.append(line)
            return file_data   

    def write_table(self):
        """
        Write the table to output file
        """
        o = open(self.out_file, 'w')
        o.write(self.table)

    def wrap(self,tag,data):
        """
        Surround input data with XML tags

        Args:
            tag (string): the tag to surround the data with
            data (string): the data to be surrounded by the tag

        Returns:
            string : the tag wrapped data
        """
        data = ''.join(data)
        indent1 = self.tabbing[tag] * ["  "]
        indent2 = indent1
        splitter = "\n"
        if self.tabbing[tag] == 3:
            splitter = ""
            indent2 = [""]
        else:
            data = data[:-1]
        return ''.join(indent1 +  ["<",tag,">",splitter,data,splitter] + indent2  + ["</",tag, ">\n"])

if __name__ == '__main__':
    main()
