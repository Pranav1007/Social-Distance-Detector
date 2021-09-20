#!/usr/bin/python3

from utilities.helper import video, image, webcam
import mimetypes
from os import path
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--media", help="Media Type (image(or i), video(or v), webcam(or w))")
    parser.add_argument("-p", "--path", help="Path of the Media File (For webcam enter space)")

    args = parser.parse_args()
    s = args.media
    p = args.path

    if p is None or s is None:
        print('usage: run.py [-h] [-m MEDIA] [-p PATH]')
        sys.exit(2)

    s = str(s).lower()
    p = str(p)

    if s == "i" or s == "image":
        if(path.exists(p)):
            if mimetypes.guess_type(p)[0].startswith('image'):
                print("Hit 'q' to exit")
                image(p)
            else:
                print("Entered Path is correct but invalid media type. Please Try Again.")
                sys.exit(2)
        else:
            print("Entered Path is invalid. Please Try Again")
            sys.exit(2)

    elif s == "v" or s == "video":
        if(path.exists(p)):
            if mimetypes.guess_type(p)[0].startswith('video'):
                print("Hit 'q' to exit")
                video(p)
            else:
                print("Entered Path is correct but invalid media type. Please Try Again.")
                sys.exit(2)
        else:
            print("Entered Path is invalid. Please Try Again")
            sys.exit(2)

    elif s == "w" or s == "webcam":
        print("Hit 'q' to exit")
        webcam()

    else:
        print("Invalid Media Type. Allowed Types: image, video, webcam")
        sys.exit(2)


if __name__ == '__main__':
    main()
