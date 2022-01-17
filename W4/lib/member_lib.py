def check_member(user):
    members = {"_id1": {"account": "test", "pwd": "test"}}
    if user is None:
        return {"status_code": -1}
    if user["account"] == members["_id1"]["account"] and user["pwd"] == members["_id1"]["pwd"]:
        return {"status_code": 1}
    elif user["account"] != members["_id1"]["account"] or user["pwd"] != members["_id1"]["pwd"]:
        return {"status_code": 0}
