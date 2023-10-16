import unittest

import tsaugmentation as tsag

from gpforecaster.model.gpf import GPF
from gpforecaster.visualization.plot_predictions import plot_predictions_vs_original


class TestModel(unittest.TestCase):
    def setUp(self):
        self.dataset_name = "prison"
        self.data = tsag.preprocessing.PreprocessDatasets(self.dataset_name, freq='Q').apply_preprocess()
        self.n = self.data["predict"]["n"]
        self.s = self.data["train"]["s"]
        self.input_dir = "./results/gpf/"
        self.gpf = GPF(
            self.dataset_name,
            self.data,
            input_dir=self.input_dir,
            gp_type="sparse",
            inducing_points_perc=0.75,
        )
        self.gpf_svg = GPF(
            self.dataset_name,
            self.data,
            input_dir=self.input_dir,
            gp_type="svg",
            inducing_points_perc=0.75,
        )

    def test_sparse_gp(self):
        model, like = self.gpf.train(epochs=2)
        preds, preds_scaled = self.gpf.predict(model, like)
        plot_predictions_vs_original(
            dataset=self.dataset_name,
            prediction_mean=preds[0],
            prediction_std=preds[1],
            origin_data=self.gpf.original_data,
            inducing_points=self.gpf.inducing_points,
            x_original=self.gpf.train_x.numpy(),
            x_test=self.gpf.test_x.numpy(),
            x_complete=self.gpf.complete_x,
            n_series_to_plot=8,
            gp_type=self.gpf.gp_type,
        )
        self.gpf.plot_losses(5)
        self.gpf.metrics(preds[0], preds[1])
        self.gpf.store_results(preds[0], res_measure="mean", res_type="fitpred")
        self.gpf.store_results(preds[0], res_measure="mean", res_type="pred")
        self.gpf.store_results(preds[1], res_measure="std", res_type="fitpred")
        self.gpf.store_results(preds[1], res_measure="std", res_type="pred")
        self.assertLess(self.gpf.loss_tracker.data.train.weighted[-1], 20)

    def test_svg(self):
        model, like = self.gpf_svg.train(epochs=2)
        preds, preds_scaled = self.gpf_svg.predict(model, like)
        plot_predictions_vs_original(
            dataset=self.dataset_name,
            prediction_mean=preds[0],
            prediction_std=preds[1],
            origin_data=self.gpf_svg.original_data,
            inducing_points=self.gpf_svg.inducing_points,
            x_original=self.gpf_svg.train_x.numpy(),
            x_test=self.gpf_svg.test_x.numpy(),
            x_complete=self.gpf_svg.complete_x,
            n_series_to_plot=8,
            gp_type=self.gpf_svg.gp_type,
        )
        self.gpf_svg.plot_losses(5)
        self.gpf_svg.metrics(preds[0], preds[1])
        self.gpf_svg.store_results(preds[0], res_measure="mean", res_type="fitpred")
        self.gpf_svg.store_results(preds[0], res_measure="mean", res_type="pred")
        self.gpf_svg.store_results(preds[1], res_measure="std", res_type="fitpred")
        self.gpf_svg.store_results(preds[1], res_measure="std", res_type="pred")
        self.assertLess(self.gpf_svg.loss_tracker.data.train.weighted[-1], 20)

