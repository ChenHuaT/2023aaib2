class Solution: #week15-1.py
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        table = {} #�j�A��:table[num] ����������
        for num in nums: #�C�ӼƦr���@��
            if num in table:   #�X�{�L����
                table[num] +=1 #���ƥ[�@
            else:
                table[num] = 1 #�Ĥ@���X�{
        #print(table) #�����٨S��X��

        ans=0
        for num in table:
            if table[num]==2:
                ans=ans^num
        return ans

