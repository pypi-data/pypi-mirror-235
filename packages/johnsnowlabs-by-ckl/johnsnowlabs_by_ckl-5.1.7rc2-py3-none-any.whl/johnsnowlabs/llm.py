from johnsnowlabs import try_import_lib

if try_import_lib("haystack"):
    from llm_frameworks.haystack_node import (
        _JohnsnowlabsEmbeddingEncoder,
        JohnsnowlabsEmbeddingRetriever,
    )

if try_import_lib("langchain"):
    pass
    # from llm_frameworks.haystack_node import _JohnsnowlabsEmbeddingEncoder


if not try_import_lib("langchain") and not try_import_lib("haystack"):
    print(
        "Install either langchain or haystack and restart your python kernel to use the llm module!"
    )
