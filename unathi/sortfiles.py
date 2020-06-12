import argparse
import os
import csv
from operator import itemgetter


class Footwear:
    def sort_products(self, input_list):
        by_products = sorted(input_list, key=lambda i: i[2], reverse=False)
        return by_products

    def sort_color(self, input_list):
        by_color = sorted(input_list, key=lambda i: i[0][1])
        return sorted(by_color, key=lambda i: i[2], reverse=False)

    def sort_amount(self, input_list):
        by_amount_desc = sorted(input_list, key=lambda i: i[0][1])
        return sorted(by_amount_desc, key=lambda i: i[2], reverse=True)

    def enumerate_lists(self, input_list):
        for i in self.sort_products(input_list):
            print(list(enumerate(i)))
        print("---------")
        for i in self.sort_color(input_list):
            print(list(enumerate(i)))
        print("---------")
        for i in self.sort_amount(input_list):
            print(list(enumerate(i)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    my_product_list = csv.reader(args.file)
    next(my_product_list)
    my_list = list(my_product_list)
    f = Footwear()
    f.enumerate_lists(my_product_list)