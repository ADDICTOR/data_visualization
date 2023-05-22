import requests
from loguru import logger

from operator import itemgetter


def submission_api(id, dicts):
    url = 'https://hacker-news.firebaseio.com/v0/item/' + \
        str(id) + '.json'
    submission_r =requests.get(url)
    logger.info(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        "title": response_dict["title"],
        "link": "http://news.ycombinator.com/item?id=" + \
            str(id),
        "comments": response_dict.get('descendants', 0)
    }
    dicts.append(submission_dict)


def output_info(dict):
    logger.info(f"\nTitle: {dict['title']}")
    logger.info(f"Discussion link: {dict['link']}")
    logger.info(f"Comments: {dict['comments']}")


@logger.catch
def main():
    logger.add('./log/test.log')
    # 执行API调用并存储响应
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    logger.info(f"Status code: {r.status_code}")

    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # 对每一篇文章，都执行一个API调用
        submission_api(submission_id, submission_dicts)
    logger.info(submission_dicts)

    submission_dicts = sorted(submission_dicts,
        key=itemgetter('comments'),reverse=True)

    for submission_dict in submission_dicts:
        output_info(submission_dict)

if __name__ == "__main__":
    main()