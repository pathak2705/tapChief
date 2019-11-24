import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tapChiefClear import clear
from tapChiefIndex import indexing
from tapChiefSearch import search

class Form(Frame):
    def __init__(self,master=None):

        super().__init__(master)
        self.pack(expand=True,padx=60,pady=60)
        self.createWidget()

    def btnClickClear(self):
        try:
            if(len(self.data)==0):
                raise Exception
            else:
                self.cleared_data=clear(self.data)
                tkinter.messagebox.showinfo("Info","Cleared indexes successfully!!")
        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex)

    def btnClickIndex(self):
        try:
            if("index" not in self.data.columns.values):
                x = range(len(self.data))
                x = list(x)
                self.data["index"] = x
                self.inverted_index=indexing(self.data,self.dict)
                tkinter.messagebox.showinfo("Info","Indexing done successfully!!")
            else:
                raise Exception
        except Exception as ex:
            tkinter.messagebox.showinfo("Error",ex)

    def btnClickSubmit(self):
        try:
            self.topSubmitSearch=Toplevel(self,padx=60,pady=60)
            # print(self.comboSearch.get())
            self.output = search(self.comboSearch.get(), self.data, self.inverted_index)
            # print(self.output)
            self.list=Listbox(self.topSubmitSearch, height=4, width=100)
            for i in range(len(self.output)):
                self.list.insert(i,self.output[i])
            self.s = Scrollbar(self.topSubmitSearch)
            self.s.pack(side=RIGHT, fill=Y)
            self.list.pack(side=LEFT, fill=Y)
            self.s.config(command=self.list.yview)
            self.list.config(yscrollcommand=self.s.set)

        except Exception as ex:
            tkinter.messagebox.showerror(ex)
            self.topSubmitSearch.destroy()

    def btnClickSearch(self):
        try:
            self.topSearch=Toplevel(self,padx=60,pady=60)
            self.labelSelect=Label(self.topSearch,text="Select any word :-").grid(row=0,column=0,columnspan=4,padx=10,pady=10)
            self.comboSearch=ttk.Combobox(self.topSearch,values=sorted(self.dict))
            self.comboSearch.current(1)
            self.comboSearch.grid(row=1,column=0,columnspan=4,padx=10,pady=10,sticky="E")
            self.btnSubmit=Button(self.topSearch, text="Submit", command=self.btnClickSubmit).grid(row=2,column=1,columnspan=2,sticky=E,padx=10,pady=10)

        except Exception as ex:
            tkinter.messagebox.showerror(ex)


    def createWidget(self):

        self.data = pd.read_csv(r"D:\python\DataSet\Test.csv")
        # print(len(self.data))
        self.data = self.data.drop(columns=["answer_text"])
        self.data = self.data[:1000]
        # type(self.data)

        self.dict = []
        for each in self.data["question"]:
            stop_words = set(stopwords.words('english'))
            tokens = word_tokenize(each)
            for w in tokens:
                if w not in stop_words:
                    self.dict.append(w.lower())
        self.dict = list(set(self.dict))
        self.dict

        ps = PorterStemmer()
        for i in range(len(self.dict)):
            self.dict[i] = ps.stem(self.dict[i])

        self.btn_Clear=Button(self, text="Clear", command=self.btnClickClear,borderwidth=4,width=25).grid(row=0,column=0,columnspan=2,sticky="E",padx=10,pady=10)
        self.btn_Index=Button(self, text="Index", command=self.btnClickIndex,borderwidth=4,width=25).grid(row=1,column=0,columnspan=2,sticky="E",padx=10,pady=10)
        self.btn_Search=Button(self, text="Search", command=self.btnClickSearch,borderwidth=4,width=25).grid(row=2,column=0,columnspan=2,sticky="E",padx=10,pady=10)


if __name__ == "__main__":
    root=Tk()
    root.title("TapChief")
    root.resizable(0,0)
    f=Form(root)
    root.mainloop()

data = pd.read_csv(r"D:\python\DataSet\Test.csv")
data = data.drop(columns=["answer_text"])
data = data[:1000]
# type(self.data)

dict = []
for each in data["question"]:
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(each)
    for w in tokens:
        if w not in stop_words:
            dict.append(w.lower())
dict = list(set(dict))
dict

ps = PorterStemmer()
for i in range(len(dict)):
    dict[i] = ps.stem(dict[i])

# root.mainloop()
# def btnClickSubmit():
#     toplevel=Toplevel(root)
#     output = ["how are you", "i am fie", "e rhg dgc" ,"fhf cbc etr", "gdf cc hfg" ,"dgdgd ngcg cggdg" ,"hfg ggdfd"]
#     s=Scrollbar(toplevel)
#     list=Listbox(toplevel, height=3, width=50)
#     for i in range(len(output)):
#         list.insert(i,output[i])
#     s.pack(side=RIGHT, fill=Y)
#     list.pack(side=LEFT, fill=Y)
#     s.config(command=list.yview)
#     list.config(yscrollcommand=s.set)
#
# root=Tk()
# root.title("TapChief")
# root.resizable(0,0)
# labelSelect=Label(root,text="Select any word :-").grid(row=0,column=0,columnspan=4,padx=10,pady=10)
# comboSearch=ttk.Combobox(root,values=sorted(dict))
# comboSearch.current(1)
# comboSearch.grid(row=1,column=0,columnspan=4,padx=10,pady=10,sticky="E")
# btnSubmit=Button(root, text="Submit", command=btnClickSubmit).grid(row=2,column=1,columnspan=2,sticky=E,padx=10,pady=10)
# root.mainloop()

# creating a pdf reader object
# import PyPDF2
# pdfFileObj = open(r'D:\python\DataSet\Report.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pageObj=pdfReader.getPage(30)
# print(pageObj.extractText())