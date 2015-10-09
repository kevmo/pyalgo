## Python: *arguments & ** keyword arguments

```python
>>> def F(*args, **kwargs):
        for arg in args:
            print "Argument:", arg

        print "kwargs:", kwargs

>>> F("Brown", eyes="Blue")
Argument: Brown
{'eyes': 'Blue'}
```
