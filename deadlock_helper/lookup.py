def class_name_search(entries, class_name):
    for entry in entries:
        if entry.get("class_name") == class_name:
            return entry
    return None