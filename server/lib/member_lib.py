def check_member(user):
    members = {"_id1": {"username": "username",
                        "account": "test", "pwd": "test"}}
    if user["account"][0] == "" or user["pwd"][0] == "" :
        return {"status_code": -1}
    if user["account"][0] == members["_id1"]["account"] and user["pwd"][0] == members["_id1"]["pwd"]:
        return {"status_code": 1}
    elif user["account"][0] != members["_id1"]["account"] or user["pwd"][0] != members["_id1"]["pwd"]:
        return {"status_code": 0}
