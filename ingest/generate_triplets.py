import pandas as pd
import os
import csv

# Load cleaned archive file (with nulls dropped and 'description' column renamed)
df = pd.read_csv("C:/ISRO_hackathon/data/isro_archives_updates.csv")

# Define namespaces for structured triplets
ORG_NS = "org/"
MISSION_NS = "mission/"
EVENT_NS = "event/"
DOC_NS = "document/"
DATE_NS = "date/"

triplets = []

for _, row in df.iterrows():
    desc = row["description"].strip().replace("\n", " ")
    title = row["title"].strip().replace(" ", "_")
    subj = EVENT_NS + title

    # has_description
    triplets.append((subj, "has_description", desc))

    # launched_by (if title or description contains ISRO and vehicle)
    if "ISRO" in row["title"] or "ISRO" in desc:
        triplets.append((subj, "conducted_by", ORG_NS + "ISRO"))

    # Attach the date
    if pd.notna(row["date"]):
        triplets.append((subj, "has_date", DATE_NS + row["date"].strip().replace(" ", "_")))

    # Attach document/source link
    if pd.notna(row["url"]):
        doc_id = row["url"].strip().split("/")[-1].replace(".html", "")
        triplets.append((subj, "has_document", DOC_NS + doc_id))

# Save triplets
triplet_df = pd.DataFrame(triplets, columns=["subject", "predicate", "object"])
triplet_df.to_csv("C:/ISRO_hackathon/data/triplets/isro_archives_triplets.csv", index=False, quoting=csv.QUOTE_ALL)

print("Triplets saved in structured format")