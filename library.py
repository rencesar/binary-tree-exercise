class TreeNode:
    def __init__(self, data, parent, is_right=False):
        self.data = data
        self.__left = None
        self.__right = None
        self.__parent = parent
        self.is_right = is_right
        self.left_height = 0
        self.right_height = 0

    def set_data(self, value):
        self.data = value

    def set_left(self, value):
        self.__left = value

    def set_right(self, value):
        self.__right = value
    
    def set_parent(self, parent):
        self.__parent = parent
    
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def get_data(self):
        return self.data
    
    def is_root(self):
        return not isinstance(self.__parent, TreeNode)
    
    def is_leaf(self):
        return self.get_left() is None and self.get_right() is None
    
    def get_height(self):
        left_height = 0
        if self.get_left() is not None:
            left_height = self.get_left().get_height()
        right_height = 0
        if self.get_right() is not None:
            right_height = self.get_right().get_height()
        return 1 + max(left_height, right_height)
    
    def get_depth(self):
        left_height = 0
        right_height = 0
        if self.get_left() is not None:
            left_height = self.get_left().get_height()
        if self.get_right() is not None:
            right_height = self.get_right().get_height()
        return left_height - right_height

    def rotate_to_left(self):
        parent = self.__parent
        right_child = self.get_right()
        if self.is_root():
            parent.root = right_child
            right_child.is_right = False
        else:
            if not self.is_right:
                parent.set_left(right_child)
            else:
                parent.set_right(right_child)
                right_child.is_right = True
        self.set_right(right_child.get_left())
        self.set_parent(right_child)
        right_child.set_parent(parent)
        right_child.set_left(self)
        right_child.get_left().is_right = True
        self.is_right = False

    def rotate_to_right(self):
        parent = self.__parent
        left_child = self.get_left()
        if self.is_root():
            parent.root = left_child
        else:
            if not self.is_right:
                parent.set_left(left_child)
            else:
                parent.set_right(left_child)
                left_child.is_right = True
        self.set_left(left_child.get_right())
        self.set_parent(left_child)
        left_child.set_parent(parent)
        left_child.set_right(self)
        left_child.get_right().is_right = False
        self.is_right = True

    def double_rotation_left(self):
        self.get_right().rotate_to_right()
        self.rotate_to_left()

    def double_rotation_right(self):
        self.get_left().rotate_to_left()
        self.rotate_to_right()

    def run_balance(self):
        balance = self.get_depth()
        if balance > 1:
            if self.get_left().get_depth() > 0:
                self.rotate_to_right()
            else:
                self.double_rotation_right()
        elif balance < -1:
            if self.get_right().get_depth() < 0:
                self.rotate_to_left()
            else:
                self.double_rotation_left()

    def insert(self, data):
        if self.data > data:
            if not self.get_left():
                self.set_left(TreeNode(data, self))
            else:
                self.get_left().insert(data)
        elif self.data < data:
            if not self.get_right():
                self.set_right(TreeNode(data, self, is_right=True))
            else:
                self.get_right().insert(data)
        self.run_balance()
    
    def remove(self):
        if self.get_left() is not None and self.get_right() is not None:
            substitute = self.get_right()
            while True:
                if substitute.get_left() is None:
                    break
                substitute = substitute.get_left()
            substitute.remove()
            substitute.set_left(self.get_left())
            substitute.set_right(self.get_right())
        elif not self.is_leaf():
            substitute = self.get_left() or self.get_right()
        else:
            substitute = None
        
        if self.is_root():
            parent.root = substitute
        if not self.is_right:
            parent.set_left(substitute)
        else:
            parent.set_right(substitute)
        substitute.set_parent(parent)        

    def print(self, indent=0):
        data = str(indent) + "-" * indent * 4 + str(self.data) + f" {self.get_depth()}\n"
        if self.get_left() is not None:
            data += '/' + self.get_left().print(indent+1)
        if self.get_right() is not None:
            data += '\\' + self.get_right().print(indent+1)
        return data
    
    def __str__(self):
        return self.print()
    
    def __iter__(self):
        if self.get_left() is not None:
            for node in self.get_left():
                yield node
        yield self
        if self.get_right():
            for node in self.get_right():
                yield node


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def height(self):
        if self.root is None:
            return 0
        return self.root.get_height()
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value, parent=self)
        else:
            self.root.insert(value)
        self.size += 1
    
    def search(self, value, node=0):
        if self.root is None or node is None:
            return None
        if node == 0:
            node = self.root
        
        if node.get_data() == value:
            return node
        elif value < node.get_data():
            return self.search(value, node.get_left())
        elif value > node.get_data():
            return self.search(value, node.get_right())   
    
    def search_by_year(self, value):
        if self.root is None:
            return None
        result = []
        for node in self.root:
            if node.get_data().get_year() == value:
                result.append(node.get_data())
        return result
    
    def remove_item(self, value):
        node = self.search(value)
        if node is None:
            return node
        node.remove()
    
    def __str__(self):
        return str(self.root)


class Book:

    def __init__(self, title, year):
        self._title = title
        self._year = year

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def __eq__(self, other_book):
        if isinstance(other_book, Book):
            return self.get_title() == other_book.get_title()
        return self.get_title() == other_book

    def __lt__(self, other_book):
        if isinstance(other_book, Book):
            return min(self.get_title(), other_book.get_title()) == self.get_title()
        return min(self.get_title(), other_book) == self.get_title()

    def __ne__(self, other_book):
        return not (self == other_book)

    def __gt__(self, other_book):
        if isinstance(other_book, Book):
            return max(self.get_title(), other_book.get_title()) == self.get_title()
        return max(self.get_title(), other_book) == self.get_title()
    
    def __str__(self):
        return f"{self.get_title()} |{self.get_year()}|"
