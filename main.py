# 3 Sept 2023
# Author: Noa Lerch

import sys
import os
import getopt
import Summarizer
import openai

openai.api_key = open("openai_api_key").read() # os.getenv("OPENAI_API_KEY")


def main():
    input_file = ""
    output_file = ""
    print("lol")
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("main.py -i <input_file> -o <output_file>")
        sys.exit(2)
    summarizer = Summarizer.Summarizer()
    # text = open(args[0]).read()
    text = open("darthplagueis.txt").read()
    print(text)
    #summarizer.text_from_file(args[0])
    summarizer.text_from_file("darthplagueis.txt")
    print(summarizer.summarize())


if __name__ == "__main__":
    main()