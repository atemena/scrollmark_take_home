from langchain.llms import OpenAI
import pandas as pd
from collections import defaultdict

def extract_post_type(caption: str, llm=None) -> str:
    if llm is None:
        llm = OpenAI(temperature=0)
    prompt = f"""
    Given the following social media caption, classify the type of post (e.g., giveaway, lyric quote, lifestyle, product launch, etc.).
    Only return the post type.
    Caption: {caption}
    """
    return llm(prompt).strip()

def aggregate_post_type_metrics(df, llm=None):
    df = df.copy()
    unique_captions = df["media_caption"].unique()
    caption_to_post_type = {}
    for cap in unique_captions:
        print(f"Processing caption: {cap}")
        caption_to_post_type[cap] = extract_post_type(cap, llm=llm)
    df["post_type"] = df["media_caption"].map(caption_to_post_type)
    grouped = df.groupby(["post_type"])
    metrics = grouped.agg(
        comment_count=("comment_text", "count")
    ).reset_index()
    return metrics
