grep -h -E "^http:\/\/.*\.yuku.com" bingscrape-raw.txt | cut -d / -f 3 | sort -u > bingscrape-parsed.txt
