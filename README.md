# Conversion of Non-Deterministic Finite Automata (NFA) to Deterministic Finite Automata (DFA)

A script written in python that converts a given .txt file describing a NFA to DFA. The file must be formated as follows:

| Line | Contains |
|:---:|:---:|
| 1 | number of states |
| 2 | alphabet |
| 3 | Initial state |
| 4 | Final state |
| rest | Transitions |

The input file must describe every state with the use of a **single** character (0, 1, A, B, q, r). The `∅` symbol is represented with `_` in the output DFA.txt file.

The script also prints out a dictionary where the key is the state and the values are the result states for every symbol in the alphabet. For example for an alphabet containing two symbols, from state A the first symbol transitions to state AB and the second symbol transitions to state B the program would print: `{ 'A': ['AB', 'B'] }`.

Below are three examples of how to convert the graphical representation of a NFA to an acceptable input, note that there is no need for the comments in the input file.


### Example 1
![image](https://user-images.githubusercontent.com/70406237/218232515-c98928d5-8c15-488a-b868-de5ef85711cb.png)

`NFA.txt:`
```
3       // Number of states
01      // Alphabet
0       // Initial state
2       // Final state
001     // From state 0 with input 0 next state is 1
000     // From state 0 with input 0 next state is 0
010     // From state 0 with input 1 next state is 0
112     // From state 1 with input 1 next state is 2
```
`DFA.txt` output:
```
3		//Number of states
01		// 2 symbols in the alphabet
0		// Initial state(s)
02 		// Final state(s)
0 0 01		// From state 0 with input 0 next state is 01
0 1 0		// From state 0 with input 1 next state is 0
01 0 01		// From state 01 with input 0 next state is 01
01 1 02		// From state 01 with input 1 next state is 02
02 0 01		// From state 02 with input 0 next state is 01
02 1 0		// From state 02 with input 1 next state is 0
```

### Example 2

![image](https://user-images.githubusercontent.com/70406237/218233178-12925109-79ff-416e-9bbc-1d004852b48e.png)

`NFA.txt:`

```
2       // Number of state
01      // Alphabet
A       // Initial state
A       // Final state
A0B     // From state A with input 0 next state is B
A0A     // From state A with input 0 next state is A
A1B     // From state A with input 1 next state is B
B1A     // From state B with input 1 next state is A
```
`DFA.txt`
```
3		//Number of states
01		// 2 symbols in the alphabet
A		// Initial state(s)
A AB 		// Final state(s)
A 0 AB		// From state A with input 0 next state is AB
A 1 B		// From state A with input 1 next state is B
AB 0 AB		// From state AB with input 0 next state is AB
AB 1 AB		// From state AB with input 1 next state is AB
B 0 _		// From state B with input 0 next state is _
B 1 A		// From state B with input 1 next state is A
```

### Example 3

![image](https://user-images.githubusercontent.com/70406237/218233765-8f219b8d-284c-4494-a39f-47fb52ce59a1.png)

`NFA.txt:`
```
4
01
p
s
p0p
p1p
p0q
q0r
q1r
r0s
s0s
s1s
```
`DFA.txt`
```
8		//Number of states
01		// 2 symbols in the alphabet
p		// Initial state
pqrs pqs prs ps // Final state(s)
p 0 pq		// From state p with input 0 next state is pq
p 1 p		// From state p with input 1 next state is p
pq 0 pqr	// From state pq with input 0 next state is pqr
pq 1 pr		// From state pq with input 1 next state is pr
pqr 0 pqrs	// From state pqr with input 0 next state is pqrs
pqr 1 pr	// From state pqr with input 1 next state is pr
pr 0 pqs	// From state pr with input 0 next state is pqs
pr 1 p	        // From state pr with input 1 next state is p
pqrs 0 pqrs	// From state pqrs with input 0 next state is pqrs
pqrs 1 prs	// From state pqrs with input 1 next state is prs
pqs 0 pqrs	// From state pqs with input 0 next state is pqrs
pqs 1 prs	// From state pqs with input 1 next state is prs
prs 0 pqs	// From state prs with input 0 next state is pqs
prs 1 ps	// From state prs with input 1 next state is ps
ps 0 pqs	// From state ps with input 0 next state is pqs
ps 1 ps		// From state ps with input 1 next state is ps

```
