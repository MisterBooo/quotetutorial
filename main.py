from scrapy.cmdline import execute

import sys
import os

print(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","quotes"])
