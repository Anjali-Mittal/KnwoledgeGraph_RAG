from ingest.triplets_process import ingest_triplets


path ="C:/ISRO_hackathon/data/triplets/isro_archives_triplets.csv"
dataset_name="ISRO_Archives"
if __name__ == "__main__":
    ingest_triplets(path, dataset_name)