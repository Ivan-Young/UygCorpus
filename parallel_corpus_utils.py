def parallel_corpus_info(path):
    max_len = 0
    min_len = 40
    punctuations_count = {}
    punctuations_filtered = []
    count_1_20 = 0
    count_21_40 = 0
    count_41_60 = 0
    count_61_80 = 0
    count_80_ = 0
    with open(path, "r") as f:
        while True:
            s = f.readline().strip()
            if s is "":
                break
            s_list = s.split(" ")
            len_s = len(s_list)
            if max_len<len_s:
                max_len = len_s
            if min_len>len_s:
                min_len = len_s
            if s[-1] not in punctuations_count.keys():
                punctuations_count[s[-1]] = 1
            else:
                punctuations_count[s[-1]] += 1
            if len_s in range(0, 21):
                count_1_20 += 1
            elif len_s in range(21, 41):
                count_21_40 += 1
            elif len_s in range(41, 61):
                count_41_60 += 1
            elif len_s in range(61, 81):
                count_61_80 += 1
            else:
                count_80_ += 1

    # print(punctuations_count)
    for k, v in punctuations_count.items():
        if v > 500:
            punctuations_filtered.append(k)

    print(punctuations_filtered)


    print("0-20 :" + str(count_1_20))
    print("21-40 :" + str(count_21_40))
    print("41-60 :" + str(count_41_60))
    print("61-80 :" + str(count_61_80))
    print(">80 :" + str(count_80_))

    return max_len, min_len, punctuations_filtered

if __name__ == "__main__":
    parallel_corpus_info("./uy.txt")