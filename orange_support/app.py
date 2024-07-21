from Orange.data.pandas_compat import table_to_frame, table_from_frame
import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def find_contraint_beta_prior(lower, upper, mass=0.95):
    assert lower > 0 and lower < upper, "lower bound should be between 0 and upper"
    assert upper > lower and upper < 1 , "upper bound should be between lower and 1"
    mu = (lower + upper) * 0.5
    sigma = (mu * (1-mu)) ** 0.5  # first term is an upper bound  so should be smaller
    sigma = min(mu, sigma) # should not to be too wide as initial guess
    out = pm.find_constrained_prior(pm.Beta,lower, upper,  dict(mu=mu, sigma=sigma),mass=mass)
    return out


class OrangeApp:
    def to_df(self, data, include_metas=True):
        return table_to_frame(data, include_metas=include_metas)

    def from_df(self, df):
        return table_from_frame(df)

    def describe(self, data, percentiles=[ 0.025, 0.050, 0.100, 0.200, 0.500, 0.800, 0.900, 0.950, 0.975]):
        return self.to_df(data).describe(percentiles=percentiles).round(3).pipe(self.from_df)

    def run(self, func, *args):
        """
        Transform input data to pandas DataFrame, run the function, and transform the output back to Orange data
        Acts as an adapter between orange and application.
        """
        out = None

        if len(args) == 0:
            df_out = func(self)
        else:
            in_data = args[0]
            df = self.to_df(in_data)
            df_out = func(self, df)

        if df_out is not None:
            out = self.from_df(df_out)
        return out

def create_app():
    app = OrangeApp()
    return app

app  = create_app()
