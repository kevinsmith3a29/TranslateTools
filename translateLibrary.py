#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen  # for shellCommand()

def shellCommand(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def translateWithGoogle(textToTranslate):
  textToTranslate = textToTranslate.replace("\"", "'")  # TODO  fix later.  quick fix to avoid bug
  source="de"
  target="en"
  translateCommand = 'curl -s -i --user-agent "" -d "sl='+source+'" -d "tl='+target+'" --data-urlencode "text='+textToTranslate+'"  "https://translate.google.com"   '
  webpage  = shellCommand(translateCommand)
  #print "tG: "+textToTranslate
  try:
     text = webpage.split("TRANSLATED_TEXT='")[1].split("'")[0]
  except IndexError:
     text = "Error getting result"
  text = text.replace("\\x26#39;", "'")
  #print "tG: "+text
  return text


originalText = "Guten tag!"
print "Testing translateWithGoogle, using: '" + originalText + "'"
translatedText = translateWithGoogle(originalText)
print "Result: '" + translatedText + "'"

