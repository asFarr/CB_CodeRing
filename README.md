# The CerealBox toolkit: Code Ring (v1.1) - by asFarr
CLI tool for encoding and decoding of messages from stdin or file input. 



Syntax: python ring.py {-a, -h, -s} (-r <iterations>) {-e|-d} (-i <inputfile> -o <outputfile>), -t/-b"
    
If -r is not specified, iterations defaults to 1.




    Examples:
        ring.py -a    -   Display the author tag.
        ring.py -h    -   Display the help dialog.
        ring.py -s... -   Run tool with output suppressed, for script integration.
        ring.py -et   -   Process console text input from stdin to encode.
        ring.py -eb   -   Process console binary input from stdin to encode.
        ring.py -e -i <infile> -o <outfile> -t   -   Process text file input to encode.
        ring.py -e -i <infile> -o <outfile> -b   -   Process binary file input to encode.
        ring.py -dt   -   Process console text input from stdin to decode.
        ring.py -db   -   Process console binary input from stdin to decode.
        ring.py -d -i <infile> -o <outfile> -t   -   Process text file input to decode.
        ring.py -d -i <infile> -o <outfile> -b   -   Process binary file input to decode.
