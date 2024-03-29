
class solution():

    def __init__(self):
        '''
        '''

    def search_target(self, nums:list, target:int)->int:
        '''
        二分查找
        在升序数组{nums}nums 中寻找目标值{target}target，对于特定下标 ii，比较 {nums}[i]nums[i] 和{target}target 的大小
        :return:

        for i in range(len(nums)): for循环中需要增加range作为int的循环体
        '''
        low,high = 0,len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2  # 取整 high+low/2 可能造成溢出？
            midnum = nums[mid]
            if midnum == target:
                return midnum
            elif midnum < target:
                low = mid + 1
            else:
                high = mid - 1
        # 跳出循环
        return -1


class Solution:
    def __init__(self):
        self.array = [0]*100
    def climbStairs(self, n: int) -> int:
        # print(len(self.array))
        if n == 1:
            self.array[1] = 1
            return 1
        if n == 2:
            self.array[2] = 2
            return 2
        if self.array[n]>0:
            return self.array[n]
        return self.climbStairs(n-1) + self.climbStairs(n-2)


if __name__ == '__main__':
    # resp = solution().search_target(nums=[0,1,2,3,4],target=4)
    print(Solution().climbStairs(10))