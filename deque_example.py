'''
Let’s imagine a situation where we are processing
a large document containing bug reports for an application.
In order to prioritize the most important bugs, we want any normal
bug reports to be appended to the end of the list and higher priority
bugs to be at the front of the list (kind of like a priority list).
As we fix the bugs, they can be removed from the front of the list
'''


'''Problem solved with lists'''

bug_data = []

loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # A list uses the insert method to append to the front
        bug_data.insert(0, bug)
    else:
        bug_data.append(bug)

# A list must provide an index to pop
next_bug_to_fix = bug_data.pop(0)

'''Problem solved with deque'''

from collections import deque

bug_data = deque()

loaded_bug_reports = get_all_bug_reports()

for bug in loaded_bug_reports:
    if bug['priority'] == 'high':
        # With a deque, we can append to the front directly
        bug_data.appendleft(bug)
    else:
        bug_data.append(bug)

# With a deque, we can pop from the front directly
next_bug_to_fix = bug_data.popleft()
