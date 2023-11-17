#!/usr/bin/env python3.10
# Python 3.10.2 UTF-8
# Copyright (c) 2023, Noa Velasco
from pathlib import Path
import textfiles


def scan_dir(path):
    '''With a path, returns a dictionary
    with numerical keys and where the values are
    the paths of files and directories in the path.
    Sorts the dirs first; then sorts the files.'''

    dic_content = {}
    counter = 1
    for entry in path.iterdir():
        if entry.is_dir():
            dic_content[counter] = entry
            counter += 1
    for entry in path.iterdir():
        if entry.is_file():
            dic_content[counter] = entry
            counter += 1
    return dic_content


def show_dir(dictio):
    '''Unpacks the dictionary and prints the contents with format.'''

    for nr, path in dictio.items():
        if path.is_file():
            print(f'{nr:02d} ◈   {path.name}')
        else:
            print(f'{nr:02d} ◳ {path.name}')


def goto(current_path, path_dic, number):
    '''With an input number given, it returns the path chosen.'''

    if number == 0:
        current_path = current_path.parent
    else:
        current_path = path_dic[number]
    return current_path


def curr_content(current_path, content_path):
    '''Prints with pretty formating the current dir and its contents.'''

    print(f'┌················┐\n\
| Carpeta actual └--\n\
|{current_path}\n\
└-------------------\n 0 ↩ SUBIR'
          )
    show_dir(content_path)


def looping(path, dictio):
    '''Plays a loop and navigate through the dirs
    until a file is chosen. Then, returns its path.'''

    finished = False
    while finished is False:
        curr_content(path, dictio)
        try:
            input_nr = int(input('Elige la carpeta o archivo: '))
        except ValueError:
            print('*** No es una opción válida ***')
            input_nr = int(input('Elige la carpeta o archivo: '))
        path = goto(path, dictio, input_nr)
        if Path(path).is_file():
            valid_ext = ['.docx', '.txt', '.md']
            if path.suffix in valid_ext:
                finished = True
            else:
                print('*** No es una opción válida ***\n'
                      'Prueba con un documento .docx, .txt o .md'
                      )
        else:
            dictio = scan_dir(path)
    return path
