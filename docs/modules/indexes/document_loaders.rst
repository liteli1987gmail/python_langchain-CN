文档加载器
==========================



.. 注意::   `概念指南 <https://docs.langchain.com/docs/components/indexing/document-loaders>`_
   `Conceptual Guide <https://docs.langchain.com/docs/components/indexing/document-loaders>`_





将语言模型与您自己的文本数据结合使用是区分它们的强大方法。第一步是将数据加载到\"文档\"中 - 一种花式说一些文本片段的方式。文档加载器旨在使此过程变得简单。
The first step in doing this is to load the data into "Documents" - a fancy way of say some pieces of text.

The document loader is aimed at making this easy.





提供以下文档加载器:




转换加载器
------------------------------



** 转换 ** 加载器将数据从特定格式转换为文档格式。例如，有适用于 CSV 和 SQL 的 ** 转换器 **。通常，这些加载器从文件中输入数据，但有时也会从 URL 中输入数据。
For example, there are **transformers** for CSV and SQL.

Mostly, these loaders input data from files but sometime from URLs.



许多这些转换器的主要驱动程序是 `Unstructured <https://github.com/Unstructured-IO/unstructured>`_ python 包。此软件包将许多类型的文件 - 文本、PowerPoint、图像、HTML、PDF 等 - 转换为文本数据。
This package transforms many types of files - text, powerpoint, images, html, pdf, etc - into text data.



有关如何设置 Unstructured 的详细说明，请参见 `此处 <https://github.com/Unstructured-IO/unstructured#coffee-getting-started>`_ 中的安装指南。




.. toctree::

   :maxdepth: 1

   :glob:



   ./document_loaders/examples/airtable.ipynb

   ./document_loaders/examples/audio.ipynb

   ./document_loaders/examples/conll-u.ipynb

   ./document_loaders/examples/copypaste.ipynb

   ./document_loaders/examples/csv.ipynb

   ./document_loaders/examples/email.ipynb

   ./document_loaders/examples/epub.ipynb

   ./document_loaders/examples/evernote.ipynb

   ./document_loaders/examples/excel.ipynb

   ./document_loaders/examples/facebook_chat.ipynb

   ./document_loaders/examples/file_directory.ipynb

   ./document_loaders/examples/html.ipynb

   ./document_loaders/examples/image.ipynb

   ./document_loaders/examples/jupyter_notebook.ipynb

   ./document_loaders/examples/json.ipynb

   ./document_loaders/examples/markdown.ipynb

   ./document_loaders/examples/microsoft_powerpoint.ipynb

   ./document_loaders/examples/microsoft_word.ipynb

   ./document_loaders/examples/odt.ipynb

   ./document_loaders/examples/pandas_dataframe.ipynb

   ./document_loaders/examples/pdf.ipynb

   ./document_loaders/examples/sitemap.ipynb

   ./document_loaders/examples/subtitle.ipynb

   ./document_loaders/examples/telegram.ipynb

   ./document_loaders/examples/toml.ipynb

   ./document_loaders/examples/unstructured_file.ipynb

   ./document_loaders/examples/url.ipynb

   ./document_loaders/examples/web_base.ipynb

   ./document_loaders/examples/weather.ipynb

   ./document_loaders/examples/whatsapp_chat.ipynb







公共数据集或服务加载器
----------------------------------

这些数据集和来源是为公共领域创建的，我们使用查询搜索并下载必要的文档。例如，**Hacker News** 服务。
and download necessary documents.

For example, **Hacker News** service.



我们不需要访问这些数据集和服务的任何访问权限。




.. toctree::

   :maxdepth: 1

   :glob:



   ./document_loaders/examples/arxiv.ipynb

   ./document_loaders/examples/azlyrics.ipynb

   ./document_loaders/examples/bilibili.ipynb

   ./document_loaders/examples/college_confidential.ipynb

   ./document_loaders/examples/gutenberg.ipynb

   ./document_loaders/examples/hacker_news.ipynb

   ./document_loaders/examples/hugging_face_dataset.ipynb

   ./document_loaders/examples/ifixit.ipynb

   ./document_loaders/examples/imsdb.ipynb

   ./document_loaders/examples/mediawikidump.ipynb

   ./document_loaders/examples/wikipedia.ipynb

   ./document_loaders/examples/youtube_transcript.ipynb





专有数据集或服务加载器
--------------------------------------

这些数据集和服务不来自公共领域。这些加载器主要将数据从特定应用程序或云服务的格式转换为文本数据，例如** Google Drive **。
These loaders mostly transform data from specific formats of applications or cloud services,

for example **Google Drive**.



We need access tokens and sometime other parameters to get access to these datasets and services.





.. toctree::

   :maxdepth: 1

   :glob:



   ./document_loaders/examples/airbyte_json.ipynb

   ./document_loaders/examples/apify_dataset.ipynb

   ./document_loaders/examples/aws_s3_directory.ipynb

   ./document_loaders/examples/aws_s3_file.ipynb

   ./document_loaders/examples/azure_blob_storage_container.ipynb

   ./document_loaders/examples/azure_blob_storage_file.ipynb

   ./document_loaders/examples/blackboard.ipynb

   ./document_loaders/examples/blockchain.ipynb

   ./document_loaders/examples/chatgpt_loader.ipynb

   ./document_loaders/examples/confluence.ipynb

   ./document_loaders/examples/diffbot.ipynb

   ./document_loaders/examples/discord_loader.ipynb

   ./document_loaders/examples/docugami.ipynb

   ./document_loaders/examples/duckdb.ipynb

   ./document_loaders/examples/fauna.ipynb

   ./document_loaders/examples/figma.ipynb

   ./document_loaders/examples/gitbook.ipynb

   ./document_loaders/examples/git.ipynb

   ./document_loaders/examples/google_bigquery.ipynb

   ./document_loaders/examples/google_cloud_storage_directory.ipynb

   ./document_loaders/examples/google_cloud_storage_file.ipynb

   ./document_loaders/examples/google_drive.ipynb

   ./document_loaders/examples/image_captions.ipynb

   ./document_loaders/examples/iugu.ipynb

   ./document_loaders/examples/joplin.ipynb

   ./document_loaders/examples/microsoft_onedrive.ipynb

   ./document_loaders/examples/modern_treasury.ipynb

   ./document_loaders/examples/notiondb.ipynb

   ./document_loaders/examples/notion.ipynb

   ./document_loaders/examples/obsidian.ipynb

   ./document_loaders/examples/psychic.ipynb

   ./document_loaders/examples/pyspark_dataframe.ipynb

   ./document_loaders/examples/readthedocs_documentation.ipynb

   ./document_loaders/examples/reddit.ipynb

   ./document_loaders/examples/roam.ipynb

   ./document_loaders/examples/slack.ipynb

   ./document_loaders/examples/snowflake.ipynb

   ./document_loaders/examples/spreedly.ipynb

   ./document_loaders/examples/stripe.ipynb

   ./document_loaders/examples/tomarkdown.ipynb

   ./document_loaders/examples/twitter.ipynb

