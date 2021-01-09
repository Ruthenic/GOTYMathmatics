#someone has already done this so i sure am not, but i am leaving this here incase anyone wants to look at my attempt

import requests
from lxml import html
class hltb():
    def getGameTime(gamename):
        if not isinstance(gamename, str):
            raise Exception("gamename not a string")
        searchPage = requests.post('https://howlongtobeat.com', data='queryString=' + gamename.replace(' ', '%20') + '&t=games&sorthead=popular&sortd=Normal Order&plat=&length_type=main&length_min=&length_max=&detail=&randomize=0')
        doc = html.fromstring(searchPage.content)
        content = doc.xpath("//li[1]/div[@class='search_list_details' and 2]/h3[@class='shadow_text' and 1]/a[@class='text_white' and 1]")
        print(searchPage.url)
        return content
print(hltb.getGameTime('Celeste'))
