from johnsnowlabs import try_import_lib

if try_import_lib("haystack"):
    from johnsnowlabs.llm_frameworks.haystack_node import (
        _JohnsnowlabsEmbeddingEncoder,
        JohnsnowlabsEmbeddingRetriever,
    )

if try_import_lib("langchain"):
    from johnsnowlabs.llm_frameworks.langchain_node import (
        JohnSnowLabsEmbeddings as JslLangchainEmbedder,
    )


if not try_import_lib("langchain") and not try_import_lib("haystack"):
    print(
        "Install either langchain or haystack and restart your python kernel to use the llm module!"
    )
