
[RegEx](https://regexone.com/lesson/introduction_abcs)



`\d` = ONE character from 0-9, ONE DIGIT
> e.g. `\d\d` =  TWO characters from 0-9,  TWO DIGITs

`.` = match any single character

`\.` = match dot

`[a]` == match only `a`

`^a` = NOT start with charater
> e.g. [^a].

`-` range
> e.g.
> [2-4] ==  in [2,3,4] == in range 2 to 4
> 
> [^a-b] == not a through b == not a or b

## meta character `\w`
`\w` == charcter in [A-Za-z0-9_]

## repetitions {n}
u want to `\d\d\d` ? 

f~~uck~~orget that..

Do: \d{3} = \d\d\d
> e.g:  www.com == w{3}\.com

> :memo: **note**: Certain regular expression engines will even allow you to specify a *range*.
> e.g.: w{1,3}
> 
> [\w]{1,3}  .{2,6}


# Kleene Star (Start or Plus, name convention only)
| follows | symbol |
| - | - |
| * | 0-> any |
| + | 1 -> any |

# meta character : optionality `?`














