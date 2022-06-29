"""
public


class Test {

int count = 0;

public int solution(Tree T) {
// write your code in Java SE 8
}

public int goodNodes(Tree root) {
if (root == null) {


return count;
}

markGoodNodes(root, root.x);
return count;
}

public
void
markGoodNodes(Tree
root, int
max) {
if (root.x >= max) {
count++;
}

if (root.l != null) {
markGoodNodes(root.l, Math.max(max, root.x));
}

if (root.right != null) {
markGoodNodes(root.r, Math.max(max, root.x));
}
}

}
"""