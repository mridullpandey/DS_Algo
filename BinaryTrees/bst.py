Binary
Search
Tree | Set
1(Search and Insertion)
The
following is definition
of
Binary
Search
Tree(BST)
according
to
Wikipedia

Binary
Search
Tree, is a
node - based
binary
tree
data
structure
which
has
the
following
properties:
The
left
subtree
of
a
node
contains
only
nodes
with keys lesser than the node’s key.
The
right
subtree
of
a
node
contains
only
nodes
with keys greater than the node’s key.
The
left and right
subtree
each
must
also
be
a
binary
search
tree.
There
must
be
no
duplicate
nodes.
200
px - Binary_search_tree.svg

The
above
properties
of
Binary
Search
Tree
provide
an
ordering
among
keys
so
that
the
operations
like
search, minimum and maximum
can
be
done
fast.If
there is no
ordering, then
we
may
have
to
compare
every
key
to
search
a
given
key.

Searching
a
key
To
search
a
given
key in Binary
Search
Tree, we
first
compare
it
with root, if the key is present at root, we return root.If key is greater than root’s key, we recur for right subtree of root node.Otherwise we recur for left subtree.

Recommended: Please
solve
it
on “PRACTICE” first, before
moving
on
to
the
solution.
filter_none
edit
play_arrow

brightness_4
// C
function
to
search
a
given
key in a
given
BST
struct
node * search(struct
node * root, int
key)
{
// Base
Cases: root is null or key is present
at
root
if (root == NULL | | root->key == key)
return root;

// Key is greater
than
root
's key
if (root->key < key)
    return search(root->right, key);

    // Key is smaller
    than
    root
    's key
    return search(root->left, key);
    }

    Illustration
    to
    search
    6 in below
    tree:
    1.
    Start
    from root.

    2.
    Compare
    the
    inserting
    element
    with root, if less than root, then recurse for left, else recurse for right.
    3. If element to search is found anywhere,
    return true, else return false.
    bstsearch

    Insertion
    of
    a
    key
    A
    new
    key is always
    inserted
    at
    leaf.We
    start
    searching
    a
    key
    from root till

    we
    hit
    a
    leaf
    node.Once
    a
    leaf
    node is found, the
    new
    node is added as a
    child
    of
    the
    leaf
    node.

    100
    100
/    \        Insert
40 / \
20
500 - -------->          20
500
/   \ / \
    10
30
10
30
\
40
filter_none
edit
play_arrow

brightness_4
// C
program
to
demonstrate
insert
operation in binary
search
tree
# include<stdio.h>
# include<stdlib.h>

struct
node
{
    int
key;
struct
node * left, *right;
};

// A
utility
function
to
create
a
new
BST
node
struct
node * newNode(int
item)
{
    struct
node * temp = (struct node *)
malloc(sizeof(struct
node));
temp->key = item;
temp->left = temp->right = NULL;
return temp;
}

