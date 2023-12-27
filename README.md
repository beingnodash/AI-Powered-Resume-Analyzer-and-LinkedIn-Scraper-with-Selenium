# AI驱动的简历分析器和领英数据爬取工具

## **简介**

Resume Analyzer AI是一个Streamlit应用程序，利用LLM和OpenAI的功能,专门进行全面详细的简历分析。主要功能是：

总结简历

评估优势

识别劣势

提供个性化的改进建议，同时推荐最合适的职位

Resume Analyzer AI还有一个实验性功能：使用Selenium从领英提取数据，包括公司、职位、地点、职位链接和职位描述。

总之，Resume Analyzer AI是一个由生成式语言模型支持的简历分析器，能够为用户提供全面的见解，从而简化、优化他们的求职过程、以提升他们的职业机会。

## **目录**

1. 关键技术
2. 安装
3. 使用
4. 功能
5. 贡献
6. 许可
7. 联系方式

## **依赖或包**

- Numpy
- Pandas
- Streamlit
- LLM
- LangChain
- OpenAI
- Selenium

## **安装**

运行这个项目，需要安装以下软件包:

```python
pip install numpy
pip install pandas 
pip install streamlit
pip install streamlit_option_menu
pip install streamlit_extras
pip install PyPDF2
pip install langchain
pip install openai
pip install tiktoken
pip install faiss-cpu
pip install selenium
```

## **使用**

使用这个项目，请执行以下步骤：

1. 克隆存储库:`git clone https://github.com/beingnodash/ResumeAnalyzerAI.git`
2. 安装所需的包:`pip install -r requirements.txt`
3. 运行Streamlit应用程序:`streamlit run app.py`
4. 在浏览器中访问该应用程序:`http://localhost:8501`

## **功能**

### **用户体验:**

- Resume Analyzer AI的用户操作方式比较简单：上传简历、输入OpenAI API密钥，即可使用它的所有功能。

### Langchain提供的智能文本分析

- 项目的核心功能是简历文本的智能分析器。它使用名为Langchain的库将简历中的长文本拆分成更小的块，使其更有意义。
- 这种分拆技术提高了简历分析的准确性。

### **FAISS增强的OpenAI集成:**

- 它与OpenAI服务无缝连接,使用OpenAI API密钥建立安全连接。这种集成构成了强大交互的基础,促进高级分析和高效的信息检索。
- 它使用FAISS(Facebook AI相似性搜索)库将文本块和查询文本数据转换为数值向量，简化了分析过程，并能够检索相关信息。

### **智能文本块选择和LLM:**

- 利用相似性搜索,Resume Analyzer AI比较查询和文本块,基于相似度分数选择前K个最相似的文本块。
- 同时,该应用程序创建一个OpenAI对象,特别是一个LLM(大型语言模型),使用ChatGPT 3.5 Turbo模型和你的OpenAI API密钥。

### **问答流水线:**

- 这种集成建立了一个强大的问答流水线,利用load_qa_chain函数,它包含多个组件,包括语言模型。
- QA链有效地处理输入文档列表和问题列表,响应变量捕获结果,例如从输入文档内容中派生的答案。

### **简历分析:**

- **总结:** Resume Analyzer AI对简历进行快速全面概述,强调资质、主要经历、技能、项目和成就。用户可以快速掌握个人情况，提高复习效率和洞察力。
- **优势:** 它可以轻松进行全面的简历审查，分析资质、经验和成就。
- **劣势:** AI进行全面分析以找出弱点，并提供量身定制的解决方案，将弱点转化为优势，赋能求职者。
- **建议:** AI提供与用户资质和简历内容高度匹配的个性化职位建议，优化求职体验。

### **Selenium驱动的领英数据爬取:**

- 利用Selenium和自动化测试工具Webdriver，这个功能允许用户输入职位，自动从领英爬取数据。爬取的数据包括关键细节,如公司名称、职位、地点、URL和详细的职位描述。
- 这种精简的流程使用户可以轻松查看爬取的职位详情并申请职位，简化他们的求职和申请过程。
- **重要提示:** 此功能目前仅可在本Streamlit应用程序的本地版本中使用。

### **贡献**

欢迎对这个项目做出贡献！如果你遇到任何问题或有改进建议，请随时提交pull请求。

如果还有任何其他问题或询问，请随时联系。我们很乐意帮助您解答任何问题。

## **许可**

该项目使用MIT许可证授权。请查看LICENSE文件以获取更多详细信息。

## **联系方式**

📧 电子邮件: chen.xibo@gmail.com
