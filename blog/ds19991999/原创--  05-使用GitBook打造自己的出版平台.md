# 原创
：  05-使用GitBook打造自己的出版平台

# 05-使用GitBook打造自己的出版平台

# 使用GitBook打造自己的出版平台

## 准备工作

## 使用Summary构建书籍目录

### 直接用Summary构建

```
{
    "bookname": "json-config-name",
    "outputfile": "test.md",
    "catalog": "all",  // 如 [chapter1，chapter2, ...]
    "ignores": [],
    "unchanged": [] // 如: ['myApp'] -&gt; `myApp` not `My App`
}
```

### 使用Python脚本构建

```
import os
import os.path

##############################################文件名##########################
# 文件名
folders = []
folders = ['Python-Tools', 
           'advanced-python',
           'Scipy']
# 对应的中文名
chinese = ['一、Python 工具', 
           '二、Python 进阶',
           '三、Scipy 基础']
# 对应到字典中
folders_to_chinese = dict(zip(folders, chinese))

#####################################先产生文件夹内部README.md################
for folder in folders:
    with open(folder+'/README.md','w') as f:
        pass
    folder_file = open(folder+'/README.md','w')
    folder_file.write('# '+folders_to_chinese[folder]+ '\n')
    files = sorted(os.listdir(folder)) 
    # 不处理README.md
    i = 0
    for file_name in files:
        i += 1
        if file_name.endswith('.md') and file_name != 'README.md':          
            fname = folder+'/'+file_name
            with open(fname) as fp:
                lines = fp.readlines()
                for f in lines:
                    if f[0] == '#':
                        new_name = f
                        break   
                # print '    '+str(i)+new_name[1:-1]
            folder_file.write('- ['+ str(i)+new_name[1:-1]+']('+ file_name +')\n')    
    folder_file.close()
#####################################再产生文件夹外部README.md#######################
# 产生目录文件：
index_file = open('SUMMARY.md', 'w')
index_file.write('# Python数据分析 \n\n')
print 'Contents'

for folder in folders:
    # 处理文件夹名
    index_file.write('- [' + folders_to_chinese[folder]+'](' + folder + '/' + 'README.md' +')\n')
    print folders_to_chinese[folder]
    files = sorted(os.listdir(folder))    
    # 处理文件夹内其他内容
    i = 0
    for file_name in files:       
        if file_name.endswith('.md') and file_name != 'README.md':
            i += 1
            name = file_name            
            fname = folder+'/'+name
            with open(fname) as fp:
                lines = fp.readlines()
                for f in lines:
                    if f[0] == '#':
                        new_name = f
                        break   
                print '    '+str(i)+new_name[1:-1]  

            index_file.write('    * [' + str(i)+new_name[1:-1])
            index_file.write('](' + folder + '/' + file_name +')\n')
index_file.close()
```

## 生成电子书

## 输出pdf

## 最终验证成功的命令

```
# 先卸载全局node.js
# 再安装nvm
nvm ls # 查看安装的npm版本
nvm use 8.11.3 # 切换node 8.11.3版本
nvm install 6 # 安装6的最新版本

nvm use 6.0.0  # 使用旧版本6.0.0
gitbook build --gitbook=2.6.7  # 使用旧版本创建书籍
# 这里输出的html支持跳转
gitbook pdf . book.pdf --gitbook=2.6.7 # 旧版本可以导出pdf等格式的电子书，不需要插件，前面一个是书籍路径，后面一个生成的pdf路径及文件名
```
