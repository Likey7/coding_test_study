
def max_group(people):
    """
    Parameters:
    people (list): input list of int
    group (int): 만들어진 그룹의 수
    num (int): 들어갈 수 있는 사람의 수
    size (int): 그룹을 만들기 위해 필요한 사람의 수

    Returns:
    int: group.
    """
    people.sort()
    group = 0
    num = 1
    for i in people:
        size = people[i]
        if size == num:
            group += 1
            num = 1
        else:
            num += 1
    return group

print(max_group([1,1,2,2,3,4,4,4,5]))