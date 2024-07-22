import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_video_links(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        iframes = soup.find_all('iframe')
        video_links = [iframe.get('src') for iframe in iframes if iframe.get('src')]
        return video_links
    else:
        print(f"Failed to retrieve content from {url}")
        return []

def convert_video_link(link):
    if "dood.la/e/" in link:
        return link.replace("dood.la/e/", "dood.la/d/")
    return link

def extract_download_link(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    target_div = soup.find('div', class_='the_box')
    if target_div:
        link = target_div.find('a', href=True)
        if link:
            return link['href']
    return None

def get_video_download_url(page_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(page_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        download_link_tag = soup.find('a', href=True, class_='btn btn-primary d-flex align-items-center justify-content-between')
        if download_link_tag:
            relative_url = download_link_tag.get('href')
            download_url = urljoin(page_url, relative_url)
            return download_url
    return None

def get_download_link(video_download_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(video_download_url, headers=headers)
    if response.status_code == 200:
        return extract_download_link(response.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    url = input("MASUKKAN URL VIDEO: \n")
    video_links = fetch_video_links(url)
    if video_links:
        for link in video_links:
            converted_link = convert_video_link(link)
            print(f"Link Video yang diubah:\n {converted_link}\n")

            video_download_url = get_video_download_url(converted_link)
            link_download = get_download_link(video_download_url)
            if video_download_url:
                print(f"URL download video:\n {video_download_url}\n")
                print(f"LINK DOWNLOAD:\n {link_download}\n")
                break
            else:
                print("URL download tidak ditemukan")
    else:
        print("Tidak ada link video yang ditemukan pada URL yang diberikan")
