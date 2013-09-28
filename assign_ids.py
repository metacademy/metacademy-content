import os
import sys
import random
import string

ID_LENGTH = 8

def id_file(content_path, tag):
    return os.path.join(content_path, 'concepts', tag, 'id.txt')

def random_id():
    """Generate a random ID for a concept. The IDs are arbitrary, apart from the requirement that they be distinct."""
    return ''.join([random.choice(string.lowercase + string.digits) for i in range(ID_LENGTH)])

def assign_ids(content_path):
    """Assign unique IDs to all of the concepts which don't already have IDs."""
    IGNORE_TAGS = ['.DS_Store', 'ANNOTATED_EXAMPLE']
    nodes_path = os.path.join(content_path, 'concepts')
    tags = os.listdir(nodes_path)
    tags = filter(lambda t: not t in IGNORE_TAGS, tags)

    # read in current ID strings
    ids = set()
    for tag in tags:
        if os.path.exists(id_file(content_path, tag)):
            node_id = open(id_file(content_path, tag)).read().strip()
            ids.add(node_id)
    
    for tag in tags:
        if not os.path.exists(id_file(content_path, tag)):
            new_id = None
            while new_id is None or new_id in ids:
                new_id = random_id()
            open(id_file(content_path, tag), 'w').write(new_id)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        content_path = sys.argv[1]
    else:
        content_path = os.getcwd()
    assign_ids(content_path)
