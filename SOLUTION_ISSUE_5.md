# Solution for Issue #5

## 🛠️ Proposed Solution (by Aditya Waghamare)

### Analysis
The task requires adding a new Python dictionaries exercise following the repository's convention: storyline-based progression, pytest unit tests with custom beginner-friendly assertions, and comprehensive coverage from basic dict creation/access to advanced manipulation.

### Implementation

#### 1. Exercise File (`exercises/dictionaries.py`)
```python
"""
Python Dictionaries Exercise: The Royal Treasury & Ledger of Eldoria

Storyline:
You have been appointed as the Royal Treasurer of the Kingdom of Eldoria. 
Your duty is to manage the kingdom's vaults, track tax revenues, audit merchant guilds, 
and merge provincial ledgers using Python dictionaries.
"""

# Task 1: Establish the Royal Vault Inventory
# The royal vault currently holds gold, silver, bronze, and gems with initial quantities:
# gold: 1500, silver: 3400, bronze: 12000, gems: 45
# Define a dictionary named `royal_vault` representing this inventory.
royal_vault = {
    "gold": 1500,
    "silver": 3400,
    "bronze": 12000,
    "gems": 45
}


# Task 2: Audit and Retrieve Vault Assets
# The High Chancellor requests the exact count of 'gold'.
# Write a function `get_asset_count(vault, asset_name)` that safely retrieves 
# the count of the given asset. If the asset does not exist, return 0 instead of raising a KeyError.
def get_asset_count(vault: dict, asset_name: str) -> int:
    return vault.get(asset_name, 0)


# Task 3: Record New Tribute
# A merchant caravan arrives from the Eastern Province delivering 500 gold and 80 platinum.
# Write a function `update_vault(vault, tribute)` that updates the existing vault dictionary 
# with the new items from the tribute dictionary and returns the updated vault.
def update_vault(vault: dict, tribute: dict) -> dict:
    vault.update(tribute)
    return vault


# Task 4: Provincial Tax Collection and Excluded Assets
# The tax collector needs to inspect the vault keys and values separately.
# Write a function `inspect_vault_records(vault)` that returns a tuple containing:
# 1. A list/view of all asset names (keys) sorted alphabetically.
# 2. A list of all quantities (values).
def inspect_vault_records(vault: dict) -> tuple:
    sorted_keys = sorted(list(vault.keys()))
    values = list(vault.values())
    return (sorted_keys, values)


# Task 5: Consolidating Two Regional Ledgers
# Eldoria has just annexed the Northern Duchy, which maintains its own ledger.
# Write a function `merge_ledgers(ledger_a, ledger_b)` that merges two ledger dictionaries.
# If an asset exists in both ledgers, their quantities should be combined (summed).
# Return a new combined dictionary without modifying the originals.
def merge_ledgers(ledger_a: dict, ledger_b: dict) -> dict:
    merged = ledger_a.copy()
    for key, value in ledger_b.items():
        merged[key] = merged.get(key, 0) + value
    return merged


# Task 6: Filtering the Kingdom's Surplus (Dictionary Comprehension)
# The treasury is auditing high-value assets. 
# Write a function `filter_wealthy_assets(vault, threshold)` that uses a dictionary comprehension
# to return a new dictionary containing only the assets whose quantity is strictly greater than the threshold.
def filter_wealthy_assets(vault: dict, threshold: int) -> dict:
    return {k: v for k, v in vault.items() if v > threshold}
```

#### 2. Test File (`tests/test_dictionaries.py`)
```python
import pytest
from exercises.dictionaries import (
    royal_vault,
    get_asset_count,
    update_vault,
    inspect_vault_records,
    merge_ledgers,
    filter_wealthy_assets
)

def test_royal_vault_definition():
    assert isinstance(royal_vault, dict), "royal_vault must be a dictionary."
    assert royal_vault.get("gold") == 1500
    assert royal_vault.get("gems") == 45

def test_get_asset_count():
    vault = {"gold": 100, "silver": 200}
    assert get_asset_count(vault, "gold") == 100
    assert get_asset_count(vault, "platinum") == 0, "Should return 0 safely for missing keys using .get()"

def test_update_vault():
    vault = {"gold": 1000}
    tribute = {"gold": 500, "platinum": 80}
    updated = update_vault(vault, tribute)
    assert updated["gold"] == 500
    assert updated["platinum"] == 80

def test_inspect_vault_records():
    vault = {"silver": 200, "gold": 100}
    keys, values = inspect_vault_records(vault)
    assert keys == ["gold", "silver"], "Keys must be sorted alphabetically."
    assert set(values) == {100, 200}

def test_merge_ledgers():
    ledger_a = {"gold": 500, "silver": 300}
    ledger_b = {"gold": 200, "bronze": 1000}
    combined = merge_ledgers(ledger_a, ledger_b)
    assert combined == {"gold": 700, "silver": 300, "bronze": 1000}
    # Ensure originals were not mutated
    assert ledger_a["gold"] == 500

def test_filter_wealthy_assets():
    vault = {"gold": 1500, "silver": 50, "bronze": 3000, "gems": 5}
    wealthy = filter_wealthy_assets(vault, 100)
    assert wealthy == {"gold": 1500, "bronze": 3000}
```

### Testing
Ran pytest locally to confirm all tests pass successfully.

Signed-off-by: Aditya Waghamare <adityawaghamare7620@gmail.com>


---
*Submitted by Aditya Waghamare*
💰 **Payout Address (Base L2 / EVM):** `0xb61dBcdBc3407F71EaCb64D4CBFAcf9FFfe2415C`