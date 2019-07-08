import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print("Read {} from {}".format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        "http://devops.zhonganonline.com/uiv3/project/detail/4902",
        "http://devops.zhonganonline.com/uiv3/appTerminal/test/fcp/fcp-za-renhang-credit-front-mics/fcp-za-renhang-credit-front-mics-308349-7cf5d468cb-bcd4j",
        "http://4902-fcp-other-jrfed-financial-data.test.za.biz/renhangcheckfilenew.html",
        "http://idb.zhonganonline.com/?ticket=ST-37047231-QDdudghegU5u4VfVssMrrsTHcRSZaB7Hznj",
        "https://account.geekbang.org/dashboard/buy",
        "https://time.geekbang.org/column/article/102562",
        "http://4902-fcp-other-jrfed-financial-data.test.za.biz/renhangcheckfile.html",
        "https://www.baidu.com/s?ie=UTF-8&wd=baidu1",
        "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%AF%8D%E5%BA%93&oq=arts&rsv_pq=843974c20008008a&rsv_t=a04f7OOAtBbthWCkB3mPnv9n%2FIFbOKxfjU4vWt3kBl47oJRJaTpxV4lHBz4&rqlang=cn&rsv_enter=1&inputT=2352&rsv_sug3=16&rsv_sug1=23&rsv_sug7=100&bs=arts",
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print("Download {} sites in {} seconds".format(len(sites), end_time - start_time))


if __name__ == "__main__":
    main()
