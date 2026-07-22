<p align="center">
  <img src="assets/banner.png" alt="LeetCode Solutions Banner" width="100%"/>
</p>

<h1 align="center">🧠 LeetCode Solutions</h1>

<p align="center">
  <em>A curated collection of my LeetCode problem solutions — written in Python 🐍</em>
</p>

<p align="center">
  <a href="https://leetcode.com/u/omen18/">
    <img src="https://img.shields.io/badge/LeetCode-omen18-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode"/>
  </a>
  <a href="https://github.com/omen18">
    <img src="https://img.shields.io/badge/GitHub-omen18-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

---

<p align="center">
  <img src="https://leetcard.jacoblin.cool/omen18?theme=dark&font=Karma&ext=heatmap" alt="LeetCode Stats"/>
</p>

---

## 📊 Progress Tracker

| Difficulty | Solved | Target | Progress |
|:----------:|:------:|:------:|:--------:|
| 🟢 Easy   | —      | 100    | ░░░░░░░░ |
| 🟡 Medium | —      | 150    | ░░░░░░░░ |
| 🔴 Hard   | —      | 50     | ░░░░░░░░ |

> 💡 *Update this table as you solve more problems!*

---

## 📂 Repository Structure

```
leetcode-solutions/
│
├── 📁 arrays-and-hashing/        # Array manipulation, hashmaps, sets
├── 📁 two-pointers/              # Two pointer technique problems
├── 📁 sliding-window/            # Fixed & variable sliding windows
├── 📁 stack/                     # Stack-based problems
├── 📁 binary-search/             # Binary search variants
├── 📁 linked-list/               # Singly & doubly linked lists
├── 📁 trees/                     # Binary trees, BSTs, N-ary trees
├── 📁 tries/                     # Trie / prefix tree problems
├── 📁 heap-priority-queue/       # Min/max heaps, priority queues
├── 📁 backtracking/              # Recursive backtracking
├── 📁 graphs/                    # BFS, DFS, topological sort
├── 📁 dynamic-programming/       # 1D & 2D DP problems
├── 📁 greedy/                    # Greedy algorithm problems
├── 📁 intervals/                 # Interval merging & scheduling
├── 📁 math-and-geometry/         # Mathematical & geometric problems
├── 📁 bit-manipulation/          # Bitwise operation problems
│
├── 📄 README.md                  # You are here!
└── 📁 assets/                    # Images and resources
```

---

## 🗂️ Solutions Index

### Arrays & Hashing
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | [Solution](arrays-and-hashing/001_two_sum.py) | HashMap lookup |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium | [Solution](arrays-and-hashing/049_group_anagrams.py) | Sorted key grouping |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium | [Solution](arrays-and-hashing/128_longest_consecutive_sequence.py) | HashSet approach |

### Two Pointers
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy | [Solution](two-pointers/125_valid_palindrome.py) | Two pointer squeeze |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | [Solution](two-pointers/015_3sum.py) | Sort + two pointers |

### Sliding Window
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟢 Easy | [Solution](sliding-window/121_best_time_to_buy_and_sell_stock.py) | Track min price |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | [Solution](sliding-window/003_longest_substring.py) | Variable window + set |

### Stack
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟢 Easy | [Solution](stack/020_valid_parentheses.py) | Stack matching |

### Binary Search
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 Easy | [Solution](binary-search/704_binary_search.py) | Classic binary search |

### Trees
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟢 Easy | [Solution](trees/226_invert_binary_tree.py) | Recursive swap |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟢 Easy | [Solution](trees/104_maximum_depth.py) | DFS recursion |

### Dynamic Programming
| # | Problem | Difficulty | Solution | Notes |
|:-:|---------|:----------:|:--------:|-------|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy | [Solution](dynamic-programming/070_climbing_stairs.py) | Fibonacci pattern |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | 🟡 Medium | [Solution](dynamic-programming/198_house_robber.py) | DP with skip logic |

> 📝 *This is a starter index — add rows as you solve more problems!*

---

## 🏷️ Solution Template

Each solution file follows this consistent format:

```python
"""
Problem: <Problem Name>
LeetCode #: <Number>
Difficulty: Easy / Medium / Hard
Link: https://leetcode.com/problems/<slug>/

Approach: <Brief description of approach>
Time Complexity: O(?)
Space Complexity: O(?)
"""


class Solution:
    def method_name(self, params):
        pass
```

---

## 🚀 How to Use

```bash
# Clone the repository
git clone https://github.com/omen18/leetcode-solutions.git
cd leetcode-solutions

# Run any solution
python arrays-and-hashing/001_two_sum.py
```

---

## 🤝 Connect with Me

<p align="center">
  <a href="https://github.com/omen18">
    <img src="https://img.shields.io/badge/GitHub-omen18-181717?style=flat-square&logo=github" alt="GitHub"/>
  </a>
  <a href="https://leetcode.com/u/omen18/">
    <img src="https://img.shields.io/badge/LeetCode-omen18-FFA116?style=flat-square&logo=leetcode&logoColor=white" alt="LeetCode"/>
  </a>
</p>

---

<p align="center">
  <em>⭐ Star this repo if you find it helpful!</em>
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/omen18">omen18</a>
</p>
