"""
Cores em python.
ANSI escape sequence.

\033[style; text; backgroundm
style:
0 - none
1 - bold
4 - underline
7 - negative

Text
30 - white
31 - red
32 - green
33 - yellow
34 - blue
35 - purple
36 - cyan
37 - gray

Back
40 - white
41 - red
42 - green
43 - yellow
44 - blue
45 - purple
46 - cyan
47 - gray

\33[0;30;41m
\33[4;33;44m
\33[1;35;43m
\33[30;42m
\33[m
\33[7;30m
"""

print("\33[7;30mOlá, mundo!")
