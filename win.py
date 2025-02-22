import tkinter as tk
import win32gui
import psutil
import win32process
import time

def get_focused_window_cmd_args():
    # 获取当前活动窗口的句柄
    hwnd = win32gui.GetForegroundWindow()
    # 获取该窗口所属进程的 ID
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    try:
        # 根据进程 ID 获取进程对象
        process = psutil.Process(pid)
        # 获取进程的命令行参数
        cmd_args = process.cmdline()
        return cmd_args
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return []

def get_focused_window_position_and_size():
    # 获取当前焦点窗口的句柄
    hwnd = win32gui.GetForegroundWindow()
    # 获取窗口的位置和尺寸信息
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    return (left, top), (width, height)




# 创建主窗口
root = tk.Tk()
# 设置窗口标题
root.title("MAC7")
# 设置窗口大小

root.config(bg="blue")

# 创建一个标签
label = tk.Label(root, text="MAC7",bg="yellow",font=("Arial", 24))
# 将标签放置在窗口中
label.pack(fill=tk.BOTH, expand=True)
# root.withdraw()

try:
    while True:
        cmd = get_focused_window_cmd_args()
        print(cmd)
        if "powershell" in cmd[0]:
            position, size = get_focused_window_position_and_size()
            print(f"焦点窗口位置: {position}")
            print(f"焦点窗口位置: {size}")
            x=position[0]
            y=position[1] - 130
            width=size[0] - 15
            root.geometry(f"{width}x100+{x}+{y}")
            root.deiconify()
            print("powershell window, show window")
        else:
            root.withdraw()
            print("not powershell window, hide window")
        time.sleep(1)  # 每隔 0.5 秒检查一次
except KeyboardInterrupt:
    new_window.destroy()  # 按 Ctrl+C 退出时销毁新窗口

# 进入主事件循环
#root.mainloop()
