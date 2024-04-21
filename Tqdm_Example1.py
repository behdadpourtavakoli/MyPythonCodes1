import pandas as pd
import numpy as np
from tqdm import tqdm
from tqdm.gui import tqdm as tqdm_gui

df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
tqdm.pandas(ncols=50)  # can use tqdm_gui, optional kwargs, etc
# Now you can use `progress_apply` instead of `apply`
df.groupby(0).progress_apply(lambda x: x**2)