// A
utility
function
to
do
inorder
traversal
of
BST
void
inorder(struct
node * root)
{
if (root != NULL)
    {
        inorder(root->left);
    printf("%d \n", root->key);
    inorder(root->right);
    }
    }

    / *A
    utility
    function
    to
    insert
    a
    new
    node
    with given key in BST * /
    struct node * insert(struct node * node, int key)
    {
    / *If
    the
    tree is empty,
    return a
    new
    node * /
    if (node == NULL) return newNode(key);

    / *Otherwise, recur
    down
    the
    tree * /
    if (key < node->key)
        node->left = insert(node->left, key);
        else if (key > node->key)
            node->right = insert(node->right, key);

            / * return the(unchanged)
            node
            pointer * /
            return node;
        }

        // Driver
        Program
        to
        test
        above
        functions
        int
        main()
        {
        / *Let
        us
        create
        following
        BST
        50
    / \
            30
    70
    /   \ / \
            20
    40
    60
    80 * /
    struct
    node * root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    // print
    inoder
    traversal
    of
    the
    BST
    inorder(root);

    return 0;
    }

    Output:
    20
    30
    40
    50
    60
    70
    80
    Illustration
    to
    insert
    2 in below
    tree:
    1.
    Start
    from root.

    2.
    Compare
    the
    inserting
    element
    with root, if less than root, then recurse for left, else recurse for right.
    3. After reaching end, just insert that node at left( if less than current) else right.
    bstsearch
    Time Complexity: The
    worst
    case
    time
    complexity
    of
    search and insert
    operations is O(h)
    where
    h is height
    of
    Binary
    Search
    Tree.In
    worst
    case, we
    may
    have
    to
    travel
    from root to

    the
    deepest
    leaf
    node.The
    height
    of
    a
    skewed
    tree
    may
    become
    n and the
    time
    complexity
    of
    search and insert
    operation
    may
    become
    O(n).

        Some
    Interesting
    Facts:

    Inorder
    traversal
    of
    BST
    always
    produces
    sorted
    output.
        We
    can
    construct
    a
    BST
    with only Preorder or Postorder or Level Order traversal.Note that we can always get inorder traversal by sorting the only given traversal.
    Number of unique BSTs with n distinct keys is Catalan Number
    Related Links:

        Binary
    Search
    Tree
    Delete
    Operation
    Quiz
    on
    Binary
    Search
    Tree
    Coding
    practice
    on
    BST
    All
    Articles
    on
    BST
    Please
    write
    comments if you
    find
    anything
    incorrect, or you
    want
    to
    share
    more
    information
    about
    the
    topic
    discussed
    above

    Recommended
    Posts:
    Count
    the
    Number
    of
    Binary
    Search
    Trees
    present in a
    Binary
    Tree
    Make
    Binary
    Search
    Tree
    Sum
    of
    all
    the
    levels in a
    Binary
    Search
    Tree
    Floor in Binary
    Search
    Tree(BST)
    Binary
    Search
    Tree | Set
    2(Delete)
    Optimal
    Binary
    Search
    Tree | DP - 24
    Print
    Binary
    Search
    Tree in Min
    Max
    Fashion
    Threaded
    Binary
    Search
    Tree | Deletion
    Print
    all
    odd
    nodes
    of
    Binary
    Search
    Tree
    Print
    all
    even
    nodes
    of
    Binary
    Search
    Tree
    Inorder
    Successor in Binary
    Search
    Tree
    Number
    of
    pairs
    with a given sum in a Binary Search Tree
    How to handle duplicates in Binary Search Tree?
    Construct a Binary Search Tree from given postorder
    Iterative searching in Binary Search Tree




    Article Tags: Binary
    Search
    TreeAmazonLinkedinMicrosoftSamsung
    Practice
    Tags: AmazonMicrosoftSamsungLinkedinBinary
    Search
    Tree

    thumb_up
    39

    1.8

    Based
    on
    174
    vote(s)
    Feedback / Suggest
    Improvement
    Notes
    Improve
    Article
    Please
    write
    to
    us
    at
    contribute @ geeksforgeeks.org
    to
    report
    any
    issue
    with the above content.
    Post navigation
    Previous
    first_page Add all greater values to every node in a given BST
    Next
    last_pageBinary Search Tree | Set 2 (Delete)




    Writing code in comment? Please use ide.geeksforgeeks.org, generate link and share the link here.

    auto


    Most popular articles
    Must Do Coding Questions for Companies like Amazon, Microsoft, Adobe, ...
    Python | Segregate list elements by Suffix
    Check for balanced parentheses in an expression | O(1) space | O(N ^ 2) time complexity
    D3.js | d3.entries() Function
    Find the winner of the Game to Win by erasing any two consecutive similar alphabets



    Most Visited Articles
    Find number of magical pairs of string of length L
    Find the integers that doesnot ends with T1 or T2 when squared and added X
    Average
    Perl | Reading a CSV File
    Maximum number that can be display on Seven Segment Display using N segments


    GeeksforGeeks
    5th Floor, A-118,
    Sector-136, Noida, Uttar Pradesh - 201305
    feedback @ geeksforgeeks.org
    COMPANY
    About Us
    Careers
    Privacy Policy
    Contact Us
    LEARN
    Algorithms
    Data Structures
    Languages
    CS Subjects
    Video Tutorials
    PRACTICE
    Courses
    Company-wise
    Topic-wise
    How to begin?
    CONTRIBUTE
    Write an Article
    Write Interview Experience
    Internships
    Videos

    @ geeksforgeeks, Some rights reserved
