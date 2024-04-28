import os
def list_files_in_folders(folder_path):
    try:
        files=os.listdir(folder_path)
        return files,None
    except FileNotFoundError:
        return None,"文件未发现"
    except PermissionError:
        return None,"权限拒绝"
    
def main():
    folder_paths=input("输入以空格分隔的文件夹路径列表: ").split()
    for folder_path in folder_paths:
        files,error_message=list_files_in_folders(folder_path)
        if files:
            print(f"File in {folder_path}: ")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}:{error_message}")

if __name__=="__main__":
    main()