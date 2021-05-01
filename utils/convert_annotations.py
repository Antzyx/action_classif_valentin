import csv
import os
import time
import re
from utils.convertion_functions import convert_form_to_type

path_to_data = "..\\AMI\\amicorpus"
path_to_annotations = "..\\AMI\\manual"
path_to_csv = "..\\AMI\\annotations_csv"


def get_action(action_type_name, elements_to_fetch, optional_elements=(), conversion_function_list=()):
    print("Starting to convert actions of type " + action_type_name)
    if not os.path.exists(os.path.join(path_to_csv, action_type_name)):
        os.makedirs(os.path.join(path_to_csv, action_type_name))
    files = [i for i in os.listdir(os.path.join(path_to_annotations, action_type_name)) if i.endswith("xml")]
    total_fields_detected = dict()
    total_individuals_detected = dict()
    for file in files:

        # Fetch info
        file_path = os.path.join(path_to_annotations, action_type_name, file)
        name = ".".join(file.split(".")[:-2])+".csv"
        lines = open(file_path, "r").readlines()
        actions = []
        for line in lines:
            is_line_valid = True
            for fetch_target in elements_to_fetch:
                if fetch_target not in line:
                    is_line_valid = False
            if is_line_valid:
                action = dict()
                elements = line.split(" ")
                for element in elements:
                    if len(element.split("=")) > 1 and element.split("=")[0]:
                        total_fields_detected[element.split("=")[0]] = 1
                    for fetch_target in elements_to_fetch:
                        if fetch_target in element:
                            decompose = element.split('"')
                            if not len(decompose) == 3 or decompose[-1]:
                                print("Unexpected element in file {} for line :\n{}".format(file, line))
                            action[fetch_target] = decompose[1]
                    for fetch_target in optional_elements:
                        if fetch_target in element:
                            decompose = element.split('"')
                            if not len(decompose) == 3 or decompose[-1]:
                                print("Unexpected element in file {} for line :\n{}".format(file, line))
                            action[fetch_target] = decompose[1]
                actions.append(action)

        # Convert and write info
        with open(os.path.join(path_to_csv, action_type_name, name), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            for action in actions:
                lines_to_write, is_list_valid = convert_element([action], elements_to_fetch, conversion_function_list)
                if is_list_valid:
                    for line_to_write in lines_to_write:
                        csvwriter.writerow(line_to_write)
    print("Fields detected : ", list(total_fields_detected.keys()))
    print("Fields detected : ", list(total_individuals_detected.keys()))
    print("Fields gathered : ", elements_to_fetch + optional_elements)


def convert_element(fetched_elements, mandatory, conversion_function_list):
    list_to_return = []
    is_list_valid = True
    for conversion_function in conversion_function_list:
        fetched_elements = conversion_function(fetched_elements, mandatory)
    for fetched_element in fetched_elements:
        try:
            for field in mandatory:
                list_to_return.append(fetched_element[field])
        except KeyError:
            is_list_valid = False
            print("Missing elements in fetched elements : {}".format(fetched_elements))
    return list_to_return, is_list_valid


def get_annotations(conversion_function_list):
    mandatory = ("starttime", "endtime", "type")
    optional = ()
    get_action("handGesture", mandatory, optional, conversion_function_list=[fuse_point_object,fuse_point_person])
    mandatory = ("starttime", "endtime", "type")
    optional = ("form",)
    get_action("headGesture", mandatory, optional, conversion_function_list=conversion_function_list)
    mandatory = ("starttime", "endtime", "type")
    optional = ()
    get_action("movement", mandatory, optional, conversion_function_list=[fuse_stand])
    mandatory = ("starttime", "endtime", "type")
    optional = ()
    get_action("focus", mandatory, optional, conversion_function_list=[fuse_focus_person,fuse_focus_object])

if __name__ == '__main__':
    time_start = time.time()
    function_list = [convert_form_to_type]
    get_annotations(conversion_function_list=function_list)
    print("Script finished in "+str(time.time()-time_start))
