# given a list of restaurants:rating, print out in alphabetical order
# Restaurant "name" is rated at score

from sys import argv

script, filename = argv

rest_dict = {}

def normalize( filetext ):
    #make a dictionary!!
    filelist = filetext.split("\n")

    for pairs in filelist:
        if ":" in pairs:
            new_data = pairs.split(":")
            rest_dict[new_data[0]] = new_data[1]

def main():
    open_file = open(filename)
    filetext = open_file.read()

    normalize( filetext )

    sorted_names = rest_dict.keys()

    sorted_names.sort()

    for names in sorted_names:
        print "Restaurant '%s' is rated at %s." % (names, rest_dict[names])

main()