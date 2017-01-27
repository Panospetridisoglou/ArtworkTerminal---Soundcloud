import urllib2
import requests
def savepic(image,i):
    f = open('%d.jpg'%i,'wb')
    f.write(requests.get(image).content)
    f.close()
search = raw_input("Give a name of artist")
response = urllib2.urlopen("https://soundcloud.com/search/people?q=%s"%search)
html = response.read()
people=[]
for i in range (7,17):
    link="https://soundcloud.com"+html.split("<a")[i].split('"')[1]
    print "P"+str((i-7))+"  "+str(html.split("<a")[i].split(">")[1].split("<")[0])
    people.append(link)
select = raw_input("choose\n")
c=0
for i in range (0,10):
    if (select==("p"+str(i))):
        link=people[i]+"/tracks"
        response = urllib2.urlopen(link)
        html=response.read()
        image= html.split('content="')[41].split('"')[0]
        c+=1
        savepic(image,c)

