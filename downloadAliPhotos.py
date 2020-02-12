#encoding=utf8
import urllib
import bs4
import string

#prodLink = "https://www.alibaba.com/product-detail/55-inch-floor-stand-display-digital_1362901286.html"

res = urllib.urlopen(prodLink)
print "1111111111"
#print res.read()

soup = bs4.BeautifulSoup(res,features="html.parser")
print "22222222222"
#print res.read()

book_div = soup.find(attrs={"class":"inav util-clearfix"})
print "3333333333333"

book_img = book_div.findAll("img")
print "44444444444"

#define local file folder
folder = prodLink

x = 1
for book in book_img:
    print "---%----".replace("%",str(x))
    url = book.attrs["src"]
    url_correct = ""
    #print "Original URL:"
    #print url

    #Add http if missing this character
    if str(url).__contains__("http"):
        url_correct = str(url)
    else:
        #urllib.urlretrieve("http:"+url,str(x) + ".jpg")
        url_correct = "http:" + str(url)
        #print "Adjusted URL:"
        #print url_correct

    #remove the last preview image characters,and download the original images
    url_correct = url_correct.replace("_50x50.jpg","")
    print "Large image URL:"
    print url_correct

    #define the image file name
    i = len(url_correct.split("/"))
    fileName = url_correct.split("/")[i-1]
    path = "C:\Users\henry\Documents\Henry\images\\" + str(x) + "#" + str(fileName)
    urllib.urlretrieve(url_correct,path)
    x+=1

print "Download images successfully. Total {0} images.".format(x)
