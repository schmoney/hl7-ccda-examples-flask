#!flask/bin/python
from app.db import db
import os.path
import git
import ipdb
import git
import shutil
from parse_meta_data import parse

LOCAL_EXAMPLES_REPO_DIR = "./ccda_examples_repo"

repo = git.Repo.clone_from("https://github.com/schmoney/C-CDA-Examples.git", LOCAL_EXAMPLES_REPO_DIR)
repo.git.pull("origin", "master")
parse(LOCAL_EXAMPLES_REPO_DIR)
basedir = os.path.abspath(os.path.dirname(__file__))

shutil.rmtree(LOCAL_EXAMPLES_REPO_DIR)
sections = db.sections.find().count()
examples = db.examples.find().count()
print "loaded {} sections and {} examples".format(sections, examples)
