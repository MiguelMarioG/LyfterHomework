def separate_words (list_words):
    new_list = list_words.split("-")
    return (new_list)


def order_words (joint_list):
    joint_list.sort()
    order_list = "-".join(joint_list)
    return order_list


def main ():
    list_words =  "computer-airplane-function-monitor-train-python-variable-zion"
    joint_list = separate_words (list_words)
    result = order_words(joint_list)
    print(result)


if __name__ == "__main__":
    main()