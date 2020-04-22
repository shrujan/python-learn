
from xml.dom.minidom import parse

import xml.dom.minidom

DOMTree =  xml.dom.minidom.parse("movies.xml")

collection = DOMTree.documentElement   #returns root element - Collection as node object

moviesList = collection.getElementsByTagName("movie")

print("*************************************")
print(' Total Number of Moves in the list are: ' + str(len(moviesList)))
print("-------------------------------------")

for movie in moviesList:
    print('*************************')
    if movie.hasAttribute('title'):
        print("Movie Name: ", movie.getAttribute('title'))

        type = movie.getElementsByTagName('type')[0]
        print("\t Type: ", type.childNodes[0].data)

        format = movie.getElementsByTagName('format')[0]
        print("\t Format: ",format.childNodes[0].data)
        
        Rating = movie.getElementsByTagName('rating')[0]
        print("\t Rating: ",Rating.childNodes[0].data)

        stars = movie.getElementsByTagName('stars')[0]
        print("\t Stars: ",stars.childNodes[0].data)

        description = movie.getElementsByTagName('description')[0]
        print("\t description: ",description.childNodes[0].data)
