# pycloud / sparkhub

## Overview

pycloud / sparkhub is a Python package that provides a set of utilities for running spark pipelines on Google Cloud Platform (GCP) and in an on-prem cluster. It includes functions for generating Hail headers, running Hail pipelines on Dataproc clusters, and managing GCP resources.

## Main Features

- Generate Hail headers for use in Hail pipelines
- Run Hail pipelines on Dataproc clusters
- Manage GCP resources, such as Dataproc clusters and Google Cloud Storage buckets

## Installation

To install pycloud, you can use pip:

`pip install sparkhub`

## Usage

To use pycloud, you can import the relevant functions into your Python code:

```python
from pycloud.hailrunner import get_hail_header, HailRunnerGC, RunnerMagics
from pycloud.submit import *
```

Then, you can call the functions with the appropriate arguments to generate headers, run pipelines, and manage GCP resources.

## Maintainer

pycloud/sparkhub is maintained by TJ Singh. If you have any questions or issues, please contact him at <ts3475@cumc.columbia.edu>.
