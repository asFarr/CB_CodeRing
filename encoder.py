"""
The CerealBox toolkit: Code Ring Encoder Module (v1.0) - by leToads : 2/25/22

A script-ready tool for recursive encoding of
input data provided from stdin or file input.

    Usage: python ring.py -e (-i <inputfile> -o <outputfile>), -t/-b
    Examples:
    ring.py -et   -   Process console text input from stdin to encode.
    ring.py -eb   -   Process console binary input from stdin to encode.
    ring.py -e -i <infile> -o <outfile> -t   -   Process text file input to encode.
    ring.py -e -i <infile> -o <outfile> -b   -   Process binary file input to encode.

"""
import getopt
import sys
import time
import base64

rot13 = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM0987654321")


def text_lit():  # TODO: Refine algorithm
    """Text stdin processing and encoding subprogram."""
    print("Text Literals")
    input_text = input('Plaintext: ')
    temp = input_text
    i = 0
    iterations = int(input('Number of iterations: '))
    while i < iterations:
        temp = temp.translate(rot13)
        print("ROT result: " + temp)
        time.sleep(0.5)
        temp = temp.encode('utf-8').hex()
        print("Hex result: " + temp)
        time.sleep(0.5)
        temp = str(base64.b64encode(temp.encode('utf-8')), 'utf-8')
        print("Base64 result: " + temp)
        time.sleep(0.5)
        i += 1


def text_file(infp, outfp):  # TODO: Refine algorithm
    """Text file processing and encoding subprogram."""
    print("Text Files")
    j = 0
    with open(infp, 'r', encoding='utf-8') as infile:
        temp = infile.read()
        iterations = int(input('Number of iterations: '))
        while j < iterations:
            temp = base64.b64encode(bytes(str(temp), 'utf-8'))
            print("Base64 result: " + str(temp))
            time.sleep(0.5)
            temp = bytes.hex(temp).encode('utf-8')
            print("Hex result: " + str(temp))
            time.sleep(0.5)
            temp = bytes(str(temp).translate(rot13), 'utf-8')
            print("ROT result: " + str(temp))
            time.sleep(0.5)
            j += 1
        with open(outfp, 'w', encoding='utf-8') as outfile:
            outfile.write(str(temp))


def bin_lit():  # TODO: Refine algorithm
    """Binary stdin processing and encoding subprogram."""
    print("Binary Literals")
    input_text = input('Plaintext: ')
    temp = input_text
    i = 0
    iterations = int(input('Number of iterations: '))
    while i < iterations:
        temp = temp.translate(rot13)
        print("ROT result: " + temp)
        time.sleep(0.5)
        temp = temp.encode('utf-8').hex()
        print("Hex result: " + temp)
        time.sleep(0.5)
        temp = str(base64.b64encode(temp.encode('utf-8')), 'utf-8')
        print("Base64 result: " + temp)
        time.sleep(0.5)
        i += 1


def bin_file(infp, outfp):  # TODO: Refine algorithm
    """Binary File processing and encoding subprogram."""
    print("Text Files")
    j = 0
    with open(infp, 'r', encoding='utf-8') as infile:
        temp = infile.read()
        iterations = int(input('Number of iterations: '))
        while j < iterations:
            temp = base64.b64encode(bytes(str(temp), 'utf-8'))
            print("Base64 result: " + str(temp))
            time.sleep(0.5)
            temp = bytes.hex(temp).encode('utf-8')
            print("Hex result: " + str(temp))
            time.sleep(0.5)
            temp = bytes(str(temp).translate(rot13), 'utf-8')
            print("ROT result: " + str(temp))
            time.sleep(0.5)
            j += 1
        with open(outfp, 'w', encoding='utf-8') as outfile:
            outfile.write(str(temp))


def main(argv):
    """Main Driver - Parse CLI flags/options and run the related function."""
    if not argv:
        argument_list = ['-a', '-h']
    else:
        argument_list = argv

    options = "abdehti:o:"
    infile = ''
    outfile = ''
    try:
        arguments, values = getopt.getopt(argument_list, options)

        for current_argument, current_value in arguments:
            if current_argument == "-i":
                infile = current_value

            elif current_argument == "-o":
                outfile = current_value

            elif current_argument == "-t":
                if (infile != '') & (outfile != ''):
                    text_file(infile, outfile)
                else:
                    text_lit()

            elif current_argument == "-b":
                if (infile != '') & (outfile != ''):
                    bin_file(infile, outfile)
                else:
                    bin_lit()

    except getopt.error as err:
        print(str(err))


if __name__ == '__main__':
    main(sys.argv[1:])
