'''
Create a python script called googlesearch that provides a command line utility to
perform google search. It gives you the top links (search results) of whatever you want to
search on google
Input:-
python demo2_web.py 'Edureka'
'''
# Performing google search using Python code
import sys
class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=5,pause=2):
         count += 1
         print (count)
         print(i + '\n')
if __name__=='__main__':
   gs = Gsearch_python(str(sys.argv))
   gs.Gsearch()