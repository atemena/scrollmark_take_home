import argparse
import os
from dotenv import load_dotenv
from src.ingest import load_comments_csv
from src.db import init_db, insert_data
from src.agents import aggregate_topic_metrics
from src.report import generate_report

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Social Media Topic Metrics")
    parser.add_argument("--csv", type=str, default="data/example.csv", help="Path to CSV file")
    parser.add_argument("--db", type=str, default="data/example.sqlite", help="Path to SQLite DB file")
    parser.add_argument("--report", type=str, default="report.md", help="Path to output Markdown report")
    args = parser.parse_args()

    print(f"Loading data from {args.csv}...")
    df = load_comments_csv(args.csv)

    print(f"Initializing DB at {args.db} and inserting data...")
    init_db(args.db)
    insert_data(args.db, df)

    print("Extracting topics and aggregating metrics...")
    metrics = aggregate_topic_metrics(df)
    print(metrics)

    print(f"Generating Markdown report at {args.report}...")
    generate_report(metrics, args.report)
    print(f"Report saved to {args.report}")

if __name__ == "__main__":
    main()
