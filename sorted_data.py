# given a list of restaurants:rating, print out in alphabetical order
# Restaurant "name" is rated at score

from sys import argv

script, filename = argv

rest_dict = {}

def main():
    f = open(filename)

    for line in f:
        if ":" in line:
            new_data = line.split(":")
            # if scores are not integers, would have to strip out newline.
            rest_dict[new_data[0]] = int(new_data[1])

    sorted_names = rest_dict.keys()

    sorted_names.sort()

    for names in sorted_names:
        print "Restaurant '%s' is rated at %s." % (names, rest_dict[names])

main()