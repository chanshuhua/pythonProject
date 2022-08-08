class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution(ListNode):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # write code here
        pre = head
        temp = head.next
        if head is None:
            return head
        if head.next is None:
            return head
        while head is not None:
            if pre.val == temp.val:
                temp = temp.next
                pre.next = temp
            else:
                pre = pre.next
                temp = temp.next
        return head


if __name__ == '__main__':
    Solution.deleteDuplicates("1,2,2,3")