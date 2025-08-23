---
title: 在 iPadOS 上使用 git
date: 2023-08-08 14:00:00
code: true
---

谈论如何在 iPadOS 上使用 [git](https://git-scm.com/) 之前，我们需要介绍为什么会有这方面的需求：

>有一款小有名气的笔记管理软件叫做 [Obsidian](https://obsidian.md/)，我把它安装在我的 Linux 计算机和 iPad 上，在计算机上进行密集型的写作（比如本文），在 iPad 上进行查阅及轻量级的编辑。但是问题在于 Obsidian 以本地化的笔记管理见长，这种设计理念意味着它在多端同步方面有着先天的不足，把计算机上的笔记同步到 iPad 是一件相当折磨的事情。
>
>我最先想到的就是借助 github 进行同步（其实还有比它方便得多的办法，这将在后续介绍），然而 iPadOS 上并没有官方的 git CLI。第三方 git 工具比如 Working Copy 是收费软件，这与 git 本身的开源理念背道而驰，而且我个人认为其图形界面相当凌乱与丑陋，所以我对该第三方 APP 持抵触态度。再者相比图形界面我其实更习惯用命令行操作 git。
>
>那么，找到一种在 iPadOS 上使用 git，并且能自由地使用 git 完整功能的方法，就是我的需求。

我们有一个非常 fancy 的解决方案，那就是在 iPadOS 上运行一个轻量级的 Linux 虚拟机，这可以通过开源的 [iSH](https://ish.app/) 来实现。iSH 实质是在模拟的 x86 架构上运行一个非常轻量的 [Alpine Linux](https://www.alpinelinux.org/) 系统，并且支持把 iPadOS 本地的文件夹挂载到该系统上（这一点至关重要，它使我们那些有创造性的折腾成为可能）。

到此为止，本文的标题就略显狭隘了，因为既然我们可以运行一个 Linux 系统，又何必止步于 git 呢，如何在 iPadOS 上使用 g++, make, gnuplot, python, nodejs 等等问题都迎刃而解了。

## 安装 iSH

直接在 [App Store](https://apps.apple.com/us/app/ish-shell/id1436902243) 搜索并安装即可，仅 5.9Mb 大小。

![500](assets/appstore.jpeg)

进入之后界面如下，提示我们可以通过`apk add <package>`安装软件，注意只能通过命令行进行交互。

![500](assets/ish.png)

它的文件系统可以在 iPad 自带的 Files 查看：

![500](assets/file.png)

## 使用 git

我们先安装 git，并且为了测试，我们也安装上 g++ 编译器：

```bash
apk add git g++
```

先在根目录下创建`test`文件夹，作为 iPadOS 文件系统的挂载点。我们在 iPad 上事先也准备了一个名为`test`的文件夹，它才真正承载着我们的 git 仓库。然后通过`mount`命令把 iPad 上的文件夹挂载到 iSH：

![500](assets/mount.jpeg)

命令执行完毕会弹出对话框，选择需要挂载的文件夹即可：

![500](assets/mount-test.jpeg)

选择自己喜欢的方式写一段代码，用 Linux 自带的 vi 或者安装 Vim 都可以，这里我用的是 Koder，写了一段非常简易的计算平方的 C++ 代码：

![500](assets/koder.png)

之后进入 iSH 使用`g++`进行编译：

![500](assets/g++1.jpeg)

可以看到代码成功编译并且输出了正确结果。然后我们初始化 git 仓库，并提交当前代码：

![500](assets/g++2.jpeg)

然后我们对代码进行简单修改，把计算平方改为计算立方，并重新编译执行（见上图）。执行的结果如下图。然后我们提交新的代码。

![500](assets/g++3.jpeg)

远程仓库的拉取和推送等功能也能正常使用，在此不做过多展示。可见，通过这种方式，我们不仅能使用 git 的完整功能，而且可以实现对 iPad 本地的文件进行版本控制。

## 使用 gnuplot

除了 git，我们再测试一下 [gnuplot](http://www.gnuplot.info/) 能否正常使用。先进行安装：

```bash
apk add gnuplot
```

简单画个函数：

![500](assets/gnuplot.jpeg)

成功输出了结果`sin.png`，我们可以在 iPad 上浏览该图片：

![500](assets/test.jpeg)
