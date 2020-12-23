from transitions.extensions import GraphMachine

from utils import send_text_message ,push_message, send_image_carousel,send_button_message,send_button_carousel,send_image_url,send_button_budget,send_video_url
import requests 
from bs4 import BeautifulSoup
import csv
import os.path

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return True

# first carusol
    def is_going_to_find_laptop(self, event):
        text = event.message.text
        return text.lower() == "search laptop"
    def is_going_search_cpu(self, event):
        return True
    def is_going_to_search_laptop(self,event):
        return True
    def is_going_budget(self,event):
        text = event.message.text
        return text.lower() =="budget"
    def is_going_range(self,event):
        return True
    def is_going_to_fsm(self,event):
        text = event.message.text
        return text.lower() =="fsm"
# second carosel
    def is_going_top_cpu_laptop(self,event):
        text = event.message.text
        #print("entering cpu")
        return text.lower() == "top laptop cpu"
    def is_going_top_gpu_laptop(self,event):
        text = event.message.text
        #print("entering gpu")
        return text.lower() == "top gpu for laptop"
    def is_going_to_cgpu_review(self,event):
        text = event.message.text
        return text.lower() =="cgpu_review"



# third carusol
    def is_going_to_high_game(self,event):
        text = event.message.text
        return text.lower() == "high game"
    def is_going_to_mid_game(self,event):
        text = event.message.text
        return text.lower() == "mid game"
    def is_going_to_program(self,event):
        text = event.message.text
        return text.lower() == "program"
    def is_going_cpu_info(self,event):
        return True

    def is_going_to_laptop_search(self,event):
        return True
    def is_going_to_requirement(self,event):
        text = event.message.text
        return text.lower() == "requirement"
    def is_going_back(self,event):
        text = event.message.text
        return text.lower() == "return"
    def is_going_to_games(self,event):
        return True
    #last carosel
    def is_going_to_coolpc(self,event):
        text = event.message.text
        return text.lower() =="coolpc_link"
    def is_going_to_apple(self,event):
        text = event.message.text
        return text.lower() =="apple_link"
    def is_going_to_pchome(self,event): 
        text = event.message.text
        return text.lower() =="pchome_link"  
    def on_enter_show_games(self,event):
        text = event.message.text
        reply_token = event.reply_token
        url = "https://www.intel.com/content/www/us/en/gaming/resources/system-requirements.html"
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        rows = soup.findAll("div", {"class": "editorialtable section"})

        row_ler=[y.text for y in rows]
        row_ler =[i.replace('\n\n',"")for i in row_ler]
        if(text=="0"):
            send_text_message(reply_token,row_ler[0][:-28])
        elif(text=="1"):
            send_text_message(reply_token,row_ler[1][:-28])
        elif(text=="2"):
            send_text_message(reply_token,row_ler[2][:-28])
        elif(text=="3"):
            send_text_message(reply_token,row_ler[3][:-28])
        elif(text=="4"):
            send_text_message(reply_token,row_ler[4][:-28])
    def on_enter_requirement(self,event):
        reply_token = event.reply_token
        one = 'https://steamcdn-a.akamaihd.net/steam/apps/1091500/header.jpg?t=1608552868'
        two = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/MarvelLogo.svg/1280px-MarvelLogo.svg.png'
        three = 'https://image.api.playstation.com/cdn/HP9000/CUSA05682_00/1J6HqFz7q5jR0bS1poj3oYbQ9veI64NgpGHo36qeC4CfwrLjikjQYONSqBtwXwiU.png'
        four = 'https://www.riotgames.com/darkroom/1370/d0807e131a84f2e42c7a303bda672789:a0e5fc336a003f2987ce613812fbf9f4/valorant-offwhitelaunch-keyart.jpg'
        five = 'https://cdn-wp.thesportsrush.com/2020/09/cod-warzopne.jpg'
        urls = [one, two, three, four, five]
        labels=["Cyber","Marvel","Horizon","Valorant","COD"]
        text =["0","1","2","3","4"]
        #print(len(urls))
        #print(labels)
        userid = event.source.user_id
        send_image_carousel(userid, urls, labels, text)
        msg = "Choose One"
        push_message(userid, msg)
    def on_enter_cgpu_review(self,event):
        reply_token = event.reply_token
        userid = event.source.user_id
        push_message(userid,"CPU")
        send_text_message(reply_token,"https://www.youtube.com/watch?v=VDZQCcDMcfw")
        push_message(userid,"GPU")
        push_message(userid,"https://www.youtube.com/watch?v=CoDPTJ-3qCM")
    def on_enter_coolpc(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "http://www.coolpc.com.tw/evaluate.php")
    def on_enter_apple(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.apple.com/tw/?afid=p238%7CsdGAPHwnZ-dc_mtid_18707vxu38484_pcrid_486296301760_pgrid_12618487742_&cid=aos-tw-kwgo-brand--slid---product--")
    def on_enter_pchome(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://24h.pchome.com.tw/region/DHAA")
    def on_enter_fsm(self,event):
        reply_token = event.reply_token
        send_image_url(reply_token,"https://raw.githubusercontent.com/johnyu1234/LineBot/master/fsm.png")
    def on_enter_range(self,event):
        text=event.message.text
        arr=list()
        if(text=="<$700"):
            arr=["Best Business Laptop:","Lenovo ThinkPad E15","Best Overall:","Acer Swift 3 (SF314-42)","Best for Student:","ASUS ZenBook 14 UM433"]
        elif(text=="<$500"):
            arr=["Newest Model:","Dell Inspiron 15 3593","Best Overall:","Acer Aspire 3 (A317-51G)","Value for Money:","Acer Aspire 5 (A515-56G)"]
        elif(text=="<$300"):
            arr=["14-inch Laptop:","Lenovo Ideapad 110 (15″)","15-inch Laptop:","Asus VivoBook 15 L510MA-DB02","Touchscreen:","Lenovo Chromebook S330 (14″)"]
        string = "\n".join(arr)
        reply_token = event.reply_token
        send_text_message(reply_token, string)
        userid = event.source.user_id
        push_message(userid,"Please enter search laptop")
    def on_enter_budget(self,event):
        userid = event.source.user_id
        send_button_budget(userid)
    def on_enter_gpu(self,event):
        url = "https://laptopmedia.com/top-laptop-graphics-ranking/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        rows = soup.find("table", {"class": "table-style-4 rate_table"})
        rows = rows.tbody.find_all("tr")
        row_list = list()
        i = 0
        for tr in rows[6:]:
            if (i == 14):
                break
            th = tr.find_all('a')
            row = [i.text for i in th]
            row = [i.replace('\xa0', "") for i in row]
            row = [i.replace('...', "") for i in row]
            row = [i.replace('  ', "") for i in row]
            row_list.append(row)
            i += 1
        t = 1
        labels = list()
        text = list()
        for i in range(len(row_list)):
            if (i % 2 == 0):
                text.append(str(t)+": "+row_list[i][1]+" "+row_list[i][2])
                t+=1
        string = "\n".join(text)
        reply_token = event.reply_token
        send_text_message(reply_token, string)
    def on_enter_start(self,event):
        userid = event.source.user_id
        send_button_carousel(userid)
    def on_enter_program(self,event):
        reply_token = event.reply_token
        one = 'https://cdn.mos.cms.futurecdn.net/BWsKGDUhVnQCYUykJSmHxK-970-80.jpg.webp'
        two = 'https://cdn.mos.cms.futurecdn.net/5ee3h97W4HdReSx7jWp8AW-970-80.jpg.webp'
        three = 'https://cdn.mos.cms.futurecdn.net/McyW7sR2fGuWDLFjAvzP2H-970-80.jpg.webp'
        four = 'https://cdn.mos.cms.futurecdn.net/8Z2ajoNMvvFb8WTokE3amZ-970-80.jpg.webp'
        five = 'https://cdn.mos.cms.futurecdn.net/9Efer8PDwqDAZJvVpgwZqD-970-80.jpg.webp'
        urls = [one, two, three, four, five]
        labels=["Hp","Lenovo","Apple","Apple","Microsoft"]
        text =["HP Spectre x360 13 (13-aw0000)","Lenovo ThinkPad X1 Extreme Gen 2","Apple MacBook Air 13 (2020)","Apple MacBook Pro 16 (2019)","Microsoft Surface Pro 7"]
        #print(len(urls))
        #print(labels)
        userid = event.source.user_id
        send_image_carousel(userid, urls, labels, text)
        msg = "Choose One"
        push_message(userid, msg)
    def on_enter_mid_game(self,event):
        reply_token = event.reply_token
        one = 'https://www.lenovo.com/medias/lenovo-legion-y540-15-3.png?context=bWFzdGVyfHJvb3R8MTI1NjA1fGltYWdlL3BuZ3xoYmMvaDY4LzEwMDkyNjE0MjU0NjIyLnBuZ3w5YzU2YTdkYjU3M2UxZjY1NGMyMzlhNDc2ZDAyZjZhNTVhYmFiMTc5NTc1YzZhY2U2N2JlZjU5NzM5OWM2M2Yy'
        two = 'https://cdn.mos.cms.futurecdn.net/oXmE4PwwP9RGYAz47Hnhai-970-80.jpg.webp'
        three = 'https://cdn.mos.cms.futurecdn.net/J6g9K9D3ge4XR6TYR9SEmn-970-80.jpg.webp'
        four = 'https://images-na.ssl-images-amazon.com/images/I/81WDXiOLM6L._AC_SL1500_.jpg'
        five = 'https://www.notebookcheck.net/uploads/tx_nbc2/4zu3_Acer_Nitro_5_AN517_52.jpg'
        urls = [one, two, three, four, five]
        labels=["Lenovo","Dell","Asus","HP","Acer"]
        text =["Lenovo Legion Y545","Dell G3 15","Asus TUF Gaming A15( FA506)","HP Pavilion Gaming 15 (15-dk)","Acer Nitro 5 (AN515-55)"]
        #print(len(urls))
        #print(labels)
        userid = event.source.user_id
        send_image_carousel(userid, urls, labels, text)
        msg = "Choose One"
        push_message(userid, msg)
    def on_enter_high_game(self,event):
        reply_token = event.reply_token
        one = 'https://cdn.mos.cms.futurecdn.net/q8dZoxDaAkAVMBheY5X5yJ-970-80.jpg.webp'
        two = 'https://cdn.mos.cms.futurecdn.net/tEzTTgKtmNBuLfeZgwf8uk-970-80.png.webp'
        three = 'https://brain-images-ssl.cdn.dixons.com/7/3/10211737/u_10211737.jpg'
        four = 'https://cdn.mos.cms.futurecdn.net/5PDW7HKPcLduRJx6dXYYzB-970-80.jpg.webp'
        five = 'https://cdn.mos.cms.futurecdn.net/k6tkVDv8T2xADuDVqv4u3m-970-80.jpg.webp'
        urls = [one, two, three, four, five]
        labels=["Razer","Asus","Alienware","Msi","Acer"]
        text =["Razer Blade 15 (2020)","ASUS ROG SCAR Edition (GL503VS)","Alienware m17 R3","MSI GS65 Stealh Thin","Acer Predator Helios 300"]
        print(len(urls))
        print(labels)
        userid = event.source.user_id
        send_image_carousel(userid, urls, labels, text)
        msg = "Choose One"
        push_message(userid, msg)
    def on_enter_search_laptop(self,event):
            text = event.message.text.lower()
            text = text.replace(" ", "-")
            reply_token = event.reply_token
            url = "https://laptopmedia.com/series/"+text+"/"
            page =requests.get(url)
            soup = BeautifulSoup(page.content,'html.parser')           
            rows = soup.find("div",{"class":"col-md-6 lm-catalog-info"})
            rows = rows.find("a",href=True) 
            new = rows['href']
            pages=requests.get(new)
            soupy = BeautifulSoup(pages.content,'html.parser')
            rows_1 = soupy.find("div",{"class":"lp-catalog-header-info"})
            rows_1 = rows_1.find_all("li")
            row_ler=[y.text for y in rows_1]
            string = "\n".join(row_ler)
            send_text_message(reply_token, string)

    def on_enter_laptop(self, event):
        print("I'm entering laptop")
        reply_token = event.reply_token
        send_text_message(reply_token, "Please Select Laptop")
    def on_enter_cpu_info(self,event):
        text = event.message.text.lower()
        text = text.replace(" ", "-")
        url = "https://laptopmedia.com/processor/"+text+"/"
        page =requests.get(url)

        soup = BeautifulSoup(page.content,'html.parser')

        rows = soup.find("div",{"class":"col-md-6 col-sm-12"})
        rows = rows.tbody.find_all("tr")
        row_list = list()
        for tr in rows:
            th = tr.find_all('th')
            td = tr.find_all('td')
            row = [i.text for i in th]
            row = [i.replace('\xa0', "") for i in row]
            row = [i.replace('...', "") for i in row]
            row_td = [i.text for i in td]
            row_td = [i.replace('\xa0', "") for i in row_td]
            row_td = [i.replace('...', "") for i in row_td]
            str1 =''.join(row)
            str2 =''.join(row_td)
            row_list.append(str1+" :"+str2)
        string = "\n".join(row_list)
        reply_token=event.reply_token
        send_text_message(reply_token, string)
    def on_enter_cpu(self,event):
        url = "https://laptopmedia.com/top-laptop-cpu-ranking/"
        page =requests.get(url)

        soup = BeautifulSoup(page.content,'html.parser')

        rows = soup.find("table",{"class":"table-style-4 rate_table"})
        rows = rows.tbody.find_all("tr")
        row_list = list()
        i=0
        for tr in rows:
            if(i==10):
                break
            th = tr.find_all('a')
            row = [i.text for i in th]
            row = [i.replace('\xa0', "") for i in row]
            row = [i.replace('...', "") for i in row]
            row_list.append(row)
            i+=1
        arr=list()
        t=0
        labels=list()
        text=list()
        for i in range(len(row_list)):
        
            if(i%2==0):
                text.append(row_list[i][1])
        one = 'https://sunfar.blob.core.windows.net/webimage/jpg360/251/251454YF10.jpg'
        two = 'https://static.techspot.com/images/products/2018/processors/intel/org/2018-10-19-product.jpg'
        three = 'https://sunfar.blob.core.windows.net/webimage/jpg360/251/251454YF10.jpg'
        four = 'https://images.versus.io/objects/amd-ryzen-7-4800h.front.medium.1584042851705.webp'
        five = 'https://images.versus.io/objects/amd-ryzen-9-4900hs.front.medium.1587585924969.webp'
        urls = [one, two, three, four, five]
        labels=["Intel","Intel","Intel","AMD","AMD"]
        print(len(urls))
        print(labels)
        print(text)
        userid = event.source.user_id
        send_image_carousel(userid, urls, labels, text)
        msg = "Press click on any CPU for more info"
        push_message(userid, msg)
    def on_enter_laptop_search(self,event):
        text = event.message.text.lower()
        reply_token = event.reply_token
        text = text.replace(" ", "-")
        url = "https://laptopmedia.com/series/"+text+"/"
        page =requests.get(url)
        userid = event.source.user_id
        if(page.status_code==200):
            #print("true")
            soup = BeautifulSoup(page.content,'html.parser')
            rows = soup.find("div",{"class":"col-md-2 lm-image"})
            rows = rows.find("img")
            hello = rows.get("src")
            
            soup = BeautifulSoup(page.content,'html.parser')
            
            rows = soup.find("div",{"class":"col-md-6 lm-catalog-info"})
            rows = rows.find("a",href=True)
            
            new = rows['href']
            pages=requests.get(new)
            soupy = BeautifulSoup(pages.content,'html.parser')
            rows_1 = soupy.find("div",{"class":"lp-catalog-header-info"})
            rows_1 = rows_1.find_all("li")
            row_ler=[y.text for y in rows_1]
            string = "\n".join(row_ler)
           # print(string)
            send_image_url(reply_token,hello)
            push_message(userid,string)
        else:
           # print("false")
            push_message(userid,"laptop doesn't exists,please try again")
            self.go_laptop()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_exit_state3(self):
        print("Leaving state3")
