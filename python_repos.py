"""Github上star最多的项目"""
import requests
import pygal
from loguru import logger
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
names, plot_dicts = [], []
repo_dicts = response_dict["items"]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('./images/python_repos.svg')

# repo_dicts = response_dict["items"]
# logger.info(f"Repositories returned: {len(repo_dicts)}")

# # 研究第一个仓库
# # repo_dict = repo_dicts[0]
# # logger.info(f"\nKeys: {len(repo_dict)}")
# # for key in sorted(repo_dict.keys()):
# #     logger.info(key)

# logger.info("\nSelected information about all repositories:")
# for repo_dict in repo_dicts:
#     logger.info(f'Name: {repo_dict["name"]}')
#     logger.info(f'Owner: {repo_dict["owner"]["login"]}')
#     logger.info(f'Stars: {repo_dict["stargazers_count"]}')
#     logger.info(f'Repository: {repo_dict["html_url"]}')
#     logger.info(f'Created: {repo_dict["created_at"]}')
#     logger.info(f'Updated: {repo_dict["updated_at"]}')
#     logger.info(f'Description: {repo_dict["description"]}')