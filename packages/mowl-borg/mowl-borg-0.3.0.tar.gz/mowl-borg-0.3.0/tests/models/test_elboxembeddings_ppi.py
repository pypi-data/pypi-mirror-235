from unittest import TestCase

from tests.datasetFactory import PPIYeastSlimDataset
from mowl.models.elboxembeddings.examples.model_ppi import ELBoxPPI
import pytest

class TestELBoxEmbeddingsPPI(TestCase):

    @pytest.mark.slow
    def test_ppi(self):
        """Test ELBoxEmbeddings on PPI dataset. The test is not very strict, it just checks the \
correct syntax of the code."""

        dataset = PPIYeastSlimDataset()
        model = ELBoxPPI(dataset, epochs=1, embed_dim=2)
        return_value = model.train()
        self.assertEqual(return_value, 1)
