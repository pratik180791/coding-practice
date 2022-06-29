s = "(]"
s = "()[]{}"
s = "(]"
s = "(])"
def valid_params(s:str):
    #print(s)
    param_list = []
    param_mapper = {")":"(", "]":"[", "}":"{"}
    for i in s:
        if i in ("[", "(", "{"):
            param_list.append(i)
        elif i in ("]", ")", "}"):
            if not param_list:
                return False
            elif param_mapper.get(i) == param_list[-1]:
                param_list.pop()
            elif param_mapper.get(i) != param_list[-1]:
                return False
    if param_list:
        return False
    return True
    #print(param_list)

valid_params(s)
