def lucky_winner(file_name, my_id):

    text = open(file_name, "r")
    found = False
    is_listed = ""
    
    for line in text:
        if my_id in line:
            is_listed = "YES"
            found = True

    if not found:
        is_listed = "NO"

    text.close()

    return is_listed


print(lucky_winner("lucky_ids.txt", "001090464"))  # Test 1 success
print(lucky_winner("lucky_ids.txt", "001068766"))  # Test 2 success
print(lucky_winner("lucky_ids.txt", "223"))  # Test 3 success
print("EXTRAAAAAA")
