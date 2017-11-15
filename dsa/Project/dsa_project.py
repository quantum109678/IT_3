import json
import requests
import re


class Node:

    def __init__(self):
        self.val=None
        self.next=None

class TrieNode:
    # Trie node class
    def __init__(self):
        self.children=[]
        for i in range(26):
            self.children.append(Node())

        self.EOW=False

    def __getitem__(self,index):
        return self.children[index]

    



class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        return TrieNode()



    def _charToIndex(self, ch):

        return (ord(ch) - ord('a'))

    def insert(self, key,det):
        


        tmp=self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])


            if index<=26 and index>=0:
                if tmp.children[index].val==None:
                    tmp.children[index].val=key[i]
                    tmp.children[index].next= self.getNode()


                tmp=tmp.children[index].next


                if i==len(key)-2:
                    curr=tmp.__getitem__(index)

        tmp.EOW=True
        

        if curr.next==None:
            curr.next=det
        else:
            det.next=curr.next
            curr.next=det
        


    def song_search(self, key):


        tmp= self.root
        length = len(key)


        for i in range(length):
            index = self._charToIndex(key[i])

            if tmp.children[index].val==None:
                print("No results found :(")
                return
            
            else:
                tmp=tmp.children[index].next


            if i==len(key)-1 and tmp.EOW==False:
                print("No results found :(")
                return

            if i==len(key)-2:
                curr=tmp.__getitem__(index)
                

        curr=curr.next
    
        print("SONG:",curr.ori_song,"\nARTIST:",curr.ori_artist,"\nDURATION:",curr.duration,"seconds\nURL:",curr.url)
        print()


    def artist_search(self,key):

        tmp= self.root
        length = len(key)
        print("len",length)
        for i in range(length):
            index = self._charToIndex(key[i])

            if tmp.children[index].val==None:
                print("No results found :(")
                return
            
            else:
                tmp=tmp.children[index].next

            if i==len(key)-1 and tmp.EOW==False:
                print("No results found :(")
                return

            if i==len(key)-2:
                curr=tmp.__getitem__(index)

        curr=curr.next

        while curr!=None:
            print("SONG:", curr.ori_song, "\nARTIST:",curr.ori_artist, "\nDURATION:",
                  curr.duration, "seconds\nURL:", curr.url)
            print()
            curr=curr.next



class song_obj:
    def __init__(self,key1,key2,song,artist,duration,url):
        self.song_key=key1
        self.artist_key=key2
        self.duration=duration
        self.url=url
        self.ori_song=song
        self.ori_artist=artist
        self.next=None


# driver function
def main():
    t=Trie()
    response = requests.get("http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&api_key=14bdca878b6b2ad0a9ba5278a32a1e14&format=json&limit=400")
    data = response.json()
    for i in range (400):
        if i!=296 and i!=9:
            s=data["tracks"]["track"][i]["name"]
            os=data["tracks"]["track"][i]["name"]
            ar=data["tracks"]["track"][i]["artist"]["name"]
            oriar=data["tracks"]["track"][i]["artist"]["name"]
            du=data["tracks"]["track"][i]["duration"]
            url=data["tracks"]["track"][i]["url"]
            s=s.replace(" ","")
            ar=ar.replace(" ","")
            s=s.lower()
            s=re.sub("[^a-z]+", "",s)
            ar=ar.lower()
            ar=re.sub("[^a-z]+", "",ar)
            temp=song_obj(s,ar,os,oriar,du,url)
            t.insert(temp.song_key,temp)
            t.insert(temp.artist_key,temp)
    while True:
        print("Press:\n\t1) to search through song\n\t2) to search through artist\n\t3) to Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            song=input("Enter song name:")
            song = song.replace(" ", "")
            song = song.lower()
            t.song_search(song)
        elif ch==2:
            art=input("Enter artist name:")
            art = art.replace(" ", "")
            art = art.lower()
            t.artist_search(art)
        else:
            break





if __name__ == '__main__':
    main()