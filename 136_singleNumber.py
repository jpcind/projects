class Solution:
    def singleNumber(self, nums: list[int]):
        my_arr = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    my_arr.append(nums[i])
        new_list = [i for i in nums if i not in my_arr]
        return new_list[0]
def main():
    my_sol = Solution()
    print(my_sol.singleNumber([2, 2, 3, 1, 3]))
main()
