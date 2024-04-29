#在 Kubernetes Github 存储库上创建拉取请求（活动）的用户的详细信息。

import requests  #发送 HTTP 请求以及处理响应

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# 发送 GET 请求，将响应存储在 response 变量中
response = requests.get(url)  

# Only if the response is successful
if response.status_code == 200:
    #response.json()将 JSON 响应转换为字典
    pull_requests = response.json()  

    # 创建了一个空字典，用于存储每个拉取请求的创建者及其数量
    pr_creators = {}

    for pull in pull_requests:
        #从当前拉取请求中提取了创建者的用户名，并将其存储在变量 creator 中
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")