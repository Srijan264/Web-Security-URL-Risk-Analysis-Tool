import requests
import re
from bs4 import BeautifulSoup


# Function to analyze website risk
def analyze_website(url):

    score = 0
    reasons = []

    # Add https if missing
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Suspicious keywords in URL
    patterns = [
        "free",
        "lottery",
        "winner",
        "prize",
        "gift",
        "offer",
        "freeiphone",
        "kbc",
        "cash"
    ]

    # Check URL for suspicious keywords
    for pattern in patterns:
        if re.search(pattern, url, re.IGNORECASE):
            score += 2
            reasons.append(f"Contains suspicious keyword: {pattern}")

    try:
        # Send request to website
        response = requests.get(url, timeout=5)

        # Check website accessibility
        if response.status_code != 200:
            score += 2
            reasons.append("Website returned an error")

        # Get webpage content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract webpage text
        text = soup.get_text().lower()

        # Common spam words
        spam_words = [
            "winner",
            "claim now",
            "lottery",
            "cash prize",
            "click here",
            "congratulations",
            "urgent"
        ]

        # Check webpage content
        for word in spam_words:
            if word in text:
                score += 1
                reasons.append(f"Page contains: {word}")

        # Count hyperlinks
        links = soup.find_all("a")

        # Too many links can be suspicious
        if len(links) > 100:
            score += 2
            reasons.append("Too many links found")

    except Exception:
        score += 3
        reasons.append("Website could not be reached")

    # Determine risk level
    if score >= 8:
        status = "Potential Spam Website"
        risk = "HIGH"

    elif score >= 4:
        status = "Suspicious Website"
        risk = "MEDIUM"

    else:
        status = "Likely Safe Website"
        risk = "LOW"

    # Display report
    print("\n" + "=" * 40)
    print("      URL RISK ANALYSIS REPORT")
    print("=" * 40)

    print(f"\nWebsite    : {url}")
    print(f"Status     : {status}")
    print(f"Risk Level : {risk}")
    print(f"Spam Score : {score}/10")

    print("\nReasons:")

    if reasons:
        for reason in reasons:
            print(f"✓ {reason}")
    else:
        print("✓ No suspicious activity found")

    print("\nFinal Verdict:")

    if risk == "HIGH":
        print("This website may be unsafe.")

    elif risk == "MEDIUM":
        print("Be careful before sharing personal information.")

    else:
        print("No major security concerns detected.")

    print("\n" + "=" * 40)


# Main program starts here
if __name__ == "__main__":

    print("=" * 40)
    print(" WEB SECURITY & URL RISK ANALYSIS TOOL")
    print("=" * 40)

    # Take URL input from user
    website_url = input("\nEnter Website URL: ")

    # Analyze website
    analyze_website(website_url)
