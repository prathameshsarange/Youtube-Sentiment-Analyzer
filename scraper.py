from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
API_KEY = "AIzaSyDhGZEQKDXa1REhw-NvVvP1RLrpLPwXYEg" 
VIDEO_URL = "https://www.youtube.com/watch?v=nZaDmhlMBOE"
analyzer = SentimentIntensityAnalyzer()
# collecting the video id by using the url
video_id = VIDEO_URL.split("v=")[1]
print("video id :", video_id)
# connecting the youtube api 
youtube = build("youtube" ,"v3",developerKey=API_KEY)
# fetching the comment 
request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=10
)
comments = []
response = request.execute()

while True:
    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    
    if "nextPageToken" in response:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=response["nextPageToken"]
        )
        response = request.execute()
    else:
        break
result = []
for comment in comments:
    score = analyzer.polarity_scores(comment)
    
    if score['compound'] >= 0.05:
        label = "POSITIVE"
    elif score['compound'] <= -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    
    result.append({'comment': comment, 'sentiment': label})

for r in result:
    print(r['sentiment'], ":", r['comment'])
positive = 0
negative = 0
neutral = 0
for results in result:
    if results['sentiment'] == "POSITIVE":
        positive = positive + 1
    elif results['sentiment'] == 'NEGATIVE':
         negative = negative + 1
    elif results['sentiment'] == 'NEUTRAL':
        neutral = neutral + 1
    else:
        pass
print(results)
print(positive , negative , neutral)
plt.bar(["Positive","Negative","neutral"],[positive,negative,neutral],color=["yellow","red","gray"])
plt.title("YouTube Comment Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")
plt.show()
