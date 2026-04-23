# week09-5.py 學習計畫 Linked List 第1題 Medium
# LeetCode 2059. Minimum Operations to Convert Number
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None

        prev = fast = slow = head # fast 兔子 slow 烏龜 一開始都在最前面
        while fast != None and fast.next != None: # 兔子還沒到終點
            fast = fast.next.next #　兔子跳２格
            prev = slow # 烏龜在走之前，先記下來下一個的位置
            slow = slow.next # 烏龜走一格
        # print(slow.val) # 當兔子到終點時，烏龜在中間
        prev.next = slow.next
        return head
