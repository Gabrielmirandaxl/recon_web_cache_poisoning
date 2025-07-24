import argparse
import requests
import sys
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CACHE_HIT_HEADER = 'X-Cache'
CACHE_HIT_VALUES = {'hit', 'h'}
POISON_PARAM = "?cache_poison=1"


def check_url(url: str, total_requests: int = 5) -> Tuple[str, bool]:

    session = requests.Session()
    target_url = url.rstrip('/') + '/' + POISON_PARAM

    try:
        session.get(target_url, verify=False, timeout=10)

        for _ in range(total_requests - 1):
            response = session.get(target_url, verify=False, timeout=10)

            cache_status = response.headers.get(CACHE_HIT_HEADER, '').lower()

            if any(hit_value in cache_status for hit_value in CACHE_HIT_VALUES):
                return url, True

    except requests.exceptions.RequestException:
        return url, False

    return url, False


def process_urls_with_threads(urls: List[str], num_threads: int):

    hits_found = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}

        progress_bar = tqdm(as_completed(future_to_url), total=len(urls), desc="Scanning URLs", unit="url", ncols=80)

        for future in progress_bar:
            url, is_hit = future.result()
            if is_hit:
                hits_found.append(url)

    if hits_found:
        print("\n" + "-" * 50)
        print("✅ Cache Hit Detected on the following URLs:")
        print("-" * 50)
        for url in hits_found:
            print(f"  -> {url}")
    else:
        print("\n" + "-" * 50)
        print("❌ No URLs with a detectable cache hit were found.")
        print("-" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="Web Cache Poisoning Scanner - Checks for 'X-Cache: hit' headers.",
        epilog="Example: python %(prog)s -l urls.txt -t 20"
    )

    parser.add_argument("-u", "--url", type=str, help="Single URL to test.")
    parser.add_argument("-l", "--list", type=str, help="Path to a file with a list of URLs (one per line).")
    parser.add_argument("-t", "--threads", type=int, default=10,
                        help="Number of concurrent threads to use with --list (default: 10).")

    args = parser.parse_args()

    if not args.url and not args.list:
        parser.error("No target specified. Use --url or --list.")
        sys.exit(1)

    if args.url:
        print(f"[*] Checking single URL: {args.url}")
        _, is_hit = check_url(args.url)
        if is_hit:
            print(f"[+] Cache Hit Detected: {args.url}")
        else:
            print("[-] Cache Hit not detected.")

    if args.list:
        try:
            with open(args.list, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]

            if not urls:
                print("[!] The provided list is empty.")
                return

            process_urls_with_threads(urls, args.threads)
        except FileNotFoundError:
            print(f"[!] Error: The file '{args.list}' was not found.")
            sys.exit(1)

if __name__ == "__main__":
    main()