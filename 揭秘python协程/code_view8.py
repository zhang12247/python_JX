import asyncio
import aiohttp

from bs4 import BeautifulSoup
import time


async def fetch_content(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
    }
    async with aiohttp.ClientSession(
        headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, "lxml")

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find("div", id="showing-soon")
    for each_moive in all_movies.find_all("div", class_="item"):
        all_a_tag = each_moive.find_all("a")
        all_li_tag = each_moive.find_all("li")

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]["href"])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_dates, movie_dates, pages):
        soup_item = BeautifulSoup(page, "lxml")
        img_tag = soup_item.find("img")

        print("{} {} {}".format(movie_name, movie_date, img_tag["src"]))


if __name__ == "__main__":
    print("-------begin--------")
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print("-------end--------")
    print("wall time:{}", end - start)
