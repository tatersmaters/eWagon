# eWagon: an esolang created by a 7th grader for no reason

## Intro

eWagon is an esoteric programming language based on queues and stacks. It stands for **E**solang **W**ithout **A** **Go**od **N**ame. It’s unique in that it has 2 storage modes: Queue Mode and Stack Mode. Using the `~` and `` ` `` commands pretty much dumps the contents of the queue into the stack, and vice versa, without changing the order. It also modifies the behavior of certain commands. Queue mode is activated by default when running a program.

## Commands

Every command will simply pop or dequeue however many arguments it needs from the argument queue, which is modified by the `%` and `^` commands (peek and pop/dequeue).

| Command      | What it does                                                                  |
| ----------   | ----------------------------------------------------------------------------- |
| `any number` | put an integer in the main queue/stack (ex.: 34 will enqueue 34)              |
| `%`          | peek at the front item of the queue or stack and put it in the argument queue |
| `^`          | pop or dequeue an item and put it in the argument queue                       |
| `+`          | add two values                                                                |
| `-`          | subtract two values                                                           |
| `*`          | multiply two values                                                           |
| `/`          | divide two values                                                             |
| `=`          | push/enqueue a truthy value if the two arguments are equal                    |
| `_`          | push/enqueue a truthy value if the two arguments are not equal                |
| `>`          | push/enqueue a truthy value if one argument is greater than the other         |
| `<`          | push/enqueue a truthy value if one argument is less than the other            |
| `“`          | enqueue or push the ASCII values of the characters between the `“”`           |
| `$`          | print a number with a newline                                                 |
| `@`          | print an ASCII value as a character with a newline                            |
| `#`          | print a number without a newline                                              |
| `!`          | print an ASCII value as a character without a newline                         |
| `&`          | get numerical input                                                           |
| `{`          | start a loop                                                                  |
| `}`          | if argument is truthy, break loop, otherwise, continue looping                |
| `[`          | if argument is truthy, execute the code between it and the next `]`           |
| `]`          | end an if-statement                                                           |
| `~`          | queue mode                                                                    |
| `` ` ``      | stack mode                                                                    |
| `.`          | end program                                                                   |

At the moment, eWagon doesn’t support nested if-statements. Feel free to modify the interpreter to your liking, however!

## The Interpreter

To use the interpreter, open the terminal (or command prompt if you're using Windows) and type this in the directory that `eWagon.py` is located:

`python eWagon.py [filename].ewg`

It should run under Python 2 or 3.

## Examples
Hello World:
`` "!dlrow ,olleH" { % ! "!" ^ ^ _ ^ } 0 ^ @ .`

**Fibonacci:**
``0 1 { ~ ^ % + % $ % ` 10000 ^ < ^ } .``

**Truth-machine:**
`& ^ [ { 1 ^ $ 1 ^ } ] 0 ^ $ .`

**Cat (numerical input only):**
`{ & ^ $ 1 ^ } .`

## Future Plans
This is a list of things I plan to implement.
* Modules and Add-ons
 * Modules will be written in eWagon
 * Add-ons will be Python modules loaded by the interpreter
* Functions
* Nested if-statements
* Character input