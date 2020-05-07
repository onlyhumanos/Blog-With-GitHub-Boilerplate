# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/" #如果为其他仓库，改为"/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "进击的普通人"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-05-04T17:04+08:00"
author = "OnlyHumanOS"
email = "jizenghui@outlook.com"
author_homepage = "https://www.imalan.cn"
description = "Our greatest freedom is the freedom to choose our attitude."
key_words = ['Maverick', 'OnlyhumanOS', '进击的普通人', 'blog']
language = 'zh-CN'
external_links = [
    #{
    #    "name": "Maverick",
    #    "url": "https://github.com/AlanDecode/Maverick",
    #    "brief": "🏄‍ Go My Own Way."
    #},
    {
        "name": "Matters",
        "url": "https://matters.news/@whynot",
        "brief": "进击的普通人Matters主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    #{
    #    "name": "Twitter",
    #    "url": "https://twitter.com/AlanDecode",
    #    "icon": "gi gi-twitter"
    #},
    {
        "name": "GitHub",
        "url": "https://github.com/onlyhumanos",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/1805119341/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
