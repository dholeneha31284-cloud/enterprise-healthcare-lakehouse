from src.bronze.bronze_loader import BronzeLoader
from src.validation.validator import Validator

loader = BronzeLoader()

bronze_df = loader.load_claims()

valid_df, invalid_df = Validator.validate_claims(bronze_df)

print("\n========== VALID RECORDS ==========")
valid_df.show(truncate=False)

print("\n========== INVALID RECORDS ==========")
invalid_df.show(truncate=False)

print(f"\nValid Rows   : {valid_df.count()}")
print(f"Invalid Rows : {invalid_df.count()}")