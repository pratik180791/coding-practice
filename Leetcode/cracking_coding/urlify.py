def _urlify(inp_str):
    spaces = 0
    inp_str = inp_str.strip()

    for i in inp_str:
        if i == " ":
            spaces += 1

    output_arr = [None for _ in range(len(inp_str) + spaces*2)]

    op_len = len(output_arr)-1
    for i in range(len(inp_str)-1, -1, -1):
        if inp_str[i] == " ":
            output_arr[op_len] = "0"
            output_arr[op_len-1] = "2"
            output_arr[op_len-2] = "%"
            op_len -= 3
        else:
            output_arr[op_len] = inp_str[i]
            op_len-=1
    return "".join(output_arr)


def urlify(inp_str):
    spaces = 0
    inp_str = inp_str.strip()

    for i in inp_str:
        if i == " ":
            spaces += 1

    output_arr = [None for _ in range(len(inp_str) + spaces*2)]

    op_len = 0
    for i in range(len(inp_str)):
        if inp_str[i] == " ":
            output_arr[op_len] = "0"
            output_arr[op_len+1] = "2"
            output_arr[op_len+2] = "%"
            op_len += 3
        else:
            output_arr[op_len] = inp_str[i]
            op_len+=1
    return "".join(output_arr)

ip = "Mr John Smith   "
op = urlify(ip)
print(op)
