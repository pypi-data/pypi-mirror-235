import logging
import datasets
import pandas as pd
import numpy as np
from typing import Optional, Sequence
from dataclasses import dataclass
from . import (
    classifiers,
    conversations,
    loaders,
    filters,
    taggers,
    transforms,
    embedding,
    clustering,
    # minhash_lsh,
    visualize,
    # scraping,
)
from .base import GalacticDatasetBase

# set up logging
from .logger import setup_logger

setup_logger()
logger = logging.getLogger("galactic")


@dataclass
class GalacticDataset(GalacticDatasetBase):
    """
    This is the GalacticDataset class. It contains methods for loading data,
    filtering data, tagging data, transforming data, and classifying data.
    """

    dataset: datasets.Dataset
    model: Optional[object] = None
    emb_matrix: Optional[np.ndarray] = None
    cluster_ids: Optional[Sequence[int]] = None
    cluster_centers: Optional[dict[int, np.ndarray]] = None
    openai_api_key: Optional[str] = None
    max_tokens_per_minute: Optional[int] = 100000
    max_requests_per_minute: Optional[int] = 2000

    # attach all the imported methods
    ## loaders
    from_csv = classmethod(loaders.from_csv)
    from_jsonl = classmethod(loaders.from_jsonl)
    from_pandas = classmethod(loaders.from_pandas)
    from_parquet = classmethod(loaders.from_parquet)
    from_hugging_face = classmethod(loaders.from_hugging_face)
    from_hugging_face_stream = classmethod(loaders.from_hugging_face_stream)
    save = loaders.save
    to_pandas = loaders.to_pandas
    ## conversation utils
    conversation_from_dicts = conversations.conversation_from_dicts
    conversation_from_string = conversations.conversation_from_string
    convert_conversation_to_string = (
        conversations.convert_conversation_to_string
    )
    standardize_last_turn = conversations.standardize_last_turn
    get_conversation_length = conversations.get_conversation_length
    get_conversation_speakers = conversations.get_conversation_speakers
    is_alternating = conversations.is_alternating
    get_last_speaker = conversations.get_last_speaker
    get_shared_prefix = conversations.get_shared_prefix
    add_initial_system_message = conversations.add_initial_system_message
    take_initial_system_message = conversations.take_initial_system_message
    take_last_message = conversations.take_last_message
    ## filters
    filter_string = filters.filter_string
    filter_regex = filters.filter_regex
    apply_bloom_filter = filters.apply_bloom_filter
    ## taggers
    tag_string = taggers.tag_string
    tag_regex = taggers.tag_regex
    detect_language = taggers.detect_language
    detect_pii = taggers.detect_pii
    count_tokens = taggers.count_tokens
    calc_perplexity = taggers.calc_perplexity
    ai_tagger = taggers.ai_tagger
    ## transforms
    trim_whitespace = transforms.trim_whitespace
    unicode_normalize = transforms.unicode_normalize
    ai_column = transforms.ai_column
    ## classifiers
    ai_classifier = classifiers.ai_classifier
    fasttext_classifier = classifiers.fasttext_classifier
    embeddings_classifier = classifiers.embeddings_classifier
    train_fasttext_classifier = classifiers.train_fasttext_classifier
    train_embeddings_classifier = classifiers.train_embeddings_classifier
    ## embedding
    initialize_embedding_model = embedding.initialize_embedding_model
    get_embeddings = embedding.get_embeddings
    get_nearest_neighbors = embedding.get_nearest_neighbors
    reduce_embedding_dim = embedding.reduce_embedding_dim
    ## clustering
    cluster = clustering.cluster
    recompute_cluster_centers = clustering.recompute_cluster_centers
    _get_clusters = clustering._get_clusters
    remove_cluster = clustering.remove_cluster
    ai_label_clusters = clustering.ai_label_clusters
    get_cluster_info = clustering.get_cluster_info
    semdedup = clustering.semdedup
    ## minhash lsh

    ## visualizations
    plot_embeddings = visualize.plot_embeddings

    ## scraping
    # scrape_urls = scraping.scrape_urls
    # postprocess_scraped_pages = scraping.postprocess_scraped_pages

    def __post_init__(self):
        """
        Initializes the GalacticDataset instance.
        If '__id' does not exist in dataset columns, it is added.
        If the dataset contains cluster and embedding info but no cluster centers, they are set.
        If the dataset contains embeddings, the embedding matrix is set.
        Raises:
        ValueError: If the dataset contains duplicate __id values.
        """
        # add unique increaing int __id field if it doesn't already exist
        if "__id" not in self.dataset.column_names:
            self.dataset = self.dataset.map(
                lambda _, i: {"__id": i},
                with_indices=True,
            )
        elif "__id" in self.dataset.column_names:
            if len(self.dataset["__id"]) != len(set(self.dataset["__id"])):
                raise ValueError("Dataset contains duplicate __id values.")

    def __repr__(self):
        return pd.DataFrame(self.dataset.select(range(10))).__repr__()

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]

    # delegate basic stuff to the underlying Dataset object
    def __getattr__(self, name):
        if name in ["column_names", "features", "info"]:
            return getattr(self.dataset, name)
        elif name in ["filter", "map", "select", "shuffle", "select_columns"]:
            if name == "shuffle":
                logger.warning(
                    "Shuffling the dataset can be really expensive! Watch out!"
                )

            def wrapper(*args, **kwargs):
                result = getattr(self.dataset, name)(*args, **kwargs)
                if name == "shuffle":
                    result = result.flatten_indices()
                return GalacticDataset(
                    dataset=result,
                    model=self.model,
                    emb_matrix=self.emb_matrix,
                    cluster_ids=self.cluster_ids,
                    cluster_centers=self.cluster_centers,
                    openai_api_key=self.openai_api_key,
                )

            return wrapper

    def drop_column(
        self,
        column: str,
    ):
        """
        This method drops a column from the dataset.

        :param column: The column to drop.
        :type column: str
        """
        self.dataset = self.dataset.select_columns(
            [x for x in self.dataset.column_names if x != column]
        )

    def set_openai_key(self, key):
        """
        This method sets the OpenAI API key.

        :param key: The OpenAI API key.
        :type key: str
        """
        self.openai_api_key = key

    def set_rate_limits(self, **kwargs):
        if "max_tokens_per_minute" in kwargs:
            self.max_tokens_per_minute = kwargs["max_tokens_per_minute"]
        if "max_requests_per_minute" in kwargs:
            self.max_requests_per_minute = kwargs["max_requests_per_minute"]
