from csc583.document import Document

class InvertedIndex:

    def __init__(self,input_file):
        # add your code here
        pass

    def read_txt_file(self,input_file):
        # add your code here
        docs=None
        return docs

    def q8_1_1(self, query):
        # add your code here
        # return multiple outputs that have the same docid if and
        # when there are multiple matches per doc.
        ans=None
        return ans

    def q8_1_2(self, query):
        # add your code here
        ans=None
        return ans


    def q8_2(self, query):
        # add your code here
        ans=None
        return ans

def main():
    # adding a main just in case you want to run not from pytest
    query="schizophrenia /2 drug"
    ans=InvertedIndex().q8_1_1(query)


if __name__ == "__main__":
    main()