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
def fuse_stand(fetched_elements, mandatory):
    return_elements = []
    pattern = re.compile("stand_")
    for action in fetched_elements:
        if pattern.match(action["type"]):
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
            new_action["type"] = "stand_up"
        else:
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
        return_elements.append(new_action)
    return return_elements

def fuse_point_object(fetched_elements, mandatory):
    return_elements = []
    pattern = re.compile("point_a")
    for action in fetched_elements:
        if pattern.match(action["type"]):
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
            new_action["type"] = "point_object"
        else:
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
        return_elements.append(new_action)
    return return_elements

def fuse_point_person(fetched_elements, mandatory):
    return_elements = []
    pattern = re.compile("point_p")
    for action in fetched_elements:
        if pattern.match(action["type"]):
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
            new_action["type"] = "point_person"
        else:
            new_action = dict()
            for i in mandatory:
                new_action[i] = action[i]
        return_elements.append(new_action)
    return return_elements

def fuse_focus_person(fetched_elements, mandatory):
  return_elements = []
  for action in fetched_elements:
      if action["type"] == "person":
          new_action = dict()
          for i in mandatory:
              new_action[i] = action[i]
          new_action["type"] = "look_at_person"
      else:
          new_action = dict()
          for i in mandatory:
              new_action[i] = action[i]
      return_elements.append(new_action)
  return return_elements

def fuse_focus_object(fetched_elements, mandatory):
  return_elements = []
  for action in fetched_elements:
      if action["type"] == "place":
          new_action = dict()
          for i in mandatory:
              new_action[i] = action[i]
          new_action["type"] = "look_at_object"
      else:
          new_action = dict()
          for i in mandatory:
              new_action[i] = action[i]
      return_elements.append(new_action)
  return return_elements
