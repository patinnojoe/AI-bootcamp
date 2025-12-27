import pandas as pd

s = pd.Series([1,2,3], index=["a", "b", "c"])
data = {
    "names": ['patrick', 'josiah', 'innocent'],
    'ages':  [10, 20, 30,40]
}

print(pd.DataFrame(data))