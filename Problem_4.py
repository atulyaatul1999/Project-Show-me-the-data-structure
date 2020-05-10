class Group():
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
def is_user_in_group(user, group):
    #Return True if user is in the group,Check the group's immediate visible users
    users = group.get_users()
    if user in users:
        return True
        # Recurse through the group's groups and check if user exists in any
    list = group.get_groups()
    for item in list:
        if is_user_in_group(user, item):
            return True
    return False
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child.add_user("sub_child_user")
child.add_group(sub_child)
parent.add_group(child)
parent.add_user("shaktiman")
print(is_user_in_group("sub_child_user",parent))
# its answer should be True as "sub_child_user" is the user of sub_child which is in the parent's group list
print(is_user_in_group("sub_child_user",sub_child))
# its answer should be True as "sub_child_user" is the user of sub_child
print(is_user_in_group(child,parent))
# its answer should be False as child is not in parent's group list
sub_child2=Group("sub_child2")
sub_child2.add_user("sub_child_user2")
parent.add_group(sub_child2)
print(is_user_in_group("sub_child_user2",child))
# its answer should be False as "sub_child_user2" is not in the user's list of child and the group list of child is also empty
print(is_user_in_group("sub_child_user2",parent))
# its answer should be True as "sub_child_user2" is the user of sub_child2 which is in the parent's group list
