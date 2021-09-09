import re
from translator.keywords import keywords
from os import linesep

class Translator:
    
    def __init__(self, command_lines):
        self.command_lines = command_lines
        self.dynamic = {}

    def translate(self):
        result = ""
        for line in self.command_lines:
            for keyword in keywords.keys():
                line = re.sub(keyword, keywords[keyword], line)
        
            result += line + linesep
        
        return result
   
