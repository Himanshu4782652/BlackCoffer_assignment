import pandas as pd
from data_extraction import extract_article
from text_analysis import analyze_text


def main():
    # Read input from Excel file
    input_data = pd.read_excel("data/Input.xlsx")

    # Iterate over URLs and extract articles
    results_df = pd.DataFrame()
    for index, row in input_data.iterrows():
        url = row["URL"]
        article_title, article_text = extract_article(url)

        # Analyze article text and calculate variables
        results = analyze_text(article_text)

        # Append results to a DataFrame
        results_df = results_df.append(results, ignore_index=True)

    # Save results to Excel file
    results_df.to_excel("data/Output.xlsx", index=False)


if __name__ == "__main__":
    main()
