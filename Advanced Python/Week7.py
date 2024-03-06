# def is_palindrome(num):
#     old_num = num
#     new_num = 0
#     while num > 0:
#         new_num = (new_num * 10) + num % 10
#         num = int(num / 10)
#
#     if new_num == old_num:
#         return True
#     return False
#
#
# print(is_palindrome(543345))
#
# roman_to_integer = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
#
#
# def convert_roman_to_integer(roman):
#     final_value = 0
#     roman_array = list(roman)
#     roman_array.reverse()
#     print(roman_array)
#
#     last_value = 0
#     for r in roman_array:
#         curr_val = roman_to_integer[r]
#         if last_value > curr_val:
#             final_value = final_value - curr_val
#         else:
#             final_value = final_value + curr_val
#
#         last_value = curr_val
#     return final_value
#
#
# print(convert_roman_to_integer("III"))
# print(convert_roman_to_integer("LVIII"))
#
# import heapq
#
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def merge_k_lists(lists):
#     # Define a dummy node to serve as the head of the merged list
#     dummy = ListNode()
#     current = dummy
#
#     # Initialize a min-heap
#     heap = []
#
#     # Push the head node of each linked list into the min-heap
#     for head in lists:
#         if head:
#             heapq.heappush(heap, (head.val, head))
#
#     # Continue until the heap is empty
#     while heap:
#         # Pop the node with the smallest value from the heap
#         val, node = heapq.heappop(heap)
#
#         # Append the popped node to the merged list
#         current.next = node
#         current = current.next
#
#         # Move to the next node in the linked list
#         if node.next:
#             heapq.heappush(heap, (node.next.val, node.next))
#
#     # Return the merged list
#     return dummy.next
#
#
# # Convert the input lists of arrays to linked lists
# def array_to_linked_list(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head
#
#
# # Convert the merged linked list to array
# def linked_list_to_array(head):
#     arr = []
#     current = head
#     while current:
#         arr.append(current.val)
#         current = current.next
#     return arr
#
#
# # Example usage:
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
#
# # Convert input lists to linked lists
# linked_lists = [array_to_linked_list(lst) for lst in lists]
#
# # Merge the linked lists
# merged_list = merge_k_lists(linked_lists)
#
# # Convert the merged linked list to array
# result_array = linked_list_to_array(merged_list)
#
# print(result_array)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]


def count_good_subarrays(nums, k):
    def at_most_k(nums, k):
        counter = {}
        left = 0
        result = 0

        for right in range(len(nums)):
            counter[nums[right]] = counter.get(nums[right], 0) + 1

            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

            result += right - left + 1

        return result

    return at_most_k(nums, k) - at_most_k(nums, k - 1)


# Example usage:
nums = [1, 2, 1, 2, 3]
k = 2
print(count_good_subarrays(nums, k))  # Output: 7
