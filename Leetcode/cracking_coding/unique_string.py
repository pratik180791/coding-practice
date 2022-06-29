def unique_str(inp_str:str) -> bool:
    res = {}
    if not inp_str:
        return False
    for i in inp_str:
        if i in res:
            return False
        res[i] = 1
    return True

op = "a"
op = "aabb"
sol = unique_str(op)
print(sol)
