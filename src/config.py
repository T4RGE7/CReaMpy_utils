from ast import literal_eval
import sys
import os

src_git = "src_git"
output_folder="output_folder"
wiki_folder="wiki_folder"
html_folder="html_folder"
image_folder="images"
tar_file="tar_file"
tree_file="tree_file"
template_folder="template_folder"

def get_locs():
    return {
            src_git: "/home/build/CReaMpy_src",
            output_folder: "/home/build",
            wiki_folder: "CRM",
            html_folder: "CRM_html",
            image_folder:"http://192.168.1.4/CRM/images/",
            tar_file:"CRM_latest.tar.gz",
            tree_file: "tree/wiki.tree",
            template_folder: "template",
    }

def our_loc():
    encoding = sys.getfilesystemencoding()
    loc = sys.executable if hasattr(sys, "frozen") else __file__
    return os.path.dirname(unicode(loc, encoding))

def get_updated_locs(loc):
    path = os.path.join(loc if loc is not None else our_loc(), "local.config")
    to_return = get_locs()
    if os.path.exists(path):
        with open(path, "r") as f:
            config = literal_eval("".join(f.readlines()))
            for (name, loc) in config:
                to_return[name] = loc
    return to_return

def join_list(locs, to_join):
    reduce_list = map(lambda a: locs[a], to_join)
    return os.path.join(*reduce_list)

if __name__ == "__main__":
    print get_updated_locs(our_loc())
