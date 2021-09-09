from translator.translator import Translator

def parsefile(file:str):
    parts = file.split(".")
    if (parts[-1] != "czql"):
        print("ČQL files must ends with .czql!")
        exit()

    f = open(file)
    lines = f.readlines()
    f.close()

    translator = Translator(lines)
    compiled = translator.translate()
    parts.pop(-1)
    new_file = ".".join(parts) + ".sql"
    nf = open(new_file, "w")
    nf.write(compiled)
    nf.close()
