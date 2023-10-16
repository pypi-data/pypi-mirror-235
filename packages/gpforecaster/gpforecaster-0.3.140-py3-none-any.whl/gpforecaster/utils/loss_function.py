from typing import Dict, Union, Tuple, Optional, Any, List
from dataclasses import dataclass
import numpy as np
from collections import namedtuple


@dataclass
class EpochLossLevels:
    """Container to hold epoch-wise losses for each fold for each level."""

    weighted: List[List[float]]
    upper: Optional[List[List[float]]] = None
    bottom: Optional[List[List[float]]] = None


@dataclass
class LossLevels:
    """Container to hold fold-wise losses for each level."""

    weighted: List[float]
    upper: Optional[List[float]] = None
    bottom: Optional[List[float]] = None

    def average(self, level: str) -> float:
        """
        Compute average of the specified level's losses.

        Args:
            level (str): Name of the level ('weighted', 'upper', or 'bottom').

        Returns:
            float: Average loss.
        """
        losses = getattr(self, level)
        return sum(losses) / len(losses) if losses else 0.0


LossData = namedtuple("LossData", ["train", "val", "test"])


class LossTracker:
    """Track and manage losses for training, validation, and testing processes."""

    def __init__(self):
        """Initialize loss containers for train, val, and test."""
        self.data = LossData(
            train=LossLevels([], [], []),
            val=LossLevels([], [], []),
            test=LossLevels([], [], []),
        )

        self.epoch_data = LossData(
            train=EpochLossLevels([], [], []),
            val=EpochLossLevels([], [], []),
            test=EpochLossLevels([], [], []),
        )

    def add_epoch_loss(
        self,
        fold_idx: int,
        loss_type: str,
        weighted: float,
        upper: Optional[float] = None,
        bottom: Optional[float] = None,
    ):
        """
        Add epoch's loss for a specific fold, type, and level.

        Args:
            fold_idx (int): Index of the fold.
            loss_type (str): Type of the loss ('train', 'val', 'test').
            weighted (float): Loss value for the 'weighted' level.
            upper (Optional[float], optional): Loss value for the 'upper' level. Defaults to None.
            bottom (Optional[float], optional): Loss value for the 'bottom' level. Defaults to None.
        """
        loss_level = getattr(self.epoch_data, loss_type)

        while len(loss_level.weighted) <= fold_idx:
            loss_level.weighted.append([])
            loss_level.upper.append([])
            loss_level.bottom.append([])

        loss_level.weighted[fold_idx].append(weighted)
        if upper is not None:
            loss_level.upper[fold_idx].append(upper)
        if bottom is not None:
            loss_level.bottom[fold_idx].append(bottom)

    def add_fold_loss(self, fold_idx: int):
        """
        Store the final epoch's loss for a specific fold and loss type.

        Args:
            fold_idx (int): Index of the fold.
        """
        for loss_type in ["train", "val", "test"]:
            loss_level = getattr(self.data, loss_type)
            epoch_loss_level = getattr(self.epoch_data, loss_type)
            # Ensure we have recorded epoch losses for this fold
            if len(epoch_loss_level.weighted) > fold_idx:

                # Fetch the last epoch's loss for this fold and store it
                loss_level.weighted.append(epoch_loss_level.weighted[fold_idx][-1])

                if loss_type != "train":
                    if (
                        epoch_loss_level.upper
                        and len(epoch_loss_level.upper) > fold_idx
                    ):
                        loss_level.upper.append(epoch_loss_level.upper[fold_idx][-1])

                    if (
                        epoch_loss_level.bottom
                        and len(epoch_loss_level.bottom) > fold_idx
                    ):
                        loss_level.bottom.append(epoch_loss_level.bottom[fold_idx][-1])
            else:
                raise ValueError(
                    f"No epoch losses recorded for fold {fold_idx} and loss type {loss_type}."
                )

    def get_average_loss(self, loss_type: str, level: str) -> float:
        """
        Retrieve the average loss for a specific type and level.

        Args:
            loss_type (str): Type of the loss ('train', 'val', 'test').
            level (str): Level of the loss ('weighted', 'upper', 'bottom').

        Returns:
            float: Average loss.
        """
        return getattr(self.data, loss_type).average(level)

    def log_average_losses(self, logger):
        """
        Log average losses for all types and levels.

        Args:
            logger: Logging object.
        """
        logger.info('Finished training for all folds.\n')
        logger.info('Average results:')
        for loss_type in ["train", "val", "test"]:
            for level in ["weighted", "upper", "bottom"]:
                logger.info(
                    f"Average {loss_type} loss ({level}): {np.round(self.get_average_loss(loss_type, level),3)}"
                )

    def log_loss_details(self, fold_idx: int, epoch: int, logger, verbose: bool):
        """
        Log loss details for a specific type, fold, and epoch.

        Args:
            fold_idx (int): Index of the fold.
            epoch (int): Current epoch.
            logger: Logging object.
        """
        msg = f"Fold {fold_idx + 1} - Epoch {epoch}"
        for loss_type in ["train", "val", "test"]:
            loss_levels = getattr(self.epoch_data, loss_type)

            msg += (
                f" | {loss_type.capitalize()} Loss:"
                f" Weighted: {np.round(loss_levels.weighted[fold_idx][-1], 3)}"
            )
            if verbose and loss_type != "train":
                msg += (
                    f", Upper: {np.round(loss_levels.upper[fold_idx][-1] if loss_levels.upper else 0, 3)},"
                    f" Bottom: {np.round(loss_levels.bottom[fold_idx][-1] if loss_levels.bottom else 0, 3)}"
                )

        logger.info(msg)
