import unittest
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess

from lowess_grouped.lowess_grouped import lowess_grouped

DATA_DIR = Path(__file__).parent / "data"


class TestLowessGrouped(unittest.TestCase):
    def setUp(self):
        # load the data before each test
        self.temp_region = pd.read_csv(DATA_DIR / "temperature-by-region.csv")

    def test_lowess_has_no_side_effects(self):
        """
        Test if function lowess_grouped() has no side effects (i.e. does not change the input dataframe)
        """
        temp_region_copy = self.temp_region.copy()

        lowess_grouped(self.temp_region, "year", "temperature_anomaly", "region_name", frac=0.05)

        self.assertTrue(
            self.temp_region.equals(temp_region_copy),
            "lowess_grouped seems to change the input dataframe"
        )

    def test_lowess_for_multiple_groups(self):
        """
        Test if lowess smoothing works correctly for multiple groups
        """

        # smooth data with lowess-grouped
        lowess_grouped_output = lowess_grouped(
            self.temp_region,
            "year",
            "temperature_anomaly",
            "region_name",
            frac=0.05
        )

        # foreach region (aka group), check if lowess-grouped produces the same output as statmodels lowess()
        groups = self.temp_region["region_name"].unique().tolist()
        for group in groups:
            temp_region_subset = self.temp_region[self.temp_region["region_name"] == group]

            # get smoothed values from statsmodels lowess, for this region:
            smooth_values_statsmodels: np.ndarray = lowess(temp_region_subset["temperature_anomaly"],
                                                           temp_region_subset["year"], frac=0.05)[:, 1]

            # get smoothed values from lowess-grouped, for this region:
            smooth_values_lowess_grouped = lowess_grouped_output[lowess_grouped_output["region_name"] == group][
                "temperature_anomaly_smooth"].to_numpy()

            self.assertTrue(
                np.array_equal(smooth_values_statsmodels, smooth_values_lowess_grouped),
                f"lowess-grouped values are different from statmodels lowess, for region {group}"
            )

    def test_lowess_for_single_groups(self):
        """
        Test if lowess smoothing works correctly for a single group
        """

        # foreach region (aka group), check if lowess-grouped produces the same output as statmodels lowess()
        groups = self.temp_region["region_name"].unique().tolist()
        for group in groups:
            temp_region_subset = self.temp_region[self.temp_region["region_name"] == group]

            # get smoothed values from statsmodels lowess, for this region:
            smooth_values_statsmodels: np.ndarray = lowess(temp_region_subset["temperature_anomaly"],
                                                           temp_region_subset["year"], frac=0.05)[:, 1]

            # get smoothed values from lowess-grouped, for this region:
            smooth_values_lowess_grouped = \
                lowess_grouped(temp_region_subset, "year", "temperature_anomaly", None, frac=0.05)[
                    "temperature_anomaly_smooth"].to_numpy()

            self.assertTrue(
                np.array_equal(smooth_values_statsmodels, smooth_values_lowess_grouped),
                f"lowess-grouped values are different from statmodels lowess, for region {group}"
            )


class TestSmoothingSuffix(unittest.TestCase):
    def setUp(self):
        # load the data before each test
        self.temp_region = pd.read_csv(DATA_DIR / "temperature-by-region.csv")

    def test_str_suffix_str_y_name(self):
        """
        Test using a string as smoothed_col_suffix, when y_name is also a string
        """
        self.temp_region = lowess_grouped(self.temp_region, "year", "temperature_anomaly", "region_name",
                                          smoothed_col_suffix="_smooth2", frac=0.05)

        column_names = list(self.temp_region.columns)
        self.assertTrue(
            "temperature_anomaly_smooth2" in column_names,
            "Smoothed column has either wrong name, or does not exist")

    def test_tuple_suffix_str_y_name(self):
        """
        Test using a tuple as smoothed_col_suffix, when y_name is a string
        """
        with self.assertRaises(ValueError) as cm:
            lowess_grouped(self.temp_region, "year", "temperature_anomaly", "region_name",
                           smoothed_col_suffix=("_smooth2", "_smooth3"), frac=0.05)

        self.assertEqual(str(cm.exception), "If type of y_name is string then smoothed_col_suffix must also be string")

    def test_str_suffix_tuple_y_name(self):
        """
        Test using a string as smoothed_col_suffix, when y_name is a tuple
        """
        self.temp_region = self.temp_region.rename(columns={'temperature_anomaly': ('temperature_anomaly', 'median')})

        self.temp_region = lowess_grouped(self.temp_region, "year", ('temperature_anomaly', 'median'), "region_name")

        column_names = list(self.temp_region.columns)
        self.assertTrue(
            ('temperature_anomaly_smooth', 'median') in column_names,
            "Smoothed column has either wrong name, or does not exist")

    def test_tuple_suffix_tuple_y_name(self):
        """
        Test using a tuple as smoothed_col_suffix, when y_name is a tuple of the same length
        """
        self.temp_region = self.temp_region.rename(columns={'temperature_anomaly': ('temperature_anomaly', 'median')})

        self.temp_region = lowess_grouped(self.temp_region, "year", ('temperature_anomaly', 'median'),
                                          "region_name", smoothed_col_suffix=('_smooth1', '_smooth2'))

        column_names = list(self.temp_region.columns)
        self.assertTrue(
            ('temperature_anomaly_smooth1', 'median_smooth2') in column_names,
            "Smoothed column has either wrong name, or does not exist")

    def test_tuple_suffix_wrong_length(self):
        """
        Test using a tuple as smoothed_col_suffix, when y_name is a tuple with a different length
        """
        temp_region = self.temp_region.rename(columns={'temperature_anomaly': ('temperature_anomaly', 'median')})

        with self.assertRaises(ValueError) as cm:
            lowess_grouped(temp_region, "year", ('temperature_anomaly', 'median'), "region_name",
                           smoothed_col_suffix=('_smooth1', '_smooth2', '_smooth3'))

        self.assertEqual(str(cm.exception), "Tuple of smoothed_col_suffix must have same length as tuple of y_name")


if __name__ == '__main__':
    unittest.main()
