todo_list=[]
def add_task():
    text=input("请输入待办任务：")
    todo_list.append({"task":text,"done":False})
    print("✅任务添加成功！")

def list_tasks():
    if len(todo_list)==0:
        print("暂无待办任务")
        return
    print("\n=====待办清单=====")
    for idx,item in enumerate(todo_list):
        status="✅已完成" if item["done"] else "🔲未完成"
        print(f"{idx}.{status} {item['task']}")
    print("=============\n")

def mark_finished():
    list_tasks()
    if len(todo_list)==0:
        return
    num=int(input("请输入要标记完成的任务编号："))
    if 0<=num<len(todo_list):
        todo_list[num]["done"]=True
        print("已标记完成")
    else:
        print("编号无效")

def delete_task():
    list_tasks()
    if len(todo_list)==0:
        return
    num=int(input("请输入要删除的任务编号："))
    if 0<=num<len(todo_list):
        todo_list.pop(num)
        print("任务已经删除")
    else:
        print("编号无效")

def main():
    while True:#无限循环（死循环）while后面条件写True就代表条件永远成立，里面的代码会一遍一遍反复跑。
        print("""
========todo list========
1-添加任务
2-查看全部任务
3-标记任务完成
4-删除任务
0-退出程序
==========================        
        """)
        choice=input("请输入数字：")
        if choice=="1":
            add_task()
        elif choice=="2":
            list_tasks()
        elif choice=="3":
            mark_finished()
        elif choice=="4":
            delete_task()
        elif choice=="0":
            print("程序结束")
            break
        else:
            print("输入无效")

if __name__=="__main__":
    main()
