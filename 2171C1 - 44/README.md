Explanation

This is a turn-based game problem where two players, Ajisai and Mai, play optimally under strict constraints.

Ajisai moves on odd-numbered turns, and Mai moves on even-numbered turns.
A player is allowed to swap elements only at positions whose parity matches their turn.

The key observation is that only the parity of positions matters, not the exact sequence of moves.
Since both players play optimally, the game outcome depends on how many positions each player can influence.

By analyzing the array under these parity constraints, we can reduce the problem to checking which player has a winning advantage based on the current configuration.
This avoids simulating individual moves and instead relies on evaluating the game state directly.

Using this observation, the solution runs in linear time O(n), which easily satisfies the constraints even for very large arrays (up to 10^6 elements)