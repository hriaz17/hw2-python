from unittest import TestCase
from csc583.invertedindex import InvertedIndex
from csc583.document import Document

class Test_hw2_q8(TestCase):
    input_path= "Docs.txt"

    def test_q8_1_1(self):
        query = "schizophrenia /2 drug"
        gold_q811=[Document("Doc1",3,1),Document("Doc2",1,2)]
        ans_q811=InvertedIndex(self.input_path).q8_1_1(query)

        assert type(ans_q811) is not None
        assert type(ans_q811) is list
        assert len(ans_q811) > 0
        assert len(ans_q811) == 2

        for gold,ans in zip(gold_q811,ans_q811):
            gold.__eq__(ans)


    def test_q8_1_2(self):
        query = "schizophrenia /4 drug"
        gold_q812 = [Document("Doc1", 3, 1), Document("Doc2", 1, 2), Document("Doc3", 5, 1)]
        ans_q812 = InvertedIndex(self.input_path).q8_1_2(query)
        assert ans_q812 is not None
        assert type(ans_q812) is list
        assert len(ans_q812) > 0
        assert len(ans_q812) == 3

        for gold, ans in zip(gold_q812, ans_q812):
            gold.__eq__(ans)


    def test_q8_2_directional(self):
        query = "schizophrenia /2 drug"
        gold_q82 = [Document("Doc2", 1, 2)]
        ans_q82 = InvertedIndex(self.input_path).q8_2(query)

        assert ans_q82 is not None
        assert type(ans_q82) is list
        assert len(ans_q82) > 0
        assert len(ans_q82) == 1

        for gold, ans in zip(gold_q82, ans_q82):
            gold.__eq__(ans)


