"""
The CerealBox toolkit: Code Ring Decoder Module (v1.1) - by asFarr : 2/25/22

A script-ready tool for recursive encoding/decoding of
input data provided from stdin or file input.

    Usage: python -m ring -s (-r <iterations>) -d (-i <inputfile> -o <outputfile>), -t/-b
    If -r is not specified, iterations defaults to 1.

    Examples:
    ring -s... -   Run tool with output suppressed, for script integration.
    ring -dt   -   Process console text input from stdin to decode.
    ring -db   -   Process console binary input from stdin to decode.
    ring -d -i <infile> -o <outfile> -t   -   Process text file input to decode.
    ring -d -i <infile> -o <outfile> -b   -   Process binary file input to decode.

"""

import getopt
import sys
import time
import base64

rot13 = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM0987654321")


def text_lit(is_silent, iterate):
    """Text stdin processing and encoding subprogram."""
    if is_silent:
        input_text = input('Plaintext: ')
        temp = input_text
        i = 0
        while i < iterate:
            temp = bytes.fromhex(temp)
            temp = temp.translate(rot13)
            temp = base64.b64decode(temp[2:-1])
            i += 1
        print(temp)
    else:
        print("Text Literals")
        input_text = input('Plaintext: ')
        temp = input_text
        i = 0
        while i < iterate:
            temp = bytes.fromhex(temp)
            print(str(temp)[4:-2])
            temp = temp.translate(rot13)
            print(str(temp)[4:-2])
            temp = base64.b64decode(temp[2:-1])
            temp = str(temp)[2:-1]
            print(temp)
            i += 1


def text_file(is_silent, infp, outfp, iterate):
    """Text file processing and encoding subprogram."""
    if is_silent:
        j = 0
        with open(infp, 'r', encoding='utf-8') as infile:
            temp = infile.read()
            while j < iterate:
                temp = bytes.fromhex(temp)
                temp = temp.translate(rot13)
                temp = base64.b64decode(temp[2:-1])
                j += 1
            with open(outfp, 'w', encoding='utf-8') as outfile:
                outfile.write(str(temp))
    else:
        print("Text Files")
        j = 0
        with open(infp, 'r', encoding='utf-8') as infile:
            temp = infile.read()
            while j < iterate:
                temp = bytes.fromhex(temp)
                print("Hex result: " + str(temp))
                temp = temp.translate(rot13)
                print("ROT result: " + str(temp))
                temp = base64.b64decode(temp[2:-1])
                temp = str(temp)[2:-1]
                print("Base64 result: " + temp)
                j += 1
            with open(outfp, 'w', encoding='utf-8') as outfile:
                outfile.write(str(temp))


def bin_lit(is_silent, iterate):
    """Binary stdin processing and encoding subprogram."""
    if is_silent:
        input_text = input('Plaintext: ')
        temp = input_text
        i = 0
        while i < iterate:
            temp = bytes.fromhex(temp)
            temp = temp.translate(rot13)
            temp = base64.b64decode(temp)
            i += 1
        print(temp)
    else:
        print("Binary Literals")
        input_text = input('Plaintext: ')
        temp = input_text
        i = 0
        while i < iterate:
            temp = bytes.fromhex(temp)
            print(str(temp)[2:-1])
            temp = temp.translate(rot13)
            print(str(temp)[2:-1])
            temp = base64.b64decode(temp)
            print(str(temp)[2:-1])
            i += 1


def bin_file(is_silent, infp, outfp, iterate):
    """Binary File processing and encoding subprogram."""
    if is_silent:
        j = 0
        with open(infp, 'rb') as infile:
            temp = infile.read()
            while j < iterate:
                temp = bytes.fromhex(str(temp.decode('utf-8')))
                temp = temp.translate(rot13)
                temp = base64.b64decode(temp)
                j += 1
            with open(outfp, 'wb') as outfile:
                outfile.write(temp)
    else:
        print("Binary Files")
        j = 0
        with open(infp, 'rb') as infile:
            temp = infile.read()
            while j < iterate:
                temp = bytes.fromhex(str(temp.decode('utf-8')))
                print("Hex result: " + str(temp)[2:-1])
                temp = temp.translate(rot13)
                print("ROT result: " + str(temp)[2:-1])
                temp = base64.b64decode(temp)
                print("Base64 result: " + str(temp)[2:-1])
                j += 1
            with open(outfp, 'wb') as outfile:
                outfile.write(temp)


def main(argv):
    iterations = 1
    is_silent = False
    """Main Driver - Parse CLI flags/options and run the related function."""
    if not argv:
        argument_list = ['-a', '-h']
    else:
        argument_list = argv

    options = "sr:abdehti:o:"
    infile = ''
    outfile = ''
    try:
        arguments, values = getopt.getopt(argument_list, options)

        for current_argument, current_value in arguments:
            if current_argument == "-s":
                is_silent = True

            if current_argument == "-r":
                iterations = int(current_value)

            if current_argument == "-i":
                infile = current_value

            elif current_argument == "-o":
                outfile = current_value

            elif current_argument == "-t":
                if (infile != '') & (outfile != ''):
                    text_file(is_silent, infile, outfile, iterations)
                else:
                    text_lit(is_silent, iterations)

            elif current_argument == "-b":
                if (infile != '') & (outfile != ''):
                    bin_file(is_silent, infile, outfile, iterations)
                else:
                    bin_lit(is_silent, iterations)

    except getopt.error as err:
        print(str(err))


if __name__ == '__main__':
    main(sys.argv[1:])
