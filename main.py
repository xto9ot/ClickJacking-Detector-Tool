from bs4 import BeautifulSoup
import requests

print("--------------------------------------------------------------------------------")
print("---------------------------ClickJacking Detection Tool--------------------------")
print("--------------------------------------------------------------------------------")
link = input("Enter The URL:")
x= requests.get(link)
soup = BeautifulSoup(x.text,'html.parser')
iframes=soup.find_all('iframe')
if iframes==[]:
    print("No ClickJacking Detected \n")
else:
    print("Link Might Contain ClickJacking\n")
    print("What we found in the website:\n",iframes)
print("--------------------------------------------------------------------------------")
print("---------------------------------Made by Xto9ot---------------------------------")
print("--------------------------------------------------------------------------------")