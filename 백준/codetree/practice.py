import sys


class customList(list):
  
    '''
    시계 방향으로 90도 회전한 리스트를 반환합니다
    1차원 return 1차원
    2차원 return 2차원
    1,2차원만 가능합니다
    '''
    def rotate(self) -> list:
        if self.get_dimension() == 2:
            new_list = [list(e) for e in zip(*self.copy()[::-1])]
        elif self.get_dimension() == 1:
            new_list = [list(e) for e in self.copy()]
        else:
            raise ValueError("can rotate dimension 1 or 2")
        return new_list
    
    '''
    리스트의 끝에서부터 인덱스를 찾아 인덱스 번호를 반환합니다
    '''
    def indexfromlast(self, e) -> int:
        li = self.copy()
        for i in range(len(li) - 1, -1, -1):
            if li[i] == e:
                return i
        raise IndexError("Element Not Found Error")
    
    '''
    리스트의 차원을 반환합니다
    '''
    def get_dimension(self) -> int:
        s = str(self)
        dimension = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ']':
                dimension += 1
            else:
                break
        del s
        return dimension

    '''
    리스트를 깊은복사하여 새로운 리스트를 반환합니다
    '''
    def deepcopy(self) -> list:
        new_list = []
        for e in self.copy():
            new_list.append(e)
        return new_list

    '''
    2차원 리스트의 대각선을 전부 반환합니다
    단, 두개의 리스트로 이루어진 2차원 리스트로 반환됩니다
    첫번째 리스트 : 왼쪽 아래 방향 대각선 리스트
    두번째 리스트 : 오른쪽 아래 방향 대각선 리스트
    '''
    def diagonal(self) -> list:
        if self.get_dimension() != 2:
            raise ValueError("diagonal support only 2 dimension list")
        result = []
        for i in range(2):
            diagonals = []
            if i == 0:
                matrix = self
            else:
                matrix = self.rotate()
            rows, cols = len(matrix), len(matrix[0])
            for d in range(rows + cols - 1):
                diagonal = []
                for row in range(max(0, d - cols + 1), min(rows, d + 1)):
                    col = d - row
                    diagonal.append(matrix[row][col])
                diagonals.append(diagonal)
            result.append(diagonals)
        return result
    '''
    슬라이싱 연산 오버라이드
    '''
    def __getitem__(self, index):
        result = super().__getitem__(index)
        return customList(result) if isinstance(index, slice) else result
    
    '''
    is_col = True -> 열을 반전시켜서 리스트로 리턴
    is_col = False -> 행을 반전시켜서 리스트로 리턴
    '''
    def reverse_list(self, is_col = False) -> list:
        if is_col:
            new_list = []
            for i in range(len(self)):
                new_list.append(self[i][::-1])
        else:
            new_list = self.deepcopy()[::-1]
        return new_list

def search(li):
    

input = sys.stdin.readline

li = customList(customList(map(int, input().split())) for _ in range(19))

