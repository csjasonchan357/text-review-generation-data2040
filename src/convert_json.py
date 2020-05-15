""""
Utility for converting JSON-formatted review data into tabular form.
"""
import json
from tqdm import tqdm
from keywords import get_keywords

file_name = "Clothing_Shoes_and_Jewelry_5.json"
col_names = ["id", "text", "rating"]
tsv_name = file_name.replace("json", "tsv")
output = open(tsv_name, 'w')
output.write("\t".join(["id", "rating", "keyword", "text"]))
output.close()

i = 0
with open(file_name) as f:
    for line in tqdm(f, desc="Reading from JSON"):
        # do stuff with this one line
        review = json.loads(line)
        text = review["reviewText"]
        rating = review["overall"]
        keyword = get_keywords(text)
        output = open(tsv_name, 'a')
        output.write("\n")
        output.write("\t".join([str(i), str(rating), keyword, text]))
        output.close()
        i += 1
        # for smaller sets, use:
        # if i >= 25:
        #     break
