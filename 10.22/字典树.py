class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root  # 插入时从根节点开始判断，根节点是一个空字符串?
        for char in word:
            child = node.data.get(char)
            if child is None:  # 如果当前节点没有该元素，就增加该节点
                node.data[char] = TrieNode()  # 本级字典添加新字典
            node = node.data[char]  # 判断节点下移
        node.is_word = True


def search(self, word):
    node = self.root
    for char in word:
        node = node.data.get(char)  # 节点下沉
        if not node:
            return False
    return node.is_word  # 判断单词是否完整的存在trie 树中，存在就返回True 不存在就False

def startWith(self,prefix):   #查找前缀
    node = self.root
    for char in prefix:
        node = node.data.get(char)
        if not node:
            return False
    return Trie

def get_start(self,prefix:str):
    pass








if __name__ == '__main__':
    tire = Trie()
    tire.insert('somethere')
    tire.insert('something')
    print(tire.root.data)
