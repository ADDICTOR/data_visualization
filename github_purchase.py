"""Shopping in Github"""
import requests
from loguru import logger

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
logger.info(f"Status code: {r.status_code}")

# 将API响应存储到一个变量中
response_dict = r.json()
logger.info(f"Total repositories: {response_dict['total_count']}")

# 处理结果
# logging.info(response_dict.keys())
logger.info(response_dict.keys())

# 搜索有关仓库的信息
repo_dicts = response_dict["items"]
logger.info(f"Repositories returned: {len(repo_dicts)}")

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# logger.info(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     logger.info(key)

logger.info("\nSelected information about all repositories:")
for repo_dict in repo_dicts:
    logger.info(f'Name: {repo_dict["name"]}')
    logger.info(f'Owner: {repo_dict["owner"]["login"]}')
    logger.info(f'Stars: {repo_dict["stargazers_count"]}')
    logger.info(f'Repository: {repo_dict["html_url"]}')
    logger.info(f'Created: {repo_dict["created_at"]}')
    logger.info(f'Updated: {repo_dict["updated_at"]}')
    logger.info(f'Description: {repo_dict["description"]}')