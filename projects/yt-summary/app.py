from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

video_id = "dQw4w9WgXcQ"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
text_chunks = []

for entry in transcript:
    line = entry["text"]
    text_chunks.append(line)

full_text = " ".join(text_chunks)

summariser = pipeline("Summarization")

summary_results = summariser(full_text)
summary_text = summary_results[0]["summary_text"]

print("Summary of the video: ")
print(summary_text)