class Solution:
    def simplifyPath(self, path: str) -> str:
        # path = "/a/./b/../../c/"
        # . : 현재 디렉토리, .. : 상위 디렉토리 => 디렉토리 이동따져서 루트에서 시작하는 디렉토리만 출력해야 함

        dirs = [i for i in path.split("/") if i]
        # a = ['a', '.', 'b', '..', '..', 'c']
        # b = ['a', '.', 'b', '..', '.', 'c']
        # c = ['..', 'b', '..', '.', 'c', '...', '.', '_d']

        st = []
        for di in dirs:
            if di != "." and di !="..": st.append(di)
            else:
                if di == ".": pass
                else:
                    if st: st.pop()
                    else: continue

        output = "/".join(st)
        return "/" + output
    
        """
        wrong answer - pattern 처리로 생각할 문제 X
        dirs = path.split('/')
        output = ""
        for di in dirs:
            if di != '' and di != '.' and di != '..': 
                output += "/" + di
       
        return output if output else "/"
        """

    

        