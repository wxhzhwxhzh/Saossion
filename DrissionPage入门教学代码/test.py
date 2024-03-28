import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time

def new_window(root):
    filename = filedialog.askopenfilename()  # 弹出文件选择对话框，获取用户选择的文件路径
    new_window = tk.Toplevel(root)  # 创建新窗口
    new_window.title("代码生成预览")
    
    filename_label = ttk.Label(new_window, text="预览代码：")
    filename_label.pack()
    
    # 创建带有垂直滚动条的文本框
    text_frame = ttk.Frame(new_window)
    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    filename_text = tk.Text(text_frame, width=70, font=("maple mono", 10), yscrollcommand=scrollbar.set)
    filename_text.insert(tk.END, filename+'\n')  # 在文字区域中显示文件名
    filename_text.pack(fill=tk.BOTH, expand=True)
    
    # 设置滚动条的command为文本框的yview
    scrollbar.config(command=filename_text.yview)  
    
    
    def update_time():          
        filename_text.insert(tk.END, '\n'+time.strftime('%Y-%m-%d %H:%M:%S'))
        # 每秒钟更新一次时间
        root.after(1000, update_time)
        
    update_time()    

root = tk.Tk()
root.title("文件信息显示程序")

button = ttk.Button(root, text="显示文件信息", command=lambda: new_window(root))
button.pack(padx=20, pady=20)

root.mainloop()
