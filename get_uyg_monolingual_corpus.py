import re
import json
from urllib import request
from pyquery import PyQuery as pq
from parallel_corpus_utils import parallel_corpus_info



headers = {
            "Host": "uyghur.people.com.cn",
            "Cookie": "wdcid=62baa762b4832f8a; wdlast=1545032438; wdses=4169b7d11f9e8cf1",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
            "Referer": "http://uyghur.people.com.cn/"
        }

suffix_dict = {}
# used for new indexes
suffix_dict_temp = {}
pattern1 = re.compile(r"/\d+/\d+.html")
pattern2 = re.compile(r"/\S+\d/index.html")
pattern3 = re.compile(r"\S+\d\S*")

#get "/******/index.html"
def get_url_suffixes():
    url_suffixes = []
    url = "http://uyghur.people.com.cn/"
    try:
        req = request.Request(url, headers=headers)
        page = request.urlopen(req).read()
        doc = pq(page)
        tag_li_s = doc("ul li")
        for i in range(len(tag_li_s)):
            for j in range(len(tag_li_s.eq(i).children())):
                suffix = tag_li_s.eq(i).children().eq(j).attr("href")
                temp = check_suffixes(suffix)
                if temp and temp not in url_suffixes:
                    url_suffixes.append(temp)
        url_suffixes.append("/311301/311302/index.html")
        print(url_suffixes)
        for suff in url_suffixes:
            suffix_dict[suff] = []
        return url_suffixes

    except Exception as e:
        print(e)


#input "/******.index", get "/******/******.html"
def get_news_url(url_suffix):
    url = "http://uyghur.people.com.cn" + url_suffix
    other_suffix = []
    complete_suffixes = []
    try:
        req = request.Request(url, headers=headers)
        page = request.urlopen(req).read()
        doc = pq(page)
        tag_li_s = doc("ul li")
        for i in range(len(tag_li_s)):
            for j in range(len(tag_li_s.eq(i).children())):
                t = tag_li_s.eq(i).children().eq(j).attr("href")
                if t is None:
                    continue
                if re.match(pattern2, t) and t not in suffix_dict.keys():
                    suffix_dict_temp[t] = []
                if re.match(pattern1, t):
                    l = '/' + t.split("/")[1] + '/index.html'
                    if l not in suffix_dict.keys():
                        suffix_dict_temp[l] = [t]
                    else:
                        if t not in suffix_dict[l]:
                            suffix_dict[l].append(t)

        return complete_suffixes

    except Exception as e:
        print(e)


#check
def check_suffixes(suffix):
    if not suffix:
        print("Before: " + "None")
    else:
        print("Before: " + suffix)
    if not suffix or len(suffix) > 30 or not re.match(pattern3, suffix):
        print("After: " + "None")
        return None
    if re.match(pattern2, suffix):
        print("After: " + suffix)
        return suffix
    if re.match(pattern1, suffix):
        l = '/' + suffix.split("/")[1] + '/index.html'
        print("After: " + l)
        return l

#use url to get the news.
def get_news_contents(url):
    try:
        url = "http://uyghur.people.com.cn/155989/15747053.html"
        req = request.Request(url, headers=headers)
        page = request.urlopen(req).read()
        doc = pq(page)
        title = doc("#p_title").text()
        contents = doc("#zoom").text()


    except Exception as e:
        print(e)


#slice up the sentences to right length
def slice_contents(contents, punctuations):
    assert isinstance(contents, str)
    assert isinstance(punctuations, list)
    sentences_list = contents.split(".")
    print(len(sentences_list))
    for s in sentences_list:
        if len(s.split(" ")) > 40:
            for i in range(4):
                # if s.find("i") in
                continue


def main():
    MAX_LEN, MIN_LEN, punctuations = parallel_corpus_info("./uy.txt")
    # get_url_suffixes()
    # for k in suffix_dict.keys():
    #     get_news_url(k)
    # print(suffix_dict)
    # with open("uy_url_suffixes.json", "w") as f:
    #    f.write(json.dumps(suffix_dict))

    with open("./uy_url_suffixes.json", "r") as f:
        suffixes = json.loads(f.readline())
    assert isinstance(suffixes, dict)
    # for key, suffix_list in suffixes.items():
    #     for suffix in suffix_list:
    #         continue
    get_news_contents("")





    # f = open("./test.txt", "w")
    # f.write(contents)
    # f.close()


    #
    # urls = doc('li')
    #
    # print(type(urls.children().eq(0).text()))
    #
    # s = urls.children().eq(0)
    # print(s)
    # u = s.encode("utf-8").decode("gb2312")
    # print(u)
    # d = s.encode("utf-8").decode("unicode-escape")
    # print(d)


if __name__ ==  "__main__":
    main()