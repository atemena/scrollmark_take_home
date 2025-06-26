from langchain.llms import OpenAI
import pandas as pd
from collections import defaultdict

# LLM-based topic extraction (caption only)
def extract_topic(caption: str, llm=None) -> str:
    if llm is None:
        llm = OpenAI(temperature=0)
    prompt = f"""
    Given the following social media caption, extract the main topic of interest in 3 words or less. Only return the topic phrase.
    Caption: {caption}
    """
    topic = llm(prompt).strip()
    return topic

def aggregate_topic_metrics(df, llm=None):
    df = df.copy()
    # Deduplicate captions and extract topics only once per unique caption
    unique_captions = df["media_caption"].unique()
    caption_to_topic = {}
    for cap in unique_captions:
        print(f"Processing caption: {cap}")
        caption_to_topic[cap] = extract_topic(cap, llm=llm)
    df["topic"] = df["media_caption"].map(caption_to_topic)
    # Robust date parsing
    parsed_dates = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    num_unparseable = parsed_dates.isna().sum()
    if num_unparseable > 0:
        print(f"Warning: {num_unparseable} unparseable timestamps found and excluded from metrics.")
    df["date"] = parsed_dates.dt.date
    df = df.dropna(subset=["date"])  # Exclude rows with unparseable dates
    # For each topic and date, count unique commenters and total comments
    # For MVP, treat comment_text as proxy for commenter (ideally would use user_id)
    grouped = df.groupby(["topic", "date"])
    metrics = grouped.agg(
        engaged_users=("comment_text", "nunique"),
        comment_count=("comment_text", "count")
    ).reset_index()
    return metrics
