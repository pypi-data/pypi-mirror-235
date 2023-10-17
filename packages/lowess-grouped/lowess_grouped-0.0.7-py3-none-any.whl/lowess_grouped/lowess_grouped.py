from typing import Union, Literal, Tuple

import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess


def _add_suffix(
        y_name: Union[str, Tuple[str, ...]],
        smoothed_col_suffix: Union[str, Tuple[str, ...]]
) -> Union[str, Tuple[str, ...]]:

    if type(y_name) is str:
        if type(smoothed_col_suffix) is str:
            return y_name + smoothed_col_suffix
        else:
            raise ValueError("If type of y_name is string then smoothed_col_suffix must also be string")
    elif type(y_name) is tuple:
        if type(smoothed_col_suffix) is str:
            return (y_name[0] + smoothed_col_suffix,) + (y_name[1:])
        elif type(smoothed_col_suffix) is tuple:
            if len(y_name) == len(smoothed_col_suffix):
                return tuple(x + y for x, y in zip(y_name, smoothed_col_suffix))
            else:
                raise ValueError("Tuple of smoothed_col_suffix must have same length as tuple of y_name")
        else:
            raise ValueError("Type of smoothed_col_suffix not supported")
    else:
        raise ValueError("Type of y_name not supported")


def lowess_grouped(
        data: pd.DataFrame,
        x_name: Union[str, Tuple[str, ...]],
        y_name: Union[str, Tuple[str, ...]],
        group_name: Union[str, Tuple[str, ...], None],
        smoothed_col_suffix: Union[str, Tuple[str, ...]] = "_smooth",
        frac: float = 0.6666666666666666,
        it: int = 3,
        delta: float = 0.0,
        is_sorted: bool = False,
        missing: Literal['none', 'drop', 'raise'] = 'drop',
        return_sorted: bool = True
) -> pd.DataFrame:
    """
    Applies lowess smoothing to each group.
    If no group is supplied, lowess will be applied to the whole dataset.

    :param data: Input dataframe containing the data to be smoothed.
    :param x_name: Name of the column representing the independent variable (x-axis).
    :param y_name: Name of the column representing the dependent variable (y-axis).
    :param group_name: Name of the column indicating the group for the groupwise smoothing. If None, smoothing will be applied to the entire dataset.
    :param smoothed_col_suffix: Suffix to be added to the column name of the smoothed y-values.
    :param frac: How strongly to smooth the data. Between 0 and 1. Specifically the fraction of the data used when smoothing each y-value.
    :param it: Number of residual-based reweightings to perform.
    :param delta: Distance within which to use linear-interpolation instead of weighted regression.
    :param is_sorted: If False, then the data will be sorted by x-values before calculating lowess. If True, then it is assumed that the data is already sorted by x-values.
    :param missing: If 'none', no nan checking is done. If 'drop', any observations with nans are dropped. If 'raise', an error is raised.
    :param return_sorted: If True, then the returned array is sorted by x-values and has missing (nan or infinite) observations removed. If False, then the returned array is in the same length and the same sequence of observations as the input array.
    :return: Copy of the original dataframe, with a new column added for the smoothed y-values.
    """

    # copy dataframe so that the function input is not changed (= side effect)
    df = data.copy()

    # create name for the new column containing the smoothed data
    y_name_smoothed = _add_suffix(y_name, smoothed_col_suffix)

    # smooth the data in column y_name accordingly
    if group_name is not None:
        groups = df[group_name].unique().tolist()
        smoothed_dfs = []
        for group in groups:
            df_by_select_group = df[df[group_name] == group]
            smoothed_df = lowess(
                df_by_select_group[y_name],
                df_by_select_group[x_name],
                frac=frac,
                it=it,
                delta=delta,
                is_sorted=is_sorted,
                missing=missing,
                return_sorted=return_sorted
            )
            smoothed_df = pd.DataFrame(smoothed_df, columns=[x_name, y_name_smoothed])
            smoothed_df[group_name] = group
            smoothed_dfs.append(smoothed_df)
        return pd.merge(df, pd.concat(smoothed_dfs), how="left", on=[x_name, group_name])
    else:
        smoothed_df = lowess(
            df[y_name],
            df[x_name],
            frac=frac,
            it=it,
            delta=delta,
            is_sorted=is_sorted,
            missing=missing,
            return_sorted=return_sorted
        )
        smoothed_df = pd.DataFrame(smoothed_df, columns=[x_name, y_name_smoothed])
        return pd.merge(df, smoothed_df, how="left", on=x_name)
