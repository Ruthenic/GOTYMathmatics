## HowLongToBeat
so we can get the game id on the search page by searching for the xpath `/html/body/div[1]/form/div[5]/div/div/div[6]/div/ul/li[1]/div[2]/h3/a` (maybe consistently?)  
now we just need to actually find the input and put the game in there and we have the game page to get the time from

why does the search box use an onkey event for gods sake, why does it gotta be like that  
ok, so the web request sent *does* contain a `queryString` that we can use in this case to simulate a key press, we just have to figure out how to send an edited version of the response  
heck yes it actually works, i can resend the response with an edited querystring and get the new responses  
so now we should just have to send a response with python and scrape that xpath, and now we have the game id?  
this seems over complicated, why does hltb not have a public api  
lol i dont have to do any of this because someone else already has  
https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI
