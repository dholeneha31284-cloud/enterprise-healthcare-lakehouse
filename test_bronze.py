from src.bronze.bronze_loader import BronzeLoader

loader = BronzeLoader()

bronze_df = loader.load_claims()

print("Rows Loaded:", bronze_df.count())