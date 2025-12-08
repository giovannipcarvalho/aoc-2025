# aoc-2025

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
