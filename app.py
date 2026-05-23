from flask import Flask, render_template, request, Response
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import io
import html

app = Flask(__name__)
API_KEY = "AIzaSyDhGZEQKDXa1REhw-NvVvP1RLrpLPwXYEg"
analyzer = SentimentIntensityAnalyzer()

stored_results = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    global stored_results
    video_url = request.form["video_url"]

    if "v=" in video_url:
        video_id = video_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[1].split("?")[0]
    else:
        return "Invalid YouTube URL"

    youtube = build("youtube", "v3", developerKey=API_KEY)

    video_response = youtube.videos().list(part="snippet", id=video_id).execute()
    video_title = video_response["items"][0]["snippet"]["title"]
    thumbnail = video_response["items"][0]["snippet"]["thumbnails"]["medium"]["url"]

    yt_request = youtube.commentThreads().list(
        part="snippet", videoId=video_id, maxResults=100
    )
    response = yt_request.execute()

    comments = []
    while True:
        for item in response["items"]:
            raw = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comment = html.unescape(raw)
            comments.append(comment)
        if "nextPageToken" in response:
            yt_request = youtube.commentThreads().list(
                part="snippet", videoId=video_id, maxResults=100,
                pageToken=response["nextPageToken"]
            )
            response = yt_request.execute()
        else:
            break

    positive = 0
    negative = 0
    neutral = 0
    scored = []
    stored_results = []

    for comment in comments:
        score = analyzer.polarity_scores(comment)
        compound = score["compound"]
        if compound >= 0.05:
            label = "POSITIVE"
            positive += 1
        elif compound <= -0.05:
            label = "NEGATIVE"
            negative += 1
        else:
            label = "NEUTRAL"
            neutral += 1
        scored.append({"comment": comment, "sentiment": label, "compound": compound})
        stored_results.append({"comment": comment, "sentiment": label})

    total = len(comments)
    pos_pct = round((positive / total) * 100, 1)
    neg_pct = round((negative / total) * 100, 1)
    neu_pct = round((neutral / total) * 100, 1)

    top_positive = [x["comment"] for x in sorted(scored, key=lambda x: x["compound"], reverse=True) if len(x["comment"]) > 20][:5]
    top_negative = [x["comment"] for x in sorted(scored, key=lambda x: x["compound"]) if len(x["comment"]) > 20][:5]

    if positive > negative and positive > neutral:
        overall = "POSITIVE"
    elif negative > positive and negative > neutral:
        overall = "NEGATIVE"
    else:
        overall = "NEUTRAL"

    return render_template("result.html",
        positive=positive, negative=negative, neutral=neutral,
        total=total, pos_pct=pos_pct, neg_pct=neg_pct, neu_pct=neu_pct,
        top_positive=top_positive, top_negative=top_negative,
        overall=overall, video_title=video_title, thumbnail=thumbnail
    )

@app.route("/download")
def download():
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["comment", "sentiment"])
    writer.writeheader()
    writer.writerows(stored_results)
    output.seek(0)
    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=sentiment_results.csv"})

if __name__ == "__main__":
    app.run(debug=True)