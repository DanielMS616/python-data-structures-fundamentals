# Python Data Structures Fundamentals

A personal learning and reference repository covering fundamental data structures, algorithmic complexity, and reusable problem-solving patterns in Python.

This repository documents my learning process around **stacks, queues, linked lists, Big-O complexity, and common algorithmic techniques**. Exercise descriptions have been paraphrased where appropriate; the implementations, explanations, examples, and additional documentation were created as part of my own learning process.

> **Language note:** Code, identifiers, and technical terminology are written in English. Some in-depth learning notes, topic documentation, and exercise explanations are currently written in German and intentionally remain part of the repository as study material.

The goal is not simply to collect working solutions. Each topic is documented with the reasoning behind the implementation, time and space complexity, edge cases, trade-offs, and patterns that can be transferred to new problems.

---

## What This Repository Demonstrates

- Reasoning about time and space complexity instead of treating data structures as black boxes
- Choosing implementations based on required operation costs and explicit trade-offs
- Recognizing reusable patterns such as slow/fast pointers, monotonic queues, and auxiliary sets
- Reasoning about invariants, edge cases, and scalability alongside functional correctness
- Turning individual exercises into a structured and reusable technical learning reference
- Documenting technical decisions in a way that makes both the implementation and the underlying reasoning reproducible

---

## Learning Structure

The repository is organized around three complementary layers:

1. **Concepts**  
   What is the data structure? Which properties and operations define it?

2. **Exercises**  
   Concrete problems with documented implementations and step-by-step explanations.

3. **Reusable Patterns**  
   Which techniques appear repeatedly across different problems?

A central idea throughout the repository is the distinction between an **abstract data type** and its **implementation**:

```text
What behavior should the structure provide?
                ↓
          ADT / concept
                ↓
How is that behavior implemented technically?
                ↓
          Implementation
```

A queue, for example, is defined by FIFO behavior. Whether it is implemented internally with a Python `list`, a `deque`, or a linked list is a separate design decision.

More: [`docs/adt_and_implementation.md`](docs/adt_and_implementation.md)

---

## Repository Structure

```text
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── docs
│   ├── README.md
│   ├── adt_and_implementation.md
│   ├── big_o_cheatsheet.md
│   ├── data_structure_patterns.md
│   ├── glossary.md
│   ├── learning_workflow.md
│   └── python_collections_complexity.md
├── LinkedLists
│   ├── README.md
│   ├── linked_list_append_o1.py
│   ├── linked_list_append_o1_explanation.md
│   ├── linked_list_find_middle.py
│   ├── linked_list_find_middle_explanation.md
│   ├── linked_list_remove_duplicates.py
│   ├── linked_list_remove_duplicates_explanation.md
│   ├── linked_list_reverse.py
│   └── linked_list_reverse_explanation.md
├── queue
│   ├── README.md
│   ├── max_queue.py
│   ├── max_queue_explanation.md
│   ├── priority_queue.py
│   ├── priority_queue_explanation.md
│   ├── reversable_queue.py
│   └── reversable_queue_explanation.md
└── Stack
    ├── README.md
    ├── balanced_symbols.py
    ├── balanced_symbols_explanation.md
    ├── par_checker.py
    ├── par_checker_explanation.md
    ├── rev_string.py
    └── rev_string_explanation.md
```

---

## Documentation Layers

### 1. Python Implementations

The `.py` files contain the clean reference implementations.

Comments are intentionally kept concise and are mainly used when they explain:

- **why** a line or step is necessary,
- an important algorithmic decision,
- a non-obvious edge case,
- or a relevant complexity consideration.

Example:

```python
# Save the next node before reversing the current link.
next_node = current.next
```

Self-explanatory code is not commented unnecessarily.

---

### 2. Exercise Explanations

Each exercise is accompanied by a detailed Markdown file:

```text
exercise.py
exercise_explanation.md
```

These files typically include:

- a paraphrased exercise goal,
- the final implementation,
- a step-by-step explanation,
- text-based visualizations,
- time and space complexity,
- edge and error cases,
- design and scaling considerations,
- additional examples.

Additional examples are explicitly separated from the original test scenario.

---

### 3. Topic READMEs and Shared Documentation

Each data-structure folder contains a `README.md` explaining the topic independently of any single exercise.

The `docs/` directory contains knowledge that applies across multiple topics:

| Document | Purpose |
| --- | --- |
| [`adt_and_implementation.md`](docs/adt_and_implementation.md) | Distinguishes ADTs, algorithms, and implementations |
| [`big_o_cheatsheet.md`](docs/big_o_cheatsheet.md) | Explains Big-O notation and complexity analysis |
| [`python_collections_complexity.md`](docs/python_collections_complexity.md) | Reference for common Python operation costs |
| [`data_structure_patterns.md`](docs/data_structure_patterns.md) | Collects reusable algorithmic patterns |
| [`glossary.md`](docs/glossary.md) | Quick reference for important terminology |
| [`learning_workflow.md`](docs/learning_workflow.md) | Documents the learning and documentation workflow |

---

## Data Structures at a Glance

