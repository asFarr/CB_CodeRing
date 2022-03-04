"""
The CerealBox toolkit: Code Ring (v1.1) - by leToads : 2/25/22

A script-ready tool for recursive encoding/decoding of
input data provided from stdin or file input.

    Usage: python -m ring {-a, -h, -s} (-r <iterations>) {-e|-d} (-i <inputfile> -o <outputfile>), -t/-b"
    If -r is not specified, iterations defaults to 1.

    Examples:
    ring -a    -   Display the author tag.
    ring -h    -   Display the help dialog.
    ring -s... -   Run tool with output suppressed, for script integration.
    ring -et   -   Process console text input from stdin to encode.
    ring -eb   -   Process console binary input from stdin to encode.
    ring -e -i <infile> -o <outfile> -t   -   Process text file input to encode.
    ring -e -i <infile> -o <outfile> -b   -   Process binary file input to encode.
    ring -dt   -   Process console text input from stdin to decode.
    ring -db   -   Process console binary input from stdin to decode.
    ring -d -i <infile> -o <outfile> -t   -   Process text file input to decode.
    ring -d -i <infile> -o <outfile> -b   -   Process binary file input to decode.

"""

import getopt
import sys

import decoder
import encoder


def author():
    """Print the author ASCII signature."""
    authorart = ["",
                 "                   88         888888888888              "
                 "                 88             d8\'              ",
                 "                   88              88                   "
                 "                 88            d8\'               ",
                 "                   88              88                   "
                 "                 88           \"\"",
                 "                   88   ,adPPYba,  88   ,adPPYba,   ,adP"
                 "PYYba,   ,adPPYb,88  ,adPPYba,",
                 "                   88  a8P_____88  88  a8\"     \"8a  \""
                 "\"     `Y8  a8\"    `Y88  I8[    \"\"",
                 "                   88  8PP\"\"\"\"\"\"\"  88  8b       d"
                 "8  ,adPPPPP88  8b       88   `\"Y8ba,",
                 "                   88  \"8b,   ,aa  88  \"8a,   ,a8\"  8"
                 "8,    ,88  \"8a,   ,d88  aa    ]8I",
                 "                   88   `\"Ybbd8\"'  88   `\"YbbdP\"'   "
                 "`\"8bbdP\"Y8   `\"8bbdP\"Y8  `\"YbbdP\"'",
                 "",
                 "",
                 "",
                 "  ,ad8888ba,                                           "
                 "        88  88888888ba",
                 " d8\"'    `\"8b                                        "
                 "          88  88      \"8b                           ",
                 "d8'                                                    "
                 "        88  88      ,8P                           ",
                 "88              ,adPPYba,  8b,dPPYba,   ,adPPYba,  ,adP"
                 "PYYba,  88  88aaaaaa8P'   ,adPPYba,  8b,     ,d8  ",
                 "88             a8P_____88  88P'   \"Y8  a8P_____88  \""
                 "\"     `Y8  88  88\"\"\"\"\"\"8b,  a8\"     \"8a  `Y8, ,8P'   ",
                 "Y8,            8PP\"\"\"\"\"\"\"  88          8PP\"\"\""
                 "\"\"\"\"  ,adPPPPP88  88  88      `8b  8b       d8    )888(",
                 " Y8a.    .a8P  \"8b,   ,aa  88          \"8b,   ,aa  "
                 "88,    ,88  88  88      a8P  \"8a,   ,a8\"  ,d8\" \"8b,",
                 "  `\"Y8888Y\"'    `\"Ybbd8\"'  88           `\"Ybbd8\""
                 "'  `\"8bbdP\"Y8  88  88888888P\"    `\"YbbdP\"'  8P'     `Y8",
                 "",
                 "",
                 "",
                 "  ,ad8888ba,                         88            "
                 "           88888888ba   88",
                 " d8\"'    `\"8b                        88          "
                 "             88      \"8b  \"\"                            ",
                 "d8'                                  88            "
                 "           88      ,8P                                ",
                 "88              ,adPPYba,    ,adPPYb,88   ,adPPYba,"
                 "           88aaaaaa8P'  88  8b,dPPYba,    ,adPPYb,d8  ",
                 "88             a8\"     \"8a  a8\"    `Y88  a8P____"
                 "_88           88\"\"\"\"88'    88  88P'   `\"8a  a8\"    `Y88  ",
                 "Y8,            8b       d8  8b       88  8PP\"\"\"\""
                 "\"\"\"           88    `8b    88  88       88  8b       88",
                 " Y8a.    .a8P  \"8a,   ,a8\"  \"8a,   ,d88  \"8b,  "
                 " ,aa           88     `8b   88  88       88  \"8a,   ,d88",
                 "  `\"Y8888Y\"'    `\"YbbdP\"'    `\"8bbdP\"Y8   `\""
                 "Ybbd8\"'           88      `8b  88  88       88   `\"YbbdP\"Y8",
                 "                                                   "
                 "                                          aa,    ,88",
                 "                                                   "
                 "                                           \"Y8bbdP\"   "]

    for i in authorart:
        print(i)


def helpme():
    """Print the help and usage dialog."""
    usage = ["The CerealBox toolkit Code Ring (v1.0) - by leToads : 2/25/22\n",
             "A script-ready tool for recursive encoding/decoding of input "
             "data provided from stdin or file input.\n",
             "Usage: python ring.py {-a, -h, -s} (-r <iterations>) {-e|-d} (-i <inputfile> -o <outputfile>), -t/-b",
             "If -r is not specified, iterations defaults to 1. \n",
             "Examples: ",
             "ring.py -h   -   Display the help dialog. ",
             "ring.py -a   -   Display the author tag.  \n",
             "ring.py -s   -   Run tool with output suppressed, for script integration. ",
             "ring.py -et   -   Process console text input from stdin to encode. ",
             "ring.py -eb   -   Process console binary input from stdin to encode. ",
             "ring.py -e -i <infile> -o <outfile> -t   -   Process text file input to encode. ",
             "ring.py -e -i <infile> -o <outfile> -b   -   Process binary file input to encode. \n",
             "ring.py -dt   -   Process console text input from stdin to decode. ",
             "ring.py -db   -   Process console binary input from stdin to decode. ",
             "ring.py -d -i <infile> -o <outfile> -t   -   Process text file input to decode. ",
             "ring.py -d -i <infile> -o <outfile> -b   -   Process binary file input to decode. "]

    for i in usage:
        print(i)

    sys.exit(0)


def main(argv):
    """Main Driver - Parse CLI flags/options and run the related subprogram."""
    if not argv:
        argument_list = ['-a', '-h']
    else:
        argument_list = argv

    options = "abdehti:o:r:s"
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
