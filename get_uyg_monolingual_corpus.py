import re
from urllib import request
from pyquery import PyQuery as pq
from parallel_corpus_utils import parallel_corpus_info

headers = {
            "Host":"uyghur.people.com.cn",
            "Cookie":"wdcid=62baa762b4832f8a; wdlast=1545032438; wdses=4169b7d11f9e8cf1",
            "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
            "Referer":"http://uyghur.people.com.cn/"
        }


def get_urls():
    url_suffixes = []
    url = "http://uyghur.people.com.cn/"
    count = 0
    try:
        req = request.Request(url, headers=headers)
        page = request.urlopen(req).read()
        doc = pq(page)
        tag_li_s = doc("ul li")
        for i in range(len(tag_li_s)):
            for j in range(len(tag_li_s.eq(i).children())):
                suffix = tag_li_s.eq(i).children().eq(j).attr("href")
                print(suffix)




    except Exception as e:
        print(e)








def main():
    # MAX_LEN, MIN_LEN, punctuations = parallel_corpus_info("./uy.txt")

    get_urls()






    # try:
    #     url = "http://uyghur.people.com.cn/155989/15747053.html"
    #     req = request.Request(url, headers=headers)
    #     page = request.urlopen(req).read()
    #     doc = pq(page)
    #     contents = doc("#zoom").text()
    #
    #     sentences_list = contents.split(".")
    #     for s in sentences_list:
    #         print(s)
    #
    # except Exception as e:
    #     print(e)

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