# aoc-2025

## Summary

```console
λ fd part | parallel -j8 --keep-order 'echo -n "{}: " && profile uv run {} >/dev/null'
day00/part1.py: took 0.10 sec, peak 45.8M mem, 99% cpu
day01/part1.py: took 0.03 sec, peak 45.8M mem, 87% cpu
day01/part2.py: took 0.06 sec, peak 46.1M mem, 87% cpu
day02/part1.py: took 0.35 sec, peak 45.8M mem, 97% cpu
day02/part2.py: took 7.74 sec, peak 46.0M mem, 99% cpu
day03/part1.py: took 0.03 sec, peak 45.7M mem, 71% cpu
day03/part2.py: took 0.04 sec, peak 45.9M mem, 67% cpu
day04/part1.py: took 0.07 sec, peak 45.9M mem, 74% cpu
day04/part2.py: took 2.46 sec, peak 45.6M mem, 98% cpu
day05/part1.py: took 0.05 sec, peak 45.8M mem, 100% cpu
day05/part2.py: took 0.11 sec, peak 45.9M mem, 99% cpu
day06/part1.py: took 0.16 sec, peak 45.9M mem, 100% cpu
day06/part2.py: took 0.10 sec, peak 45.8M mem, 99% cpu
day07/part1.py: took 0.11 sec, peak 45.7M mem, 99% cpu
day07/part2.py: took 24.40 sec, peak 45.8M mem, 99% cpu
day08/part1.py: took 0.95 sec, peak 140.1M mem, 97% cpu
day08/part2.py: took 1.14 sec, peak 140.9M mem, 91% cpu
day09/part1.py: took 0.19 sec, peak 45.8M mem, 99% cpu
day09/part2.py: took 2.00 sec, peak 45.9M mem, 99% cpu
day10/part1.py: took 0.13 sec, peak 46.1M mem, 99% cpu
day10/part2.py: took 0.54 sec, peak 87.4M mem, 394% cpu
day11/part1.py: took 0.15 sec, peak 45.9M mem, 99% cpu
day11/part2.py: took 0.12 sec, peak 45.9M mem, 93% cpu
day12/part1.py: took 0.10 sec, peak 46.1M mem, 99% cpu
```

Day 1:
* 1.1. Simple modulus.
* 1.2. Spent too much time trying to fix edge cases, and then just went back for the simple one-by-one solution.  It's day 1, it can't take that long to run.

Day 2:
* 2.1. Divide in half and check if halves are equal.
* 2.2. No smart math-y solution here, just checking everything.  Though the code is less readable than it should for being so unsmart.

Day 3:
* 3.1. Quite happy with my [3-line solution](https://github.com/giovannipcarvalho/aoc-2025/blob/master/day03/part1.py#L10-L13).
* 3.2. Extended nicely from the idea in part 1.  Also, [`slice()`](https://github.com/giovannipcarvalho/aoc-2025/blob/master/day03/part2.py#L20) was pretty handy.

Day 4:
* 4.1. Straightforward grid and checking neighbors.  Pretty common theme in AoC.
* 4.2. A little slow simulation of "removing and checking", but decently readable.

Day 5:
* 5.1. Making use of `range()`s made it very simple to solve.
* 5.2. Went back to using tuples, and only after-the-fact I learned that `ranges()` have `.start` and `.stop` attributes (didn't go back to change it, though).  I also confused myself when implementing the overlap check (`b.start <= a.stop <= b.stop` instead of `a.start <= b.start <= a.stop`) and took me quite some time to realize.

Day 6:
* 6.1. Mostly a parsing problem, not very complicated.
* 6.2. I liked my solution a lot, basically I do an [unorthodox right-to-left transpose](https://github.com/giovannipcarvalho/aoc-2025/blob/master/day06/part2.py#L25-L27), and from there the solution becomes very easy to spot.  Meaningful trailing whitespace are quite the gotcha, though.

Day 7:
* 7.1. Simple walk through the grid.
* 7.2. I got stuck for a while and was too lazy to do anything elaborate, so I just cheesed a `@cache`d recursive solution.

Day 8:
* 8.1. Starting with graphs made it too much complex.  Checking and merging sets was simpler and nicer.
* 8.2. Too easy in comparison to part 1, or maybe I got lucky with my original solution being very easy to adapt for the second part.

Day 9:
* 9.1. Similar to yesterday's, but maximizing point distance rather than minimizing.
* 9.2. This was the steepest part1->part2 so far.  Fortunately checking if any perimeter (green tile) point is inside the square worked (~500k perimeter points).  I profiled it a bit and expected it to finish within ~15min, which it did.  Optimizing it to check line segments was much more annoying, because I kept getting the checks wrong... but it turned out much faster than I expected (considering that I am still checking all point pairs).
    * I was later made aware that there's a potential edge case (not present in the problem input) where this fails.  Oh, well.

Day 10:
* 10.1. Rather straight forward.  And what a timely coincidence to have watched [this](https://www.youtube.com/watch?v=4KdvcQKNfbQ) just a few days before this puzzle.
* 10.2. I only managed to "solve" (thanks, scipy) part 2 after day 12.

Day 11:
* 11.1. Graph traversal is fun as always.  Though thankfully there seems to be no cycles in the problem input, because even though I initially created a "seen" variable, I forgot entirely to populate it.
* 11.2. After OOM-ing a few times I once again cheesed a memoized dfs with `@functools.cache`.  I got it wrong a few times, but I like that I only keep track of the [relevant nodes](https://github.com/giovannipcarvalho/aoc-2025/blob/master/day11/part2.py#L38) along the way.

Day 12:
* 12.1. Parsing took me a while and I even got to implementing the rotations and flips.  I shamefully admit to have read that this one is solvable without actually solving, but I just had to see for myself.
