

#!/usr/bin/python
import xml.sax   #event based Simple API for XML parser (SAX)


class MovieHandler( xml.sax.ContentHandler ):   #subclass of xml.sax.ContentHandler super class
   
   def __init__(self):     #constructor
      self.CurrentData = ""   #instance properties
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):   #attributes is dict, overriding method from class ContentHandler
      """ over rodding the pre defined method from ContentHandler class"""
      
      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         
         title = attributes["title"]  #value of a key title from a dcitionary attributes
         print ("Title:", title)

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "format":
         print ("Format:", self.format)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
         
            
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()    #..............1)
   # turn off namepsaces
   #parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()    #costructor   #..............2)
   parser.setContentHandler( Handler )  #registering the callback
   
   parser.parse("movies.xml")#parsing of movies.xml document is taking place..3)

   















