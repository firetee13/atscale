#!/usr/bin/env python3
from argparse import ArgumentParser

class Or_matcher:

    def __init__(self, file_name, criteria_list):
        self.f = open("text", "r")
        self.criteria_list = criteria_list
        self.output_list = []

    def match_words(self, word, line_number, word_list):
        """
        get the line number of a particular word
        """
        if word in word_list:
            return line_number

    def iterate_over_the_lists(self):
        """
        iterate over the lines, enumerate, and match if we have positive integer
        """
        for line_number, line in enumerate(self.f):
            for item in self.criteria_list:
                count = (self.match_words(item, line_number, line))
                if isinstance(count, int):
                    self.output_list.append(count)
        return(self.output_list)

    def print_Or(self):
        """
        print Or
        """
        print(
            f"The words {self.criteria_list} occur in rows {set(self.output_list)}")


class And_matcher(Or_matcher):
    def __init__(self, file_name, criteria_list, and_output_list_matched=[]):
        super().__init__(file_name, criteria_list)
        self.and_output_list_matched = []

    def matching_AND(self):
        """
        for the AND clause we compare the lenght of the list to the
        count of occurrences. If they match we have to extract the key from the dict.
        """
        Or_matcher.iterate_over_the_lists(self)
        and_dict = {i: self.output_list.count(i) for i in self.output_list}
        for k, v in and_dict.items():
            if len(self.criteria_list) == v:
                self.and_output_list_matched.append(k)

    def print_And(self):
        """
        print And
        """
        print(
            f"The words {self.criteria_list} together occur in rows {set(self.and_output_list_matched)}")


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--file', metavar='FILE', help='file to read')
    args = parser.parse_args()

    # ==============OR==================
    first_OR_list = ["Care", "Quality", "Comission"]
    second_OR_list = ["September", "2004"]
    third_OR_list = ["general", "population", "generally"]
    # ==============AND==================
    first_AND_list = ["Care", "Quality", "Commission", "admission"]
    second_AND_list = ["general", "population", "Alzheimer"]

    # ==============Object Init==========
    frist_criteria = Or_matcher(args.file, first_OR_list)
    second_criteria = Or_matcher(args.file, second_OR_list)
    third_criteria = Or_matcher(args.file, third_OR_list)
    fourth_criteria = And_matcher(args.file, first_AND_list)
    fifth_criteria = And_matcher(args.file, second_AND_list)

    # ===============OR manipulation-====
    frist_criteria.iterate_over_the_lists()
    frist_criteria.print_Or()

    second_criteria.iterate_over_the_lists()
    second_criteria.print_Or()

    third_criteria.iterate_over_the_lists()
    third_criteria.print_Or()

    # ===============AND manipulation====
    fourth_criteria.matching_AND()
    fourth_criteria.print_And()

    fifth_criteria.matching_AND()
    fifth_criteria.print_And()
