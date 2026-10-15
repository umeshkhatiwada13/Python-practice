import pandas as pd

# Load your CSV
df = pd.read_csv("preply_french_tutors_all_pages.csv")

# Convert numeric fields
df['lessons'] = pd.to_numeric(df['lessons'], errors='coerce').fillna(0).astype(int)
df['price'] = df['price'].str.replace('$', '').astype(float)

# Filter for $3 tutors
df_3usd = df[df['price'] == 3.0].copy()

# Fix profile URLs
def fix_url(url):
    if url.startswith("https://preply.comhttps://preply.com"):
        url = url.split("https://preply.com")[-1]
    if not url.startswith("https://preply.com"):
        url = f"https://preply.com{url}"
    return url

df_3usd['profile_url'] = df_3usd['profile_url'].apply(fix_url)

# Sort by lessons descending
df_3usd_sorted = df_3usd.sort_values(by='lessons', ascending=False)



# Save to new CSV
df_3usd_sorted.to_csv(".csv", index=False, encoding='utf-8')

print("Top 3 $3 tutors saved to file")
