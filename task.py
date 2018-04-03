"""
Down Stream Task:
    These are tasks that need to be completed
    before this task can start.
    These are tasks that this task depends on.

Up Stream Task:
    These are tasks that will be able to be
    started once this task is completed.
    They are tasks that depend on it.
"""
from distutils.version import StrictVersion


def show_tree_down(task, root_name=None):
    if task.name == root_name:
        root_name = task.name + ' ' + str(task.stage)
        print("\n\t{} <-- Query Downstream\n\t|".format(root_name))
    elif task.downstream:
        task.name = task.name + ' ' + str(task.stage)
        print("\t{}\n\t|".format(task.name))
    else:
        task.name = task.name + ' ' + str(task.stage)
        print("\t{} <- Lowest".format(task.name))
    if task.downstream:
        show_tree_down(task.downstream, root_name)


""" Need to solve multiple upstream tasks."""
# def show_tree_up(task, root_name=None):
    # if task.upstream:
        # for u in task.upstream:
        # show_tree_up(u, root_name)
    # print(task.name)


class Task:
    upstream = None
    downstream = None
    stage = None
    def __init__(task, name):
        task.name = name

    def set_upstream(task, upstream):
        task.upstream = upstream

    def set_downstream(task, downstream):
        if task != downstream:
            task.downstream = downstream
            downstream.set_upstream(task)
        else:
            print("Can't set task dependant on itself!")

    def set_stage(task, stage):
        task.stage = StrictVersion(stage)

    def check_order(task):
        if task.stage > task.upstream.stage:
            print("Upstream task exists at a lower stage.")
        if task.stage < task.downstream.stage:
            print("Downstream task exists at a higher stage.")
