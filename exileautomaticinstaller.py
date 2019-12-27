#Exile Auto Install
import colorama
import argparse
import sys
colorama.init()

def defaultParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=argparse.FileType())
    parser.add_argument("--zip")
    return parser
parser = defaultParser()
argsnamespace = parser.parse_args(sys.argv)
print(colorama.Fore.BLUE+"Exile Automatic Installer"+colorama.Fore.WHITE)
print("by Kraskaska & IJlyxa")
outfile = open(input("Путь к шаблону генерации (см. https://github.com/exile-dreams/exiletools Wiki для подробностей)"))