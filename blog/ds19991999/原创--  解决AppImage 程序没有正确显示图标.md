# 原创
：  解决AppImage 程序没有正确显示图标

# 解决AppImage 程序没有正确显示图标

AppImage是一种在 Linux系统中用于分发便携式软件而不需要超级用户权限来安装它们的格式。它还试图让允许Linux的上游开发者来分发他们的程序而不用考虑不同Linux发行版间的区别。

## 特点

AppImage不把Linux应用程序安装在文件系统相应的目录中。相反,它没有进行实际的安装。AppImage文件只是个压缩文件，在它运行时候挂载。

用AppImage打包的程序，一个程序就是一个文件。每一个文件都包含了该程序在其所要运行的目标平台上所需的运行库。AppImage文件是基于ISO 9660并经过zisofs压缩的包含有一个最小化的AppDir目录和一个极小的运行环境的文件。只要把这个文件添加到live CD中，这个程序便可被轻而易举地添加进live CD中。

用AppImage文件比安装一个应用程序更加简单。它不需要解压也不需要为系统环境做调整。使用主流Linux发行版的用户可以下载它，使其可执行，并且运行即可。

## 解决图标显示问题

```
/home/$USERNAME/.config/  # 这个目录中是一些配置文件
/home/$USERNAME/.local/share/applications  # 这个目录中是一个桌面文件 appimagekit.desktop
```
