function BinaryTree() {
}

function BinaryTreeNode(value, left = new EmptyBinaryTree, right = new EmptyBinaryTree) {
    this.value = value;
    this.left = left;
    this.right = right;
    Object.freeze(this);
}

BinaryTreeNode.prototype = new BinaryTree();
BinaryTreeNode.prototype.constructor = BinaryTreeNode;

BinaryTreeNode.prototype.isEmpty = function () {
    return false;
};
BinaryTreeNode.prototype.depth = function () {
    return 1 + Math.max(this.left.depth(), this.right.depth());
};

BinaryTreeNode.prototype.count = function () {
    return 1 + this.left.count() + this.right.count();
};

BinaryTreeNode.prototype.inorder = function (fn) {
    this.left.inorder(fn);
    fn(this.value);
    this.right.inorder(fn);
};
BinaryTreeNode.prototype.preorder = function (fn) {
    fn(this.value);
    this.left.preorder(fn);
    this.right.preorder(fn);
};
BinaryTreeNode.prototype.postorder = function (fn) {
    this.left.postorder(fn);
    this.right.postorder(fn);
    fn(this.value);
};

BinaryTreeNode.prototype.contains = function (x) {
    return this.value === x || (x < this.value ? this.left.contains(x) : this.right.contains(x));
};
BinaryTreeNode.prototype.insert = function (x) {
    if (x < this.value)
        return new BinaryTreeNode(
            this.value,
            this.left.insert(x),
            this.right
        );
    else
        return new BinaryTreeNode(
            this.value,
            this.left,
            this.right.insert(x),
        );
};
BinaryTreeNode.prototype.remove = function (x) {
    if (!this.contains(x))
        return this;

    if (x < this.value)
        return new BinaryTreeNode(
            this.value,
            this.left.remove(x),
            this.right
        );
    else if (x > this.value)
        return new BinaryTreeNode(
            this.value,
            this.left,
            this.right.remove(x)
        );
    else if (!this.left.isEmpty() && !this.right.isEmpty()) {
        let minValue = this.right.findMinValue();
        return new BinaryTreeNode(
            minValue,
            this.left,
            this.right.remove(minValue),
        )
    } else
        return !this.left.isEmpty() ? this.left : this.right;
};
BinaryTreeNode.prototype.findMinValue = function () {
    return this.left.isEmpty() ? this.value : this.left.findMinValue();
};

function EmptyBinaryTree() {
    Object.freeze(this);
}

EmptyBinaryTree.prototype = new BinaryTree();

EmptyBinaryTree.prototype.constructor = EmptyBinaryTree;

EmptyBinaryTree.prototype.isEmpty = function () {
    return true;
};

EmptyBinaryTree.prototype.depth = function () {
    return 0;
};

EmptyBinaryTree.prototype.count = function () {
    return 0;
};


EmptyBinaryTree.prototype.inorder = function (fn) {
};

EmptyBinaryTree.prototype.preorder = function (fn) {
};

EmptyBinaryTree.prototype.postorder = function (fn) {
};

EmptyBinaryTree.prototype.contains = function (x) {
    return false;
};

EmptyBinaryTree.prototype.insert = function (x) {
    return new BinaryTreeNode(x);
};

EmptyBinaryTree.prototype.remove = function (x) {
    return this;
};