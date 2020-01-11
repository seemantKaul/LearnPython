def rule1(list_password):
    if sorted(list_password) == list_password:
        return True
    else:
        return False


def rule2(list_password):
    # rev_list_password = list_password
    for i in range(len(list_password) - 1):
        if list_password[i] == list_password[i + 1]:
            # if rev_list_password[i] != rev_list_password[i+2]:
            if list_password.count(list_password[i]) == 2:
                return True
            # else:
            # return False
    # print(i)
    # if rev_list_password[i+1] == rev_list_password[i+2] and rev_list_password[i+1] != rev_list_password[i]:
    # return True
    # else:
    return False


if __name__ == "__main__":
    # Configurations
    MIN_RANGE = 136760
    MAX_RANGE = 595730
    # MIN_RANGE = 100
    # MAX_RANGE = 999
    list_valid_password = list()
    for passw in range(MIN_RANGE, MAX_RANGE):
        # print(f"Testing {passw}", end=" ")
        list_pass = list(str(passw))
        list_password = list(map(int, list_pass))

        if rule1(list_password):
            # print("Rule1 OK", end=" ")
            if rule2(list_password):
                list_valid_password.append(passw)
                # print("Rule2 OK")
            else:
                # print(f"Testing {passw}", end=" ")
                # print("Rule2 FAILED")
                pass

        else:
            pass
            # print("Rule1 FAILED")
    password_count = len(list_valid_password)
    print(f"There are {password_count} Valid passwords")
    # print(list_valid_password)
