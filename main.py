#Bryan Herrera & Bryant Tran
#COMP_141 Project Phase 1.2 Group 15

import sys
import re

def split(word): #Function to split words into chars
  return [char for char in word]
 
class Token:
  def __init__(self , tokenType , tokenValue):
    self.tokenType = tokenType
    self.tokenValue = tokenValue

  def __str__(self):
    return self.tokenType + " : " + self.tokenValue

def scanner(line):
  words = line.split()
  identifier = re.compile(r'^([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*')
  number = re.compile(r'^[0-9]+')
  symbol = re.compile(r'\+|\-|\*|/|\(|\)|:=|;')
  keyword = re.compile(r'if|then|else|endif|while|do|endwhile|skip')

  tokens = []
  for word in words:
    i = 0
    while(i < len(word)):
      longesttoken = None

      for j in range (i, len(word)):

        if keyword.fullmatch(word[i : j + 1]) != None:
          longesttoken = (Token("KEYWORD", word[i : j + 1]))

        elif identifier.fullmatch(word[i : j + 1]) != None:
          longesttoken = (Token("IDENTIFIER" , word[i : j + 1]))
      
        elif number.fullmatch(word[i : j + 1]) != None:
          longesttoken =(Token("NUMBER", word[i : j + 1]))
      
        elif symbol.fullmatch(word[i : j + 1]) != None:
          longesttoken =(Token("SYMBOL" , word[i : j + 1]))
          
        #tokens.append(Token("ERROR" , word))
      if longesttoken is None:
        tokens.append(Token("ERROR" , word[i]))
        return tokens
        
      i += len(longesttoken.tokenValue)
      tokens.append(longesttoken)
  return tokens


    
def main():

  if len(sys.argv) != 3:
    print("Error! Not enough arguements!")  #Error if there is not 3 sys arguements
    sys.exit(1)
    
  fileIn = sys.argv[1]  #Input file system arguement for command line
  fileOut = sys.argv[2] #Output file system arguement for command line

  with open(fileIn, 'r') as fIn, open(fileOut, 'w') as fOut:  #Opens input file to read
    for line in fIn:  #Iterate thorugh input file line by line
      print("Line: " + line)
      fOut.write("Line: " + line + "\n")  #Writes current line to be scanned to output file
      line = line.strip()

      tokenList = scanner(line)
      for token in tokenList:
        print(token)
        fOut.write(token.tokenType + " : " + token.tokenValue + "\n")
      
      fOut.write("\n")

      print("\n")

main()
