# Marking text repetitions tool

Parses a text document and creates a copy in which repetitions and nearby similar words are highlighted.

Input formats:  
- txt
- md
- docx

Output formats:  
- docx
- md


## Requirements
Tested with:
- Python==3.10.2
- python-docx==0.8.11

`pip install python-docx`

## Usage
Close any document to parse first.  
Run `main.py`.  
Browse the directories and files with numeric inputs  

![browsing](samples/browsing.jpg)

Choose a text file.  
Two new files will be created:  
- `filename-py.docx`
- `filename-py.md`

## Keep in mind
Italic, bold and other text format will be lost. The copy files are only for reference when I make a style correction of the text.

Highlight format in markdown (==like this==) are not supported for all the editors.

Python-docx highlight format is sort of weak. This means they can dissapear once the file is closed for the first time. I don't know why. The words remain with a character style named "highlight", so they can be formatted to bold or other style easily.

Interface in Spanish.

---

# Herramienta de marcado de repeticiones en texto 

Analiza un documento de texto y crea una copia en la que aparecen resaltadas repeticiones y palabras similares cercanas.  

Formatos de entrada:  
- txt
- md
- docx

Formatos de salida:  
- docx
- md


## Requisitos
Comprobado con:
- Python==3.10.2
- python-docx==0.8.11

`pip install python-docx`

## Uso
Cierra antes cualquier documento que vaya a analizarse.  
Corre `main.py`.  
Navega por los directorios y archivos introduciendo su valor numérico  

![browsing](samples/browsing.jpg)

Escoge un archivo de texto.  
Se crearán dos archivos nuevos en la carpeta del archivo escogido:
- `nombreArchivo-py.docx`
- `nombreArchivo-py.md`

## Ten en cuenta
La cursiva, la negrita y otros formatos de texto se perderán en los archivos resultantes. Estos los uso solo como referencia cuando hago una corrección de estilo del texto y no debe corregirse sobre ellos.

El formato de resaltado en Markdown (==como este==) no es compatible con todos los editores.

El formato resaltado de Python-docx es algo débil. Esto significa que puede desaparecer al abrir el archivo por segunda vez o en cualquier momento tras su primera apertura. No sé por qué, tal vez es cuestión de versiones. De todas formas, las palabras mantienen un estilo de carácter llamado "highlight", por lo que se puede editar fácilmente para dar fomato negrita u otro estilo a todas a la vez.