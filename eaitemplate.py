####
#Generated by Exile Automatic Installer
####
import sys
import argparse
import colorama
colorama.init()
def defaultParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=argparse.FileType())
    parser.add_argument("--silent", "-s", action='store_const', const=True, default=False)
    parser.add_argument("--debuglevel", choices=['Info', 'Error', 'Warn', 'Debug'], default='Error')

    return parser

parser = defaultParser()
argsnamespace = parser.parse_args(sys.argv)
print(colorama.Fore.BLUE+"Exile Automatic Installer Framework v.0.1"+colorama.Fore.WHITE)
print("by Kraskaska & IJlyxa")
print(colorama.Fore.YELLOW+"Купите полную версию, чтобы убрать сообщение!"+colorama.Fore.WHITE)
print("{0}")
print("Подготовка к установке...")
if argsnamespace.debuglevel == "Debug":
    print("[DEBUG] инициализация...")