def update_server_config(file_path,key,value):

    # with 语句打开文件可以确保文件在处理完毕后会被自动关闭
    with open(file_path, 'r') as file:
        lines=file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                # 写入操作会更新配置 注意换行
                file.write(key+' = '+value+'\n')  
            # 将原始文件中的每一行内容写回到更新后的配置文件中，保持原有的配置项不变
            else:
                file.write(line)


server_config_file=r'c:/WorkSpace/VSC/Devops/FileOperations/server.conf'

key_to_update='MAX_CONNECTIONS'
new_value='300'
update_server_config(server_config_file,key_to_update,new_value)