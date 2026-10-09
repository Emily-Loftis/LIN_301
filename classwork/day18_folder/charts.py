import re
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt

activity_folder = Path(__file__).resolve().parent
data_folder = activity_folder.parents[1] / "data" / "gutenberg"

# Count words with a dictionary
sentence = "the cat saw the dog and the dog saw the cat"
words = sentence.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print("Sentence counts:", counts)
print("Count of 'the':", counts["the"])

plt.figure()
plt.bar(list(counts.keys()), list(counts.values()))
plt.title("Word Counts: The Cat and the Dog")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(activity_folder / "cat_dog_counts_w_labels.png")
plt.close()

# Read and count Mansfield Park
with open(data_folder / "mansfield_park.txt", "r", encoding="utf-8") as f:
    mansfield_text = f.read()

mansfield_words = re.split(r"[\W]+", mansfield_text.lower())
mansfield_words = [word for word in mansfield_words if word != ""]

mansfield_counts = {}
for word in mansfield_words:
    if word in mansfield_counts:
        mansfield_counts[word] += 1
    else:
        mansfield_counts[word] = 1

print("Fanny count:", mansfield_counts.get("fanny", 0))
print("Unique Mansfield words:", len(mansfield_counts))

top10 = Counter(mansfield_words).most_common(10)
print("Mansfield top 10:", top10)

plt.figure()
plt.bar([pair[0] for pair in top10], [pair[1] for pair in top10])
plt.title("Top 10 Words in Mansfield Park")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(activity_folder / "mansfield_top10.png")
plt.close()

# Filter out common words
stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t"]

content_words = [word for word in mansfield_words if word not in stopwords]
content_top10 = Counter(content_words).most_common(10)
print("Mansfield top 10 content words:", content_top10)

plt.figure()
plt.bar([pair[0] for pair in content_top10],
        [pair[1] for pair in content_top10])
plt.title("Top 10 Content Words in Mansfield Park")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(activity_folder / "mansfield_content_top10.png")
plt.close()

print("Charts saved in:", activity_folder)
# Read Alice and make its words lowercase
with open(data_folder / "alice.txt", "r", encoding="utf-8") as f:
    alice_text = f.read()

alice_list = re.split(r"[\W]+", alice_text.lower())
alice_list = [word for word in alice_list if word != ""]

# Find the top 15 words after filtering stopwords
alice_content = [word for word in alice_list if word not in stopwords]
alice_top15 = Counter(alice_content).most_common(15)

print("Alice top 15 content words:", alice_top15)

alice_labels = [pair[0] for pair in alice_top15]
alice_freqs = [pair[1] for pair in alice_top15]

plt.figure(figsize=(10, 6))
plt.bar(alice_labels, alice_freqs)
plt.title("Top 15 Content Words in Alice in Wonderland")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(activity_folder / "alice_top15.png")
plt.close()
# Comparison:
# Mansfield Park's frequent words include character names such as
# Fanny, Crawford, and Edmund, plus titles like Mr, Miss, and Mrs.
# These suggest a focus on characters and social relationships.
# Alice's frequent words include Alice, little, Queen, went, and
# thought, suggesting a focus on Alice's experiences and adventures.
# Gutenberg and project appear because we haven't removed the
# Gutenberg license text yet.