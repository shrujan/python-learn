import re

urlFile = open('TextFiles/url.txt', "r")


while True:
        str = urlFile.readline()
        if str:
                # check for http or https 0 or more at beginning
                # :// 0 or more 
                # www - 1 or more 
                # a-zA-Z0-9, 1 or more
                # .com $ - at the end 
                # *   0 or more occurance
                # +   1 or more
                # ?   0 or 1 only
                # {number of occourances}
                # ^ beginning $ end
                # (goup)
                regEx = "^(http|https)?(://)?(www){1}.[a-zA-Z0-9]+.(com){1}$"

                match1 = re.match(regEx, str)

                if match1:
                        print('Valid URL:== ', str )
                else:
                        print( 'Wrong URL:== ', str)
                

        else:
                print ("----------------------")
                break
urlFile.close()


