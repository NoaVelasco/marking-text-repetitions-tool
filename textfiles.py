#!/usr/bin/env python3.10
# Python 3.10.2 UTF-8
# Copyright (c) 2023, Noa Velasco

import re
from pathlib import Path
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
# from docx import Document
# import paths


# def filetype(pathfile, dict):
#     if pathfile.suffix == '.docx':
#         filedocx(pathfile)
#     elif pathfile.suffix == '.txt':
#         filetxt(pathfile)
#     elif pathfile.suffix == '.md':
#         filetxt(pathfile)
#     else:
#         print('*** No es una opción válida ***\n\
# Prueba con un documento .docx, .txt o .md')
#         paths.looping(pathfile, dict)


class Coinsidensias:
    '''
    Relationed functions in order to compare words and change the similar ones.
    The output is a copy of the text, but with markdown format highlight.
    '''

    def __init__(self, pathfile):
        self.path = Path(pathfile)
        self.name = pathfile.name
        self.simplename = pathfile.stem
        self.ext = pathfile.suffix
        self.text = self.extract_text()
        # En teoría, al arrancar la clase tiene que iniciar esta función,
        # que según el tipo de archivo devolverá una lista para configurar self.text
        self.new_text = []
        self.match_ltr = 0

# -------------------------WORKING WITH FILES--------------------------------------

    def extract_text(self):
        '''Determines what kind of file and choose the extract mode.'''
        if self.ext == '.docx':
            return self.filedocx()
        return self.filetxt()

    def filedocx(self):
        '''Extracts the contents of the docx file and returns a list of words.'''
        print(f'«{self.name}» es un docx')

        doc_file = Document(self.path)
        doc_text = []
        for para in doc_file.paragraphs:
            prestring = re.split(r'([\W]+)', para.text)
            # Separates words and no-words/characters/spaces…
            for word in prestring:
                doc_text.append(word)
        return doc_text

    def filetxt(self):
        '''Extracts the contents of the text file and returns a list of words.'''
        print(f'«{self.name}» es un archivo de texto')

        with open(self.path, 'r', encoding='utf-8') as f:
            txt_file = f.read()

        return re.split(r'([\W]+)', txt_file)

# -------------------------WORKING WITH WORDS--------------------------------------

    def highlight(self, word):
        '''Apply markdown format highlight adding a special character.'''
        # I know there is a way to do this with @decorators,
        # but it's for my future me.
        return f'=={word}==Ç'

    def replacing(self, word):
        '''Spanish words has special characters, most of them vowels with «tilde».
        This function replaces the word with a safe version only for comparing.'''
        tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                  'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}

        wildcard = []
        for l in word:
            if l in tildes:
                l = l.replace(l, tildes[l])
            wildcard.append(l.lower())
        word = ''.join(wildcard)

        return word

    def scanwords(self, word1, word2):
        '''Compares 2 words: if they have a matching nr of letters,
        return True, otherwise return False'''
        word1 = self.replacing(word1)
        word2 = self.replacing(word2)

        # si las palabras son de al menos x letras
        MIN = 5
        pattern = r'[a-zA-ZñÑ]{5}'
        # si no tiene ese mínimo de caracteres alfabéticos
        # no funciona si le pongo una variable, solo el número: {5}.
        x = re.search(pattern, word1)
        y = re.search(pattern, word2)
        if x is None:
            return False
        if y is None:
            return False

        for n in range(len(word1)-MIN+1):
            searching = word1[0+n:MIN+n]
            searching = re.search(searching, word2)
            if searching is not None:
                return True
        return False

