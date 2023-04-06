#!/usr/bin/env python3

import os

def printRed(str): print("\033[91m {}\033[00m" .format(str))

def printGreen(str): print("\033[92m {}\033[00m" .format(str))

def printYellow(str): print("\033[93m {}\033[00m" .format(str))

def printLightPurple(str): print("\033[94m {}\033[00m" .format(str))

def printPurple(str): print("\033[95m {}\033[00m" .format(str))

def printCyan(str): print("\033[96m {}\033[00m" .format(str))

def printLightGray(str): print("\033[97m {}\033[00m" .format(str))

def printBlack(str): print("\033[98m {}\033[00m" .format(str))

printRed("Red")
printGreen("Green")
printCyan("Cyan")

def print_format_table():
    """
    Prints table of formatted text format options using ANSI escape sequences
    """

    # \x1b is ESC
    # ESC[1;34;{...}m -> Set graphics modes for cell, separated by semicolon (;).
    # ESC[0m -> reset all modes (styles and colors)
    # more info @ https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()

