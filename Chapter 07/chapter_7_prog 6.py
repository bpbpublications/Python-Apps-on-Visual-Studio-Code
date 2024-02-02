from multiprocessing.pool import ThreadPool
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests

url_list = ['india', 'python', 'programmers', 'swapnil', 'hyderabad', 'tiger',
            'peacock', 'guido%20van%20rossum']

def is_wiki_page_exist(url, time=10):
    response = requests.get(url=url, timeout=time)
    page_status = "unknown"
    if response.status_code == 200:
        page_status = "Exists"
    elif response.status_code == 404:
        page_status = "Can not find"

    return url + " - " + page_status

print("Method 1: Running without threads")
method1_start = time.time()
for url in url_list:
    print(is_wiki_page_exist(
        url="https://en.wikipedia.org/wiki/" + url))
method1_end = time.time()
print("Time taken without threads:", method1_end - method1_start)

print("Method 2: Using ThreadPoolExecutor")
method2_start = time.time()
with ThreadPoolExecutor() as executor:
    futures = []
    for url in url_list:
        urls = "https://en.wikipedia.org/wiki/"+url
        futures.append(executor.submit(is_wiki_page_exist, url=urls))
    for future in as_completed(futures):
        print(future.result())
method2_end = time.time()
print("Time taken with ThreadPoolExecutor:", method2_end - method2_start)
print("Method 3: Using ThreadPool")
method3_start = time.time()
# create the thread pool: count exists
with ThreadPool(len(url_list)) as pool:
    # creating the arguments
    urls = []
    for url in url_list:
        urls.append("https://en.wikipedia.org/wiki/"+url)
    args = [(url, 10) for url in urls]
    # dispatch all tasks
    results = pool.starmap(is_wiki_page_exist, args)
    # report results in order
    for result in results:
        print(result)

method3_end = time.time()
print("Time taken with ThreadPool:", method3_end - method3_start)