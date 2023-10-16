import os
from pathlib import Path

from onecontext import KnowledgeBase, Retriever
from onecontext.core import list_knowledge_bases

# %%

my_knowledge_base = KnowledgeBase("my_knowledge_base")

my_knowledge_base.create()

my_knowledge_base.create()


folder = Path("~/pdfs/").expanduser()

my_knowledge_base.upload_from_directory()


my_knowledge_base.get_info()

print(my_knowledge_base.sync_status)


retriver = Retriever(knowledge_bases=[my_knowledge_base])

retriver = Retriever(knowledge_bases=[jp_demo])

documents = retriver.query("is the green goal north")

print(documents)
