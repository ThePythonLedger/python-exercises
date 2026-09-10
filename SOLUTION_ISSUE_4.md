# Solution for Issue #4

## 🛠️ Proposed Solution (by Aditya Waghamare)

### Analysis
We need to add a new exercise on Python sets following the repository's interactive storyline convention (e.g., tracking a magical artifact or collection), progressing from basic set creation to advanced set operations (`union`, `intersection`, `difference`, `symmetric_difference`, `issubset`, `frozenset`), complete with pytest tests.

### Fix
Created `exercises/sets.py` and `tests/test_sets.py` matching the repository standards.

### Implementation
```python
# exercises/sets.py

"""
The Guild of Alchemists: The Alchemical Cabinet of Unique Elements

The Master Alchemist has entrusted you with cataloging rare magical elements found across the realm.
Unlike ordinary lists, elements in an alchemical cabinet are entirely unique (no duplicates allowed)
and can be combined using powerful ritualistic set operations.
"""

# --- Task 1: Defining the Alchemical Cabinet ---
# The Master provides an initial batch of discovered element names as a list, some of which are duplicates.
# Create a function `initialize_cabinet(elements_list)` that converts this list into a `set` to remove duplicates.

def initialize_cabinet(elements_list):
    """Convert a list of elements into a unique set."""
    return set(elements_list)


# --- Task 2: Adding and Removing Ingredients ---
# New elements are discovered, and unstable elements must be banished.
# Create a function `update_cabinet(cabinet_set, new_element, unstable_element)` that:
# 1. Adds `new_element` to `cabinet_set` using `.add()`
# 2. Removes `unstable_element` from `cabinet_set` using `.discard()` (to avoid KeyError if missing)
# 3. Returns the updated set.

def update_cabinet(cabinet_set, new_element, unstable_element):
    """Add a new element and safely discard an unstable element."""
    cabinet_set.add(new_element)
    cabinet_set.discard(unstable_element)
    return cabinet_set


# --- Task 3: Combining Two Cabinets (Union) ---
# You meet a fellow alchemist and combine your unique elements.
# Create a function `combine_cabinets(cabinet_a, cabinet_b)` that returns all unique elements from both cabinets.

def combine_cabinets(cabinet_a, cabinet_b):
    """Return the union of two cabinets."""
    return cabinet_a | cabinet_b


# --- Task 4: Finding Common Elements (Intersection) ---
# To brew the Philosopher's Stone, you need elements present in BOTH your cabinet and the ancient Grimoire.
# Create a function `find_common_elements(cabinet, grimoire)` that returns elements present in both sets.

def find_common_elements(cabinet, grimoire):
    """Return the intersection of two sets."""
    return cabinet & grimoire


# --- Task 5: Rare Discoveries (Difference & Symmetric Difference) ---
# 1. Elements in your cabinet that are NOT in the forbidden vault: `find_exclusive_elements(cabinet, vault)`
# 2. Elements that are unique to either your cabinet or the rival cabinet, but not shared: `find_unique_rivalries(cabinet_a, cabinet_b)`

def find_exclusive_elements(cabinet, vault):
    """Return elements in cabinet that are not in vault (difference)."""
    return cabinet - vault

def find_unique_rivalries(cabinet_a, cabinet_b):
    """Return elements in either cabinet_a or cabinet_b, but not both (symmetric difference)."""
    return cabinet_a ^ cabinet_b


# --- Task 6: The Sealed Vault (Frozenset) ---
# Ancient elemental essences are volatile and cannot be modified.
# Create a function `seal_essence(element_tuple)` that converts a tuple of element names into a `frozenset`.

def seal_essence(element_tuple):
    """Convert a tuple into an immutable frozenset."""
    return frozenset(element_tuple)
```

And corresponding tests (`tests/test_sets.py`):

```python
# tests/test_sets.py

import pytest
from exercises.sets import (
    initialize_cabinet,
    update_cabinet,
    combine_cabinets,
    find_common_elements,
    find_exclusive_elements,
    find_unique_rivalries,
    seal_essence,
)

def test_initialize_cabinet():
    elements = ["sulfur", "mercury", "sulfur", "lead", "gold", "mercury"]
    cabinet = initialize_cabinet(elements)
    assert isinstance(cabinet, set)
    assert cabinet == {"sulfur", "mercury", "lead", "gold"}

def test_update_cabinet():
    cabinet = {"sulfur", "mercury"}
    updated = update_cabinet(cabinet, "gold", "sulfur")
    assert "gold" in updated
    assert "sulfur" not in updated
    # Test safe discard when element doesn't exist
    updated_safe = update_cabinet(updated, "silver", "nonexistent")
    assert "silver" in updated_safe

def test_combine_cabinets():
    a = {"sulfur", "mercury"}
    b = {"gold", "silver", "mercury"}
    combined = combine_cabinets(a, b)
    assert combined == {"sulfur", "mercury", "gold", "silver"}

def test_find_common_elements():
    cabinet = {"sulfur", "mercury", "lead"}
    grimoire = {"mercury", "lead", "gold"}
    common = find_common_elements(cabinet, grimoire)
    assert common == {"mercury", "lead"}

def test_find_exclusive_elements():
    cabinet = {"sulfur", "mercury", "lead"}
    vault = {"lead", "gold"}
    exclusive = find_exclusive_elements(cabinet, vault)
    assert exclusive == {"sulfur", "mercury"}

def test_find_unique_rivalries():
    a = {"sulfur", "mercury"}
    b = {"mercury", "gold"}
    rivalries = find_unique_rivalries(a, b)
    assert rivalries == {"sulfur", "gold"}

def test_seal_essence():
    essence = ("aether", "void")
    frozen = seal_essence(essence)
    assert isinstance(frozen, frozenset)
    assert frozen == frozenset(["aether", "void"])
```

Signed-off-by: Aditya Waghamare <adityawaghamare7620@gmail.com>

### Testing
Run tests with pytest:
```bash
pytest tests/test_sets.py
```


---
*Submitted by Aditya Waghamare*
💰 **Payout Address (Base L2 / EVM):** `0xb61dBcdBc3407F71EaCb64D4CBFAcf9FFfe2415C`