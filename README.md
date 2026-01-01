# adofai-dlc-get
获取A Dance of Fire and Ice中的dlc文件的脚本  

> 本工具仅用来学习研究adofai中的dlc文件，使用该脚本下载的dlc文件仅共学习使用，作为其他用途使用的后果自负  
> 我的博客中有关于该工具的贴子，可以在这里查看：http://server.wdg.cloudns.ch:8088/  

> [!IMPORTANT]
> 目前因为dlc文件版本低的问题导致2.9.5及以上的游戏无法进入官方dlc关卡，若你拥有最新的dlc文件（游戏目录下的`Bundles`文件夹），请帮忙提供，非常感谢

注意：你需要有游戏本体才能使用

下载最新版本：前往[releases](https://github.com/wangdage12/adofai-dlc-get/releases)页面，下载最上面的`.exe`文件，然后查看[使用教程](https://www.bilibili.com/opus/1057497643524030472)

> [!NOTE]
> github上的releases内的打包标准：  
> python脚本：AMD x64 单文件  
> c# GUI工具：AMD x64 单文件 依赖框架  
> 若需要其他架构请提issues

运行打包好的exe：需要windows版本`>=windows 10`

打包exe或者直接运行py脚本：建议python版本`>=3.12`

[下载服务器状态](https://stats.uptimerobot.com/iK8au9ecDP)

如游戏版本更新或者要求其他版本，打开Issues即可

如有最新版本dlc文件，请帮忙提交

**如果你们需要的话，我会建立一个仓库作为修改后的Assembly-CSharp.dll和其他资源的存储库**

**如果无法运行：**  

> 注意:如果下载服务器失效,可以将域名前面的`f1`换为: `f3`或`f4`
> 自建ipv6服务器，首选这个：http://server.wdg.cloudns.ch:8002/adofai/
> 新CDN服务器：https://afilecdn.wdg.cloudns.ch/

下载这几个文件：  
http://f1.wdg.cloudns.ch/adofai/neocosmos_assets_all.bundle  
http://f1.wdg.cloudns.ch/adofai/64b0239cbb1b5026aca97cb135062056_unitybuiltinshaders.bundle  
http://f1.wdg.cloudns.ch/adofai/neocosmos_scenes_all.bundle  

游戏根目录下新建`Bundles`文件夹，放入下载的文件  
**2.9.5需要创建`NeoCosmos\StandaloneWindows64`两个文件夹，并将dlc文件放入`StandaloneWindows64`中**  

下载：  

> 注意:按照你的游戏版本修改下载链接后面的版本号,例如*2.9.5*是`Assembly-CSharp.dll.v2.9.5`,*2.8.1*是`Assembly-CSharp.dll.v2.8.1`

http://f1.wdg.cloudns.ch/adofai/DLL/Assembly-CSharp.dll.v2.9.5  
重命名为`Assembly-CSharp.dll`  
进入：  
`\A Dance of Fire and Ice_Data\Managed`  
备份`Assembly-CSharp.dll`后删除`Assembly-CSharp.dll`  
将刚才下载的文件放入该目录内，启动游戏即可  
