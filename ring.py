# TODO: Module docstring

import getopt
import sys

import decoder
import encoder


def author():
    """Print the author ASCII signature."""
    print("")
    print("                   88         888888888888                               88             d8\'              ")
    print("                   88              88                                    88            d8\'               ")
    print("                   88              88                                    88           \"\"")
    print("                   88   ,adPPYba,  88   ,adPPYba,   ,adPPYYba,   ,adPPYb,88  ,adPPYba,")
    print("                   88  a8P_____88  88  a8\"     \"8a  \"\"     `Y8  a8\"    `Y88  I8[    \"\"")
    print("                   88  8PP\"\"\"\"\"\"\"  88  8b       d8  ,adPPPPP88  8b       88   `\"Y8ba,")
    print("                   88  \"8b,   ,aa  88  \"8a,   ,a8\"  88,    ,88  \"8a,   ,d88  aa    ]8I")
    print("                   88   `\"Ybbd8\"'  88   `\"YbbdP\"'   `\"8bbdP\"Y8   `\"8bbdP\"Y8  `\"YbbdP\"'")
    print("")
    print("")
    print("")
    print("  ,ad8888ba,                                                   88  88888888ba")
    print(" d8\"'    `\"8b                                                  88  88      \"8b                           ")
    print("d8'                                                            88  88      ,8P                           ")
    print("88              ,adPPYba,  8b,dPPYba,   ,adPPYba,  ,adPPYYba,  88  88aaaaaa8P'   ,adPPYba,  8b,     ,d8  ")
    print("88             a8P_____88  88P'   \"Y8  a8P_____88  \"\"     `Y8  88  88\"\"\"\"\"\"8b,  a8\"     \"8a  `Y8, ,8P'   ")
    print("Y8,            8PP\"\"\"\"\"\"\"  88          8PP\"\"\"\"\"\"\"  ,adPPPPP88  88  88      `8b  8b       d8    )888(")
    print(" Y8a.    .a8P  \"8b,   ,aa  88          \"8b,   ,aa  88,    ,88  88  88      a8P  \"8a,   ,a8\"  ,d8\" \"8b,")
    print("  `\"Y8888Y\"'    `\"Ybbd8\"'  88           `\"Ybbd8\"'  `\"8bbdP\"Y8  88  88888888P\"    `\"YbbdP\"'  8P'     `Y8")
    print("")
    print("")
    print("")
    print("  ,ad8888ba,                         88                       88888888ba   88")
    print(" d8\"'    `\"8b                        88                       88      \"8b  \"\"                            ")
    print("d8'                                  88                       88      ,8P                                ")
    print("88              ,adPPYba,    ,adPPYb,88   ,adPPYba,           88aaaaaa8P'  88  8b,dPPYba,    ,adPPYb,d8  ")
    print("88             a8\"     \"8a  a8\"    `Y88  a8P_____88           88\"\"\"\"88'    88  88P'   `\"8a  a8\"    `Y88  ")
    print("Y8,            8b       d8  8b       88  8PP\"\"\"\"\"\"\"           88    `8b    88  88       88  8b       88")
    print(" Y8a.    .a8P  \"8a,   ,a8\"  \"8a,   ,d88  \"8b,   ,aa           88     `8b   88  88       88  \"8a,   ,d88")
    print("  `\"Y8888Y\"'    `\"YbbdP\"'    `\"8bbdP\"Y8   `\"Ybbd8\"'           88      `8b  88  88       88   `\"YbbdP\"Y8")
    print("                                                                                             aa,    ,88")
    print("                                                                                              \"Y8bbdP\"   ")


def helpme():  # TODO: Add flag descriptions
    """Print the help and usage dialog."""
    print("The CerealBox toolkit Code Ring (v1.0) - by leToads : 2/25/22\n")
    print("A script-ready tool for recursive encoding/decoding of input "
          "data provided from stdin or file input. \n")
    print("Usage: python ring.py {-a, -h}, {-e|-d} (-i <inputfile> -o <outputfile>), -t/-b\n\n")

    print("Examples: ")
    print("ring.py -h   -   Display the help dialog. ")
    print("ring.py -a   -   Display the author tag.  \n")
    print("ring.py -et   -   Process console text input from stdin to encode. ")
    print("ring.py -eb   -   Process console binary input from stdin to encode. ")
    print("ring.py -e -i <infile> -o <outfile> -t   -   Process text file input to encode. ")
    print("ring.py -e -i <infile> -o <outfile> -b   -   Process binary file input to encode. \n")
    print("ring.py -dt   -   Process console text input from stdin to decode. ")
    print("ring.py -db   -   Process console binary input from stdin to decode. ")
    print("ring.py -d -i <infile> -o <outfile> -t   -   Process text file input to decode. ")
    print("ring.py -d -i <infile> -o <outfile> -b   -   Process binary file input to decode. ")
    sys.exit(2)


def main(argv):
    """Main Driver - Parse CLI flags/options and run the related subprogram."""
    if not argv:
        argument_list = ['-a', '-h']
    else:
        argument_list = argv

    options = "abdehti:o:"
    try:
        arguments, values = getopt.getopt(argument_list, options)

        for current_argument, current_value in arguments:
            if current_argument == "-a":
                author()

            if current_argument == "-h":
                helpme()

            if current_argument == "-d":
                decoder.main(argv)

            if current_argument == "-e":
                encoder.main(argv)

    except getopt.error as err:
        print(str(err))


if __name__ == '__main__':
    main(sys.argv[1:])