# -------------------------DOING THE MAGIC--------------------------------------

    def activate(self):
        '''Scan a text word by word, then compare they with a number of words before
        and after them. If similar, append a highlighted version in the new text list'''

        # A list of words can be created; will not be taken into account:
        # except_file = Path(r'absolutepath/exceptions.txt')
        # with open(except_file, encoding='utf-8') as ex:
        #     exceptions = ex.read().splitlines()

        for i, word1 in enumerate(self.text):
            reqs = False
            words_cnt = 0
            word2 = ""
            highld = False
            is_word = r'([\W]+)'

            while reqs is False:
                y = i-60+words_cnt
                # Como las separaciones también cuentan como palabras (espacios, p. ej.),
                # tengo que poner más margen: 60-121
                scape_word = re.search(is_word, word1)

                # if scape_word is not None or word1 in exceptions:
                if scape_word is not None:
                    reqs = True
                    # cumple requisitos para salir del bucle: append normal
                elif y == i:
                    words_cnt += 1
                    # si es la misma instancia de palabra, a por la siguiente
                elif y < 0:
                    words_cnt += abs(y)
                    # Evita un resultado de nºs negativos si compara al principio del texto
                elif words_cnt == 121 or y >= len(self.text):
                    reqs = True
                    # No tiene en cuenta más palabras.
                else:
                    # cumple condiciones para scanwords.
                    word2 = self.text[y]
                    scape_word = re.search(is_word, word2)

                    if scape_word is not None:
                        words_cnt += 1
                    # Si no es palabra de verdad, a por la siguiente.
                    # Voy a hacer esto mismo con word1, más arriba.
                    else:
                        compare = self.scanwords(word1, word2)

                        if compare is True:
                            self.new_text.append(self.highlight(word1))
                            # Si la comparación es positiva (es similar),
                            # hace append con highlight
                            highld = True
                            reqs = True
                            # Y cumple requisitos para salir del bucle con
                            # variable especial para que no haga otro append.
                        else:
                            words_cnt += 1
            if highld is False:
                self.new_text.append(word1)


# -------------------------WRITTING THE VERSIONS--------------------------------------

    def write_docx(self, docx):
        pre_py_docx = []

        # @TODO tengo que idear la forma de adaptar lo que hice
        # con los "pero" a las palabras rodeadas de ==.
        # Voy a probar a marcar lo que sea lista y añadir solo el elemento[1]

        for word in self.new_text:
            if 'Ç' in word:
                word = word.split('==')
            pre_py_docx.append(word)

        docx.add_heading("Versión docx con palabras resaltadas")
        # run = sigue.add_run()
        # font = run.font
        # font.name = 'Bookerly'
        style = docx.styles
        par_style = style.add_style('custom', WD_STYLE_TYPE.PARAGRAPH)

        par_style.paragraph_format.first_line_indent = Inches(0.25)
        par_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        par_style.paragraph_format.space_before = Pt(0)
        par_style.paragraph_format.space_after = Pt(0)
        par_font = par_style.font
        par_font.name = 'Bookerly'
        par_font.size = Pt(12)

        char_charstyle = style.add_style('highlight', WD_STYLE_TYPE.CHARACTER)
        char_font = char_charstyle.font
        char_font.highlight_color = WD_COLOR_INDEX.YELLOW
        char_font.name = 'Bookerly'
        char_font.size = Pt(12)

        sigue = docx.add_paragraph('', style='custom')
        run = sigue.add_run()

        for word in pre_py_docx:
            if word != '':
                if isinstance(word, list):
                    run = sigue.add_run(
                        word[1], style='highlight').font.highlight_color = WD_COLOR_INDEX.YELLOW
                else:
                    run = sigue.add_run(word)
                    run.font.name = 'Bookerly'

            else:
                sigue = docx.add_paragraph(word, style='custom')

    def savedocx(self):
        doc_copy = Document()
        self.write_docx(doc_copy)

        copy_name = f'{self.path.parent}/{self.simplename}-py.docx'
        doc_copy.save(copy_name)
        return 'El archivo ha sido copiado con cambios.'

    def savemd(self):
        # El problema es que de momento hay un Ç tras los resaltes.
        copy_name = f'{self.path.parent}/{self.simplename}-py.md'
        md_text = ''.join(self.new_text)
        with open(copy_name, 'w', encoding='utf-8') as txt:
            txt.write(md_text)
        return 'El archivo ha sido copiado con cambios.'

    def writefiles(self):
        self.activate()
        self.savedocx()
        self.savemd()
