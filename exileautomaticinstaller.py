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
if not (sys.version_info.major == 3 and sys.version_info.minor < 8):
    print(colorama.Fore.RED+"Этот скрипт требует Python 3.7 или ниже!")
    print(colorama.Fore.White+"Вы используете Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)
outfile = open(input("Путь к шаблону генерации (см. https://github.com/exile-dreams/exiletools Wiki для подробностей): "))
outfile = outfile.read()