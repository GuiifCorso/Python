import pandas as pd

file_path = "squirrelCensus.csv"

df = pd.read_csv(file_path)

squirrel_colors_counts = df["Primary Fur Color"].value_counts()

new_df = pd.DataFrame(
    {
        "Colors": squirrel_colors_counts.index,
        "Count": squirrel_colors_counts
    }
)

new_df.to_csv("SquirrelColors.csv", index=False)