from task import Task
# from task import show_tree_up
from task import show_tree_down


first = Task('#1')
second = Task('#2')
third = Task('#3')
four = Task('#4')



# 2nd depends on 3rd
second.set_downstream(third)
second.set_stage('0.1')

# 3rd depends on 1st
third.set_downstream(first)
third.set_stage('0.2')

# first stage 0.3
first.set_stage('0.3')

# 4th depends on 1st
four.set_downstream(first)


third.check_order()

show_tree_down(second, second.name)
# show_tree_down(four, four.name)
