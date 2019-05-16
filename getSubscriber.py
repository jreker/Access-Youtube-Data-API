import requests

#set the youtube channel id you want to query and your generated youtube api key below:
youtubeChannelID = "<CHANNELID>"
youtubeAPIKey = "<YOUTUBE API KEY>"

url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+ youtubeChannelID +"=" + youtubeAPIKey

# make request agains youtube API
req = requests.get(url)
responseBody = req.json()
# fetch for example the subscribers
subscribers = responseBody['items'][0]['statistics']['subscriberCount']

print("Subscribers" + subscribers)