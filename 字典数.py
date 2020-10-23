class TrieNode:
    def __init__(self):
        self.data={}
        self.is_word=False

    def __repr__(self):
        return f"Node({self.data})"

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root  #插入节点时从根结点开始判断，根结点是一个空字典
        for char in word:
            child =node.data.get(char)
            if not child: # 如果当前节点没有该元素，则增加结点
                node.data[char] = TrieNode()  # 本级字典添加新字典
            node = node .data[char]  #判断结点下移
            node.is_word=True
    def search(self,word):
        node =self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

if __name__ =='__main__':
    tire =Trie()
    tire.insert('cook')
    tire.insert('book')
    print(tire)


