from bs4 import BeautifulSoup
import requests
import speech_recognition as s
query='\0'


i=0
search_results=[]


def main():
       global i,query
       r=s.Recognizer()
       with s.Microphone() as source:
              print ('talk!!')
              audio=r.listen(source)
       try:
              query=r.recognize_google(audio)

       except:
              pass

       if query=='\0':
              return
       
       if query=="next":
              i=i+1
              print(search_results[i])
       else:
              i=0
              print(query)
              del search_results [:] 
              keyword=query.replace(" ","+")
              google_search="https://www.google.co.in/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q="+keyword
              r=requests.get(google_search)
              soup=BeautifulSoup(r.text,"html.parser")
              url=soup.findAll('span',{"class":"st"})

              for u in url:
                     search_results.append(u.text)

              print(search_results[0])
              query='\0'


if __name__=='__main__':
       while 1:
              main()






"""
with s.Microphone() as source:
       print ('talk!!')
       audio=r.listen(source)
try:
       print ('you said that:\n'+r.recognize_google(audio))

except:
       pass
"""
