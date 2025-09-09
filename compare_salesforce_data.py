import pandas as pd

source_data = pd.read_csv("Financial_Sample_2.csv")
target_data = pd.read_csv("Financial_Sample.csv")
print("Script started")  

# Find common columns in both DataFrames
common_columns = list(set(source_data.columns) & set(target_data.columns))
# Merge on 'Id' to find differences
# comparison = source_data.merge(target_data, on=['IF_0', 'Segment2', 'Country', 'Product',
#                                                 'Discount Band', 'Units Sold', 
#                                                 'Manufacturing Price', 'Sale Price'], how='outer', indicator=True)
comparison = source_data.merge(
    target_data, on=common_columns, how="outer", indicator=True, suffixes=("_source", "_target")
)
mismatched_records = comparison[comparison['_merge'] != 'both']
mismatched_records.to_csv("mismatched_records.csv", index=False)


# Print summary
print(f"Total records in Source Org: {len(source_data)}")
print(f"Total records in Target Org: {len(target_data)}")
print(f"Discrepancies found: {len(mismatched_records)}")

