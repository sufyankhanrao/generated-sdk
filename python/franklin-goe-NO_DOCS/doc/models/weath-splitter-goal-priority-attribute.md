
# Weath Splitter Goal Priority Attribute

Defines the importance a goal holds for a specific user. Order of priority is Need > Want > Wish > Dream <br>         goalPriority can be from 1 to 4 levels. However, note that Goal priority defines the target probabilities and the loss threshold values.<br>         For example, goals with a higher priority (e.g. Need) would have a higher target goal probability (85%) with a higher (aggressive) loss threshold value (slightly more than IW value) in the current set-up.<br>         This needs to be re-mapped based on the number of goal-priority levels, in case of a change.

*This model accepts additional fields of type Any.*

## Enumeration

`WeathSplitterGoalPriorityAttribute`

## Fields

| Name |
|  --- |
| `NEED` |
| `WANT` |
| `WISH` |
| `DREAM` |

## Example

```
Need
```

