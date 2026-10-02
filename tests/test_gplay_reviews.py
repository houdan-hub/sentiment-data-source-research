"""
Google Play Reviews Feasibility Test
Run this on your local machine (US IP) to test Google Play reviews collection.

Usage:
    pip install google-play-scraper
    python test_gplay_reviews.py

Output:
    Prints test results and saves to gplay_results.json
"""
import time
import json
from datetime import datetime
from google_play_scraper import Sort, reviews

# Test apps across different categories
TEST_APPS = [
    {"id": "com.whatsapp", "name": "WhatsApp", "category": "Social"},
    {"id": "com.spotify.music", "name": "Spotify", "category": "Music"},
    {"id": "com.king.candycrushsaga", "name": "Candy Crush Saga", "category": "Game"},
    {"id": "com.google.android.apps.maps", "name": "Google Maps", "category": "Navigation"},
]

def test_app(app_id, app_name, category):
    """Test fetching reviews for one app"""
    result = {
        "app": app_name,
        "category": category,
        "app_id": app_id,
    }

    # Fetch 20 reviews, newest first
    start = time.time()
    try:
        review_list, token = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=20,
        )
        elapsed = time.time() - start

        result["status"] = "success"
        result["reviews_fetched"] = len(review_list)
        result["response_time_sec"] = round(elapsed, 2)

        if review_list:
            # Analyze scores
            scores = [r.score for r in review_list]
            contents = [r.content for r in review_list if r.content]
            result["avg_score"] = round(sum(scores) / len(scores), 2)
            result["score_distribution"] = {s: scores.count(s) for s in sorted(set(scores))}
            result["avg_content_length"] = round(sum(len(c) for c in contents) / len(contents), 0)
            result["reviews_with_dev_reply"] = sum(1 for r in review_list if r.replyContent)

            # Save sample review
            r = review_list[0]
            result["sample_review"] = {
                "userName": r.userName,
                "score": r.score,
                "content": r.content[:200] if r.content else "",
                "at": str(r.at),
                "thumbsUpCount": r.thumbsUpCount,
                "reviewCreatedVersion": r.reviewCreatedVersion,
                "replyContent": r.replyContent[:100] if r.replyContent else None,
            }

            # Test pagination
            time.sleep(2)
            start2 = time.time()
            page2, _ = reviews(app_id, continuation_token=token, count=20)
            elapsed2 = time.time() - start2
            result["page2_reviews"] = len(page2)
            result["page2_time_sec"] = round(elapsed2, 2)

    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)

    return result


def main():
    print(f"Google Play Reviews Test — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    all_results = []
    for app in TEST_APPS:
        print(f"\nTesting: {app['name']} ({app['category']})...")
        r = test_app(app["id"], app["name"], app["category"])
        all_results.append(r)

        if r["status"] == "success":
            print(f"  OK: {r['reviews_fetched']} reviews in {r['response_time_sec']}s")
            print(f"  Avg score: {r.get('avg_score', 'N/A')}, Avg length: {r.get('avg_content_length', 'N/A')} chars")
        else:
            print(f"  ERROR: {r.get('error', 'unknown')}")

        time.sleep(3)  # Be polite between apps

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for r in all_results:
        if r["status"] == "success":
            print(f"  {r['app']}: {r['reviews_fetched']} reviews, {r['response_time_sec']}s, avg {r['avg_score']}★")
        else:
            print(f"  {r['app']}: FAILED — {r.get('error', '')}")

    # Save
    with open("gplay_results.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, default=str)
    print("\nResults saved to gplay_results.json")
    print("Share this file with your team to document the test.")


if __name__ == "__main__":
    main()
