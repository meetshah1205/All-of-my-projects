import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}
    
    def shorten_url(self, original_url):
        # Create a unique hash for the original URL
        url_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]

        # Check if the hash is already in use
        if url_hash in self.url_map:
            # If it's in use, generate a new hash (you can customize this as needed)
            url_hash = hashlib.md5(original_url.encode()).hexdigest()[6:12]

        # Store the original URL and its shortened version in the mapping
        self.url_map[url_hash] = original_url

        # Return the shortened URL
        return f"your-short-url.com/{url_hash}"

    def resolve_url(self, short_url):
        # Extract the hash from the short URL
        url_hash = short_url.split("/")[-1]

        # Check if the hash is in the mapping
        if url_hash in self.url_map:
            return self.url_map[url_hash]
        else:
            return "URL not found"

# Example usage
url_shortener = URLShortener()
original_url = "https://chat.openai.com/c/2df87f0f-938f-430d-bf12-79ea50b306cc"
short_url = url_shortener.shorten_url(original_url)
print(f"Shortened URL: {short_url}")
resolved_url = url_shortener.resolve_url(short_url)
print(f"Resolved URL: {resolved_url}")
