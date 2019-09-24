# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('default.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
# print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(1) 

# extracting text from page 
txt=pageObj.extractText() 


import re
import string
x = re.sub('['+string.punctuation+']', '', txt).split()



if 'Threats' in x:
    print('threats are there')
    for page in range(int(x[-1])+4):
        
        pageObj = pdfReader.getPage(page)
        

        # extracting text from page 
        txt1=pageObj.extractText()

        convlist = txt1.split()
        
        if convlist[0] == 'Threats':
           

        
            findoccs=convlist.index('Occurrence')
            findocc=findoccs+1

            # print(findocc)
            findVictims=convlist.index('Victims')
            # print(findVictims)
            findVictim =  findVictims-1
            mainlist=convlist[findocc:findVictim]
            # print(mainlist)
            values=len(mainlist)
            value=values-4

            ip=txt1.split()
            print(ip)
            victimsipi = ip.index('Victims')+3
            print(ip[victimsipi])
            victimsipe = ip.index('Sources')-2
            print(ip[victimsipe])

            for g in range(victimsipi,victimsipe):
                if g%3==0:
                    vip=ip[g]
                    vocc=ip[g+1]
                    # print(vip+"and"+vocc)
                    for i in range(0, values):
                        if i % 4 == 0:
                            # print(mainlist[i])
                            if vocc == mainlist[i+3]:
                                print(mainlist[i]+"."+mainlist[i+1] + " is a  " +
                                    mainlist[i+2] + " whose Occurrence is " + mainlist[i+3] + " and the victim is "+vip)
                            else:
                                print(mainlist[i]+"."+mainlist[i+1] + " is a  " +
                                    mainlist[i+2] + " whose Occurrence is " + mainlist[i+3])
                                



    

    



        



# li = list(txt.split(" "))
# # print(li)

# # closing the pdf file object 
# pdfFileObj.close() 


