def is_right_brackets_order(s):
    if len(s) % 2 == 1:
        return "no"
    opened_brackets = "([{"
    st = []
    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for i in s:
        if i in opened_brackets:
            st.append(i)
        else:
            try:
                if bracket_pairs[i] != st.pop():
                    return "no"
            except IndexError:
                return "no"
    return "yes"
print(is_right_brackets_order(input()))