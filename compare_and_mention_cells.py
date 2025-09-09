import pandas as pd

source_file = "extract.xlsx"
target_file = "extract1.xlsx"
comparison_file = "Comparison_File_With_Cells_1.xlsx"

df_source = pd.read_excel(source_file)
df_target = pd.read_excel(target_file)


common_columns = list(set(df_source.columns) & set(df_target.columns))


df_source = pd.read_excel(source_file)
df_target = pd.read_excel(target_file)

for col in common_columns:
    try:
        # Convert both columns to string type if they contain mixed types
        df_source[col] = df_source[col].astype(str)
        df_target[col] = df_target[col].astype(str)
    except Exception as e:
        print(f"Error converting column {col}: {e}")
        
        
df_comparison = pd.DataFrame(columns=df_target.columns)
df_comparison["Mismatch Location"] = ""

for col in common_columns:
    for idx in range(len(df_target)):
        source_value = df_source[col][idx] if idx < len(df_source) else None
        target_value = df_target[col][idx] if idx < len(df_target) else None

        if pd.notna(target_value) and pd.notna(source_value) and target_value != source_value:
            df_comparison.at[idx, col] = target_value  
            col_letter = chr(65 + df_target.columns.get_loc(col))  
            current_location = df_comparison.at[idx, "Mismatch Location"]
            if pd.isna(current_location):  
                current_location = ""  
            df_comparison.at[idx, "Mismatch Location"] = current_location + f"{col_letter}{idx+2}, "

df_comparison["Mismatch Location"] = df_comparison["Mismatch Location"].str.rstrip(", ")
columns_order = ["Mismatch Location"] + [col for col in df_comparison.columns if col != "Mismatch Location"]
df_comparison = df_comparison[columns_order]

df_comparison.to_excel(comparison_file, index=False)

