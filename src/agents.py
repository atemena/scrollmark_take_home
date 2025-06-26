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
    # Add topic column
    df = df.copy()
    df["topic"] = df["media_caption"].apply(lambda c: extract_topic(c, llm=llm))
    # Convert timestamp to date
    df["date"] = pd.to_datetime(df["timestamp"]).dt.date
    # For each topic and date, count unique commenters and total comments
    # For MVP, treat comment_text as proxy for commenter (ideally would use user_id)
    grouped = df.groupby(["topic", "date"])
    metrics = grouped.agg(
        engaged_users=("comment_text", "nunique"),
        comment_count=("comment_text", "count")
    ).reset_index()
    return metrics