| Structure | Core principle | Typical strength | Mental model |
| --- | --- | --- | --- |
| Stack | LIFO | Work with the most recently added element | Stack of plates |
| Queue | FIFO | Process elements in arrival order | Waiting line |
| Linked List | Linked nodes | Change links without shifting contiguous elements | Chain of nodes |

### Stack

```text
Top
 ↓
[C]
[B]
[A]
```

The most recently added element, `C`, is removed first.

More: [`stacks/README.md`](stacks/README.md)

### Queue

```text
Front                   Rear
  ↓                       ↓
[A] -> [B] -> [C]
```

`A` entered first and is therefore removed first.

More: [`queues/README.md`](queues/README.md)

### Linked List

```text
head
 ↓
[5 | •] -> [6 | •] -> [7 | None]
```

Each node stores data and a reference to the next node.

More: [`linked_lists/README.md`](linked_lists/README.md)

---

## Exercises

### Stack

| Exercise | Main idea |
| --- | --- |
| [`rev_string.py`](stacks/rev_string.py) | Use LIFO behavior to reverse a sequence |
| [`par_checker.py`](stacks/par_checker.py) | Track unmatched opening parentheses |
| [`balanced_symbols.py`](stacks/balanced_symbols.py) | Validate correctly nested symbol types |

### Queue

| Exercise | Main idea |
| --- | --- |
| [`priority_queue.py`](queues/priority_queue.py) | Combine priority with stable insertion order |
| [`max_queue.py`](queues/max_queue.py) | Retrieve the maximum in `O(1)` using a monotonic helper queue |
| [`reversable_queue.py`](queues/reversable_queue.py) | Combine queue and stack behavior |

### Linked Lists

| Exercise | Main idea |
| --- | --- |
| [`linked_list_append_o1.py`](linked_lists/linked_list_append_o1.py) | Use a tail reference for `O(1)` append |
| [`linked_list_reverse.py`](linked_lists/linked_list_reverse.py) | Reverse links in-place with Previous / Current / Next |
| [`linked_list_remove_duplicates.py`](linked_lists/linked_list_remove_duplicates.py) | Track seen values with a helper set |
| [`linked_list_find_middle.py`](linked_lists/linked_list_find_middle.py) | Find the middle with Slow / Fast Pointers |

---

## Big O as a Shared Language

Many design decisions in this repository only make sense when the cost of individual operations is taken into account.

Examples:

```text
List index access                -> O(1)
list.pop() at the end            -> O(1)
list.pop(0)                      -> O(n)
Linked-list search               -> O(n)
Set membership                   -> average O(1)
list.sort()                      -> O(n log n)
```

These costs directly influence implementation choices:

```text
Why is the next PriorityQueue element stored at the end of the list?
→ Because pop() at the end is O(1).

Why does the Linked List keep a tail reference?
→ So the end does not need to be searched in O(n) on every append.

Why use a set when removing duplicates?
→ So checking whether a value has already been seen is average O(1).
```

More: [`docs/big_o_cheatsheet.md`](docs/big_o_cheatsheet.md)

---

## Reusable Problem-Solving Patterns

The exercises are not intended to remain isolated solutions. They expose patterns that can be recognized in new problems:

```text
Stack / LIFO
    → reverse sequences
    → validate nested structures

Previous + Current + Next
    → safely modify linked-list references

Slow + Fast Pointer
    → find the middle of a linked list
    → detect cycles

Seen Set
    → detect duplicates
    → track already processed values

Monotonic Helper Queue
    → retrieve a maximum without rescanning the full queue

Tail Pointer
    → access the end of a linked list directly
```

More: [`docs/data_structure_patterns.md`](docs/data_structure_patterns.md)

---

## Quality Considerations

The exercises are reviewed not only for functional correctness but also through a broader engineering lens:

```text
Correctness
    Does the implementation solve the intended problem?

Edge cases
    What happens with an empty structure or a single element?

Data integrity / invariants
    Do head, tail, and next references remain consistent?

Complexity
    Which operations become expensive as the input grows?

Scalability
    Does the approach still make sense with much larger inputs?

Interface design
    Should an empty dequeue return None or raise an exception?
```

For larger software projects, this same mindset extends naturally to topics such as robust error handling, persistence, database constraints, testing, configuration, and operational readiness.

---

## Setup

Some stack exercises use the `pythonds3` package. The version used by this repository is recorded in [`requirements.txt`](requirements.txt).

Install the dependencies with:

```bash
python3 -m pip install -r requirements.txt
```

Typical import:

```python
from pythonds3.basic import Stack
```

---

## Independent Learning Reference

The documentation combines personal study notes, practical implementations, and additional technical context into a structured learning reference.

Exercise goals are intentionally paraphrased where appropriate. The focus is on the implementation itself, the reasoning behind it, complexity analysis, edge cases, and transferable problem-solving patterns.

---

## License

The original implementations and documentation in this repository are available under the [MIT License](LICENSE).

---

## Learning Goal

The long-term goal is not simply to remember **how** a particular exercise was solved.

More importantly, new problems should trigger questions such as:

```text
Which data structure fits the required access pattern?

Which operation is expensive here?

Can I store additional information to make a later operation cheaper?

Which invariant must remain true after every modification?

Do I recognize a reusable pattern?
```

That shift—from recalling individual solutions to recognizing structures, costs, and patterns—is the main purpose of this repository.
