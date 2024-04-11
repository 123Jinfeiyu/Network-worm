from langchain.document_loaders import DirectoryLoader, PyPDFLoader
def read_resumes():
    # 读取resume文件夹中的所有文件
    d_loader = DirectoryLoader("./resume", glob="*.pdf",loader_cls=PyPDFLoader)

    # 获取 PDF 文本，返回一个列表，列表中的每个元素都是一个 PDF 文档的页
    pdf_pages = d_loader.load()

    resume_text = ""

    for page in pdf_pages:
        # 建立路径，用于区分是哪一份简历
        # print(page.metadata.get('source'))

        page_text = page.page_content
        resume_text += page_text

    return resume_text