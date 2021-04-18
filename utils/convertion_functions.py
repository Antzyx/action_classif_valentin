def convert_form_to_type(fetched_elements, mandatory):
    return_elements = []
    for action in fetched_elements:
        if "form" in list(action.keys()) and action["form"] in ["nod", "shake"]:
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
            new_action["type"] = action["form"]
        else:
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
        return_elements.append(new_action)
    return return_elements
