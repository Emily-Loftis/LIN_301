import re
from pathlib import Path

data_folder = Path(__file__).resolve().parents[2] / "data" / "gutenberg"

# While-loop practice: remove trailing punctuation
messy = "Really?!?!"
punct = "?!.,"

while messy and messy[-1] in punct:
    messy = messy[:-1]

print("Cleaned practice word:", messy)

# Read both novels
try:
    with open(data_folder / "frank.txt", "r", encoding="utf-8") as f:
        frank_lines = f.readlines()

    with open(data_folder / "p_and_p.txt", "r", encoding="utf-8") as f:
        pride_lines = f.readlines()
except FileNotFoundError:
    print("Couldn't find a file — check the filename and location.")
    raise SystemExit(1)

# Remove Frankenstein's Gutenberg header and footer
while frank_lines and not frank_lines[0].startswith("*** START"):
    frank_lines = frank_lines[1:]
if not frank_lines:
    raise SystemExit("Frankenstein START marker not found.")
frank_lines = frank_lines[1:]

while frank_lines and not frank_lines[-1].startswith("*** END"):
    frank_lines = frank_lines[:-1]
if not frank_lines:
    raise SystemExit("Frankenstein END marker not found.")
frank_lines = frank_lines[:-1]

# Remove Pride and Prejudice's Gutenberg header and footer
while pride_lines and not pride_lines[0].startswith("*** START"):
    pride_lines = pride_lines[1:]
if not pride_lines:
    raise SystemExit("Pride and Prejudice START marker not found.")
pride_lines = pride_lines[1:]

while pride_lines and not pride_lines[-1].startswith("*** END"):
    pride_lines = pride_lines[:-1]
if not pride_lines:
    raise SystemExit("Pride and Prejudice END marker not found.")
pride_lines = pride_lines[:-1]

# Join the lines, lowercase, and split into words
frank_text = "".join(frank_lines)
pride_text = "".join(pride_lines)

frank_words = re.split(r"[\W]+", frank_text.lower())
frank_words = [word for word in frank_words if word != ""]

pride_words = re.split(r"[\W]+", pride_text.lower())
pride_words = [word for word in pride_words if word != ""]

# Total words, unique words, and full-book TTR
frank_tokens = len(frank_words)
frank_types = len(set(frank_words))
frank_ttr = frank_types / frank_tokens

pride_tokens = len(pride_words)
pride_types = len(set(pride_words))
pride_ttr = pride_types / pride_tokens

# Compare equal-sized samples of 10,000 words
frank_sample = frank_words[:10000]
pride_sample = pride_words[:10000]

frank_ttr_10000 = len(set(frank_sample)) / len(frank_sample)
pride_ttr_10000 = len(set(pride_sample)) / len(pride_sample)

# Average word length using counters
frank_letters = 0
for word in frank_words:
    frank_letters += len(word)
frank_avg_length = frank_letters / frank_tokens

pride_letters = 0
for word in pride_words:
    pride_letters += len(word)
pride_avg_length = pride_letters / pride_tokens

print("\nFrankenstein — Mary Shelley")
print("Total words:", frank_tokens)
print("Unique words:", frank_types)
print("Full-book TTR:", frank_ttr)
print("First 10,000 words TTR:", frank_ttr_10000)
print("Average word length:", frank_avg_length)

print("\nPride and Prejudice — Jane Austen")
print("Total words:", pride_tokens)
print("Unique words:", pride_types)
print("Full-book TTR:", pride_ttr)
print("First 10,000 words TTR:", pride_ttr_10000)
print("Average word length:", pride_avg_length)
# Results:
# Frankenstein: 75,379 total words and 7,037 unique words.
# Pride and Prejudice: 128,755 total words and 7,027 unique words.
#
# Frankenstein has the higher full-book TTR: 0.0934 vs. 0.0546.
# Longer texts tend to have lower TTRs because words repeat more.
#
# Comparing the first 10,000 words is fairer:
# Frankenstein's TTR is 0.2550; Pride and Prejudice's is 0.2267.
# The result did not change. Frankenstein has more vocabulary
# variety in these samples.
#
# Average word length is similar: about 4.41 characters in
# Frankenstein and 4.39 in Pride and Prejudice.