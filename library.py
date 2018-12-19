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
        parent = self.__parent # None
        left_child = self.get_left() #15
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

    def print(self, indent=1):
        data = str(indent-1) + "-" * indent * 4 + str(self.data) + f" {self.get_depth()}\n"
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
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value, parent=self)
        else:
            self.root.insert(value)
        self.size += 1
    
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
        return self.get_title() == other_book.get_title()

    def __lt__(self, other_book):
        return min(self.get_title(), other_book.get_title()) == self.get_title()

    def __ne__(self, other_book):
        return not (self == other_book)

    def __gt__(self, other_book):
        return max(self.get_title(), other_book.get_title()) == self.get_title()
    
    def __str__(self):
        return self.get_title()
