import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_content(base_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    visited = set()
    to_visit = [base_url]
    headers = {'User-Agent': 'your-user-agent-string'}

    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"无法检索{url}。错误：{e}")
            continue

        visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else "未找到标题"

        text_content = []
        for paragraph in soup.find_all(['p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            text_content.append(paragraph.text)

        full_text = "\n".join(text_content)

        output_file_path = os.path.join(output_folder, f"{len(visited)}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n")
            f.write("=====================================\n")
            f.write(f"Text Content:\n{full_text}\n\n")

        print(f"已保存从{url}抓取的数据到{output_file_path}")

        for a_tag in soup.find_all('a', href=True):
            next_url = urljoin(base_url, a_tag['href'])

            if base_url in next_url:
                to_visit.append(next_url)

        time.sleep(1)


if __name__ == "__main__":
    base_url = "xxxxxx"
    output_folder = "抓取的页面"
    fetch_content(base_url, output_folder)
