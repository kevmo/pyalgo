
```python
def algorithm_development(problem_specs):
    correct = False
    while not correct or not fast_enough(running_time):
        algorithm = devise_algorithm(problem_specs)
        correct = analyze_correctness(algorithm)
        running_time = analyze_efficiency(algorithm)
    return algorithm
```
