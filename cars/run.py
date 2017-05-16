import subprocess

subprocess.call('scrapy crawl cars_title -o data.json', shell=True)
