"""
mlte/value/artifact.py

Artifact implementation for MLTE values.
"""

from __future__ import annotations

import abc

from mlte.artifact.artifact import Artifact
from mlte.artifact.model import ArtifactModel
from mlte.artifact.type import ArtifactType
from mlte.evidence.metadata import EvidenceMetadata


class Value(Artifact, metaclass=abc.ABCMeta):
    """
    The Value class serves as the base class of all
    semantically-enriched measurement evaluation values.
    The Value provides a common interface for inspecting
    the results of measurement evaluation, and also
    encapsulates the functionality required to uniquely
    associate evaluation results with the originating measurement.
    """

    def __init__(self, instance: Value, metadata: EvidenceMetadata):
        """
        Initialize a Value instance.
        :param instance: The subclass instance
        :param metadata: Evidence metadata associated with the value
        """
        identifier = f"{metadata.identifier}.value"
        super().__init__(identifier, ArtifactType.VALUE)

        self.metadata = metadata
        """Evidence metadata associated with the value."""

        self.typename: str = type(instance).__name__
        """The type of the value itself."""

    def to_model(self) -> ArtifactModel:
        """
        Convert a value artifact to its corresponding model.
        NOTE: To cope with polymorphism, the Value artifact type
        does not define this required method itself; instead, it
        is delegated to subclasses that implement concrete types
        """
        raise NotImplementedError("Value.to_mode()")

    @classmethod
    def from_model(cls, _: ArtifactModel) -> Value:  # type: ignore[override]
        """
        Convert a value model to its corresponding artifact.
        NOTE: To cope with polymorphism, the Value artifact type
        does not define this required method itself; instead, it
        is delegated to subclasses that implement concrete types
        """
        raise NotImplementedError("Value.from_model()")
