#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint

p = 0.015  
q = 0.45
M = 50

years = np.arange(2024, 2034)

N0 = 0  

def bass_model(N, t, p, q, M):
    dNdt = (p * (M - N)) + (q * (N / M) * (M - N))
    return dNdt

N_t = odeint(bass_model, N0, years, args=(p, q, M))
N_t = N_t.flatten()  

adoption_df = pd.DataFrame({"Year": years, "Cumulative Market Adoption ($B)": N_t})

plt.figure(figsize=(10, 5))
plt.plot(years, N_t, marker='o', linestyle='-', color='b', label="Cumulative Adoption ($B)")
plt.xlabel("Year")
plt.ylabel("Cumulative Market Adoption ($B)")
plt.title("Forecasted Adoption of Small GEO Satellites (2024-2033)")
plt.legend()
plt.grid(True)
plt.show()

print(adoption_df)


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint


p = 0.015  
q = 0.45  
M = 50  

years = np.arange(2024, 2034)

N0 = 0  

def bass_model(N, t, p, q, M):
    dNdt = (p * (M - N)) + (q * (N / M) * (M - N))
    return dNdt

N_t = odeint(bass_model, N0, years, args=(p, q, M))
N_t = N_t.flatten()  

new_adopters = np.diff(N_t, prepend=0)

adoption_df = pd.DataFrame({"Year": years, "New Adopters ($B)": new_adopters, "Cumulative Adoption ($B)": N_t})

plt.figure(figsize=(10, 5))
plt.plot(years, N_t, marker='o', linestyle='-', color='b', label="Cumulative Adoption ($B)")
plt.xlabel("Year")
plt.ylabel("Cumulative Market Adoption ($B)")
plt.title("Forecasted Adoption of Small GEO Satellites (2024-2033)")
plt.legend()
plt.grid(True)
plt.show()

print(adoption_df.head()) 


# In[ ]:




