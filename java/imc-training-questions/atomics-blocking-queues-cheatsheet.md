# Java Atomics & Blocking Queues Cheatsheet

## 1. Atomic Variables (`java.util.concurrent.atomic`)
Thread-safe variables that allow multiple threads to perform updates/reads without using manual `synchronized` blocks or `Locks`. They use **CAS (Compare-And-Swap)**, a lock-free underlying CPU instruction.

### Key Methods
- `get()` / `set(val)`: Basic access.
- `incrementAndGet()` / `decrementAndGet()`: Atomic `++i` or `--i`.
- `getAndIncrement()` / `getAndDecrement()`: Atomic `i++` or `i--`.
- `addAndGet(delta)`: Adds value and returns result.
- `compareAndSet(expected, update)`: Updates only if current value == expected. Returns `true` on success.

### Why use Atomics?
- **Lock-Free**: Threads don't "pause" (suspend) as they do with `synchronized`.
- **Performance**: High throughput for simple counters or state flags.
- **Note**: Atomics guarantee **atomicity** and **visibility**, but not the **order** of operations between different atomic variables.

---

## 2. Blocking Queues (`java.util.concurrent.BlockingQueue`)
Thread-safe queues designed for the **Producer-Consumer** pattern. They handle the waiting logic automatically.

### Operation Multi-Map

| Action | Throws Exception | Special Value | Blocks (Waits) | Times Out |
| :--- | :--- | :--- | :--- | :--- |
| **Insert** | `add(e)` | `offer(e)` (returns `false`) | `put(e)` | `offer(e, time, unit)` |
| **Remove** | `remove()` | `poll()` (returns `null`) | `take()` | `poll(time, unit)` |
| **Examine** | `element()` | `peek()` | N/A | N/A |

> **Best Practice**: `put()` and `take()` throw `InterruptedException`. Always handle it properly, usually by restoring the interrupt status: `Thread.currentThread().interrupt();`.

---

## 3. Implementation Comparison

### LinkedBlockingQueue vs. ArrayBlockingQueue

| Feature | `ArrayBlockingQueue` | `LinkedBlockingQueue` |
| :--- | :--- | :--- |
| **Internal Data** | Pre-allocated Array | Linked List (Nodes) |
| **Capacity** | Fixed (Bounded) | Optional (Bounded or Unbounded) |
| **Locking** | **Single Lock** for both `put` and `take` | **Two Separate Locks** for `put` and `take` |
| **GC Pressure** | **Low** | **High** |
| **Throughput** | Lower due to contention | Higher (Producer/Consumer don't block each other) |

#### Deep Dive: Key Concepts

*   **GC (Garbage Collection) Pressure**:
    *   `LinkedBlockingQueue` creates a new `Node` object every time you insert an item. If you process millions of orders/second, this generates a massive amount of short-lived objects.
    *   The Java Garbage Collector must eventually clean these up, which can cause **Latency Spikes** (micro-pauses in your application).
    *   `ArrayBlockingQueue` reuses the same array slots, creating zero extra objects during insertion/removal.

*   **Lock Contention**:
    *   `ArrayBlockingQueue` uses one lock for the entire queue. If a producer is adding an item, a consumer cannot remove one at the same time. They "contend" for the same lock.
    *   `LinkedBlockingQueue` has a "Two Lock Queue" algorithm. One thread can be putting an item in the tail while another is taking an item from the head simultaneously.

*   **Latency vs. Throughput**:
    *   **Latency Critical (Trading)**: Use `ArrayBlockingQueue` to avoid GC pauses.
    *   **High Throughput (General App)**: Use `LinkedBlockingQueue` to allow simultaneous production/consumption.