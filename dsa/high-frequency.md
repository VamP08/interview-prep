# High-Frequency Interview Questions

Most-reported questions at large companies (FAANG + big MNCs), cross-referenced from company-wise lists. All are in the NeetCode 150 - grind these first before an interview, they repeat constantly.

| Problem | Topic | Reported at |
|---|---|---|
| [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays & Hashing | Amazon, Google, Microsoft, everywhere |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | Amazon, Microsoft, Meta |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | Google, Amazon |
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Intervals | Meta, Amazon, Google |
| [LRU Cache](https://leetcode.com/problems/lru-cache/) | Linked List / Design | Amazon, Microsoft, everywhere |
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Graphs | Amazon, Meta, Microsoft |
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Sliding Window | Amazon, Meta |
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | Amazon, Meta, everywhere |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Arrays & Hashing | Amazon, Uber |
| [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers | Meta, Amazon |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Graphs | Amazon, Google, Meta |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Sliding Window | Amazon, Microsoft |
| [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Trees | all FAANG |
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary Search | Google, Microsoft |
| [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap / Linked List | Amazon, Google |
| [Word Ladder](https://leetcode.com/problems/word-ladder/) | Graphs | Amazon, Meta |
| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Advanced Graphs | Google |
| [Coin Change](https://leetcode.com/problems/coin-change/) | 1-D DP | Amazon, Meta |
| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Heap | Amazon, Google |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Heap | Meta, Amazon |

Notes from 2025-2026 reports:

- Medium difficulty dominates (~55% of asked questions); easies open phone screens, hards cluster at Google and senior loops.
- Trend: classic problems dressed in applied wording (delivery windows, ad budgets, rate limiters). The underlying pattern is unchanged - strip the story, find the structure.
- Expect follow-ups over new problems: "now do it in O(1) space", "now the input is a stream", "now parallelize it".

## Target company profiles

### Google
- OA (new grad): 2 easy-medium, HackerRank or internal platform. Phone screen: 1-2 medium/hard in a shared doc - NO IDE, no autocomplete; practice writing code in a plain editor.
- Onsite: 1-2 medium/hard per round with 2-3 follow-ups; graded on reasoning and communication, not just correctness. 2026 pilot: one round may be code COMPREHENSION - read and explain unfamiliar code.
- Leans: graphs, DP, hards, follow-up chains ("now the input is a stream"). Googlyness/behavioral round separate.

### Meta
- Phone screen: 45 min, TWO LC easy-medium problems in ~35 min in CoderPad with execution OFF. Speed and bug-free first pass matter more than anywhere else - drill timed pairs.
- Onsite: 2 coding rounds (2026: one may be AI-assisted in-editor), product/system design at E4+, behavioral with strict rubric.
- Leans: the Meta-tagged LC top list is unusually predictive - grind it before the loop.

### Oracle (Cloud/OCI)
- Multiple rounds, LC easy-medium difficulty; interviewers weight CODE QUALITY: naming, no redundant logic, edge cases handled unprompted.
- Java/Python fine. Expect core CS questions (OS, networking basics) mixed into coding rounds; senior loops add system design.

### AI startups (Sarvam AI and similar)
- Sarvam reported loop: ~3 rounds - project/build assessment with AI TOOLS ALLOWED (~1 hr, LLM use permitted), resume + DSA + backend breadth round, founder chat.
- Build rounds are hands-on and proctored: build something non-trivial under time pressure. A public GitHub with one well-documented recent project beats five abandoned ones.
- DSA bar exists but breadth + fundamentals + shipping ability weigh more than LC-hard grinding. Backend systems, APIs, and ML/GenAI literacy (transformers, inference, RAG basics) come up.

### Difficulty target

Google/Meta: comfortable at LC medium in <=25 min, hards attempted. Oracle: mediums, clean code. AI startups: mediums + ability to build and explain real systems.
