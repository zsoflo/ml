#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("Hello, World!")


# In[14]:


import os
import tarfile
from six.moves import urllib


# In[15]:


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
# the url of where I download the dataset from
HOUSING_PATH = os.path.join("datasets", "housing")
# the path for the specific housing dataset; I could join "datasets", "name_of_another_dataset"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
# the url for the specific housing data adds the root url to the path for the dataset that I want


# In[19]:


def fetch_housing_data(housing_url = HOUSING_URL, housing_path = HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
        # this creates a directory, "datasets/housing" in the workspace
    tgz_path = os.path.join(housing_path, "housing.tgz")
    # this joins the housing path "datasets/housing" with "housing.tgz"; "datasets/housing/housing.tgz"
    urllib.request.urlretrieve(housing_url, tgz_path)
    # retrieve from the github, the dataset, and save that to the tgz_path on my computer
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path = housing_path)
    housing_tgz.close()


# In[20]:


import pandas as pd
def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[23]:


housing = load_housing_data()
housing.head()
housing.info
