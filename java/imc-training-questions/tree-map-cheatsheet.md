# Java TreeMap Cheatsheet

Orders keys lower to higher.
- Use a **PriorityQueue** when you only need the min/max value.
- Use a **TreeMap** when you need to search or update data in the middle.

## Navigation Methods (Time Complexity: $O(\log n)$)

| Method | Description | Example Use Case |
| :--- | :--- | :--- |
| `ceilingEntry(K)` / `ceilingKey(K)` | Smallest key $\ge$ key | "Find the best ask price $\ge \$100$" |
| `floorEntry(K)` / `floorKey(K)` | Largest key $\le$ key | "Find the best bid price $\le \$100$" |
| `higherEntry(K)` / `higherKey(K)` | Smallest key $>$ key | "Find the next price level above $\$100$" |
| `lowerEntry(K)` / `lowerKey(K)` | Largest key $<$ key | "Find the next price level below $\$100$" |

## Consuming Elements (Time Complexity: $O(\log n)$)

- `firstEntry()` / `firstKey()`: Returns the lowest key (e.g., "Get the best ask/cheapest seller").
- `lastEntry()` / `lastKey()`: Returns the highest key (e.g., "Get the best bid/highest buyer").
- `pollFirstEntry()`: Returns and **removes** the lowest entry.
- `pollLastEntry()`: Returns and **removes** the highest entry.

## Initialization

```java
// Natural order (ascending)
TreeMap<Double, Volume> asks = new TreeMap<>();

// Reverse order (descending)
TreeMap<Double, Volume> bids = new TreeMap<>(Collections.reverseOrder());
```

## Range Views

```java
TreeMap<Double, Long> orderBook = new TreeMap<>();

// 1. subMap(fromKey, inclusive, toKey, inclusive)
NavigableMap<Double, Long> range = orderBook.subMap(99.0, true, 101.0, true);

// 2. tailMap(fromKey, inclusive)
NavigableMap<Double, Long> highPriced = orderBook.tailMap(100.0, true);

// 3. headMap(toKey, inclusive)
NavigableMap<Double, Long> lowPriced = orderBook.headMap(100.0, true);
```

## Update Patterns (Critical for Order Books)

### Increment Volume
```java
orderBook.put(price, orderBook.getOrDefault(price, 0L) + volume);
```

### Decrement/Remove if Zero
```java
long newVol = orderBook.getOrDefault(price, 0L) - executedVol;
if (newVol <= 0) {
    orderBook.remove(price);
} else {
    orderBook.put(price, newVol);
}
```

### Grouping Orders by Price
```java
priceMap.computeIfAbsent(price, k -> new LinkedList<>()).add(orderId);
```

## Trading Tips

- **Views**: Range views (`subMap`, `headMap`, `tailMap`) are **LIVE VIEWS**. Removing an element from the view removes it from the original map.
- **Precision**: Avoid `Double` for keys. Use `Long` (e.g., `price * 10,000`) to avoid floating-point precision issues.
- **Performance**: Use `for (Map.Entry<Double, Long> entry : orderBook.entrySet())` for the most efficient iteration.
- **Complexity**: `orderBook.clear()` is $O(n)$; most other operations are $O(\log n)$.
