import requests
from bs4 import BeautifulSoup
import csv
import time
import re

BASE_URL = "https://preply.com/en/online/french-tutors"

PARAMS = {
    "priceRange": "3-4",
    "cf": 1,
    "sort": "rating"
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

OUTPUT_FILE = "preply_french_tutors_all_pages.csv"
DELAY = 1.5


def fetch_page(page: int) -> BeautifulSoup:
    params = PARAMS.copy()
    params["page"] = page

    resp = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    return BeautifulSoup(resp.text, "html.parser")


def parse_tutors(soup: BeautifulSoup) -> list[dict]:
    tutors = []

    cards = soup.select("section[data-qa-group='tutor-profile']")

    for card in cards:
        tutor_id = card.get("data-qa-tutor-id")

        name_tag = card.select_one("h4")
        profile_tag = card.select_one("a[href*='/tutor/']")
        price_tag = card.select_one("h4[data-qa-group='tutor-price-value'] span")

        rating_tag = card.select_one("button[class*='RatingIndicator']")
        reviews_text = card.get_text(" ", strip=True)

        lessons = re.search(r"(\d+)\s+lessons", reviews_text)
        students = re.search(r"(\d+)\s+students", reviews_text)
        reviews = re.search(r"(\d+)\s+reviews", reviews_text)

        tutors.append({
            "tutor_id": tutor_id,
            "name": name_tag.get_text(strip=True) if name_tag else None,
            "profile_url": profile_tag["href"] if profile_tag else None,
            "price": price_tag.get_text(strip=True) if price_tag else None,
            "rating": rating_tag.get_text(strip=True) if rating_tag else None,
            "reviews": reviews.group(1) if reviews else None,
            "students": students.group(1) if students else None,
            "lessons": lessons.group(1) if lessons else None,
        })

    return tutors


def scrape_all_pages() -> list[dict]:
    all_tutors = []
    page = 1

    while True:
        print(f"Scraping page {page}...")
        soup = fetch_page(page)
        tutors = parse_tutors(soup)

        if not tutors:
            print("Reached last page.")
            break

        all_tutors.extend(tutors)
        page += 1
        time.sleep(DELAY)

    return all_tutors


def save_csv(data: list[dict], filename: str):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    tutors = scrape_all_pages()
    print(f"Total tutors scraped: {len(tutors)}")

    if tutors:
        save_csv(tutors, OUTPUT_FILE)
        print(f"Saved to {OUTPUT_FILE}")

