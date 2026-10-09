terms = ["phoneme", "morpheme"]
terms.append("lexeme")
print(terms)

messy = [" Phoneme\n", "MORPHEME ", "  syntax", "Semantics\n"]

clean = []
for term in messy:
    clean.append(term.strip().lower())

print(clean)

clean = [term.strip().lower() for term in messy]
print(clean)

words = ["phoneme", "phrase", "morpheme", "reconstruction", "index"]

shouting = [word.upper() for word in words]
lengths = [len(word) for word in words]
firsts = [word[0] for word in words]

print(shouting)
print(lengths)
print(firsts)

from pathlib import Path

# Locate the data folder relative to this script
data_folder = Path(__file__).resolve().parents[2] / "data" / "gutenberg"

with open(data_folder / "mansfield_park.txt", "r", encoding="utf-8") as f:
    book_lines = f.readlines()

mansfield_cleaned = [line.strip().lower() for line in book_lines]

print("Original lines:", book_lines[100:105])
print("Cleaned lines:", mansfield_cleaned[100:105])

mansfield_nonempty = [line for line in mansfield_cleaned if line != ""]

print("Empty lines removed:", len(mansfield_cleaned) - len(mansfield_nonempty))
# Count words ending in r
items = ["color", "flavour", "theater", "center", "analyze",
         "organize", "favorite", "neighbor", "honor", "catalog",
         "honour", "flavor", "analyse", "flavor", "traveler"]

r_item_count = 0
for item in items:
    if item[-1] == "r":
        r_item_count += 1

print("Words ending in r:", r_item_count)

# Change British spellings
american_spellings = []
for word in items:
    if word.endswith("our"):
        word = word.replace("our", "or")
    elif word.endswith("yse"):
        word = word.replace("yse", "yze")
    american_spellings.append(word)

print("Updated spellings:", american_spellings)

# Split Alice into words, removing punctuation and whitespace
import re

with open(data_folder / "alice.txt", "r", encoding="utf-8") as f:
    alice_text = f.read()

alice_list = re.split(r"[\W]+", alice_text)
alice_list = [word for word in alice_list if word != ""]

print("First 100 Alice words:", alice_list[:100])