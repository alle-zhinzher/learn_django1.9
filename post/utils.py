import datetime
import re
import math

from django.utils.html import strip_tags


def count_word(html_string):
    wor_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', wor_string)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    count = count_word(html_string)
    read_time_min = math.ceil(count/200)
    return int(read_time_min)
