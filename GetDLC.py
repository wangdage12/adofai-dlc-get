import sentry_sdk
sentry_sdk.init(
    dsn="https://b284ddce1d7e7dac6e25a2a8b869581e@o4507525750521856.ingest.us.sentry.io/4509116221685760",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
import json
import os
import requests
import logging
import coloredlogs
from tqdm import tqdm
# 创建日志记录器
logger = logging.getLogger(__name__)
# 配置 coloredlogs
coloredlogs.install(level='DEBUG', logger=logger)
from colorama import init, Fore, Back, Style

APP_VERSION = '1.0.0'  # 应用版本
GAME_FILE = 'A Dance of Fire and Ice.exe'  # 游戏主程序文件名

logger.info(f"工具版本：{APP_VERSION}")

print("本工具仅用来学习研究adofai中的dlc文件，使用该脚本下载的dlc文件仅共学习使用，作为其他用途使用的后果自负\n官方仓库：https://github.com/wangdage12/adofai-dlc-get")

init(autoreset=True)
def colorprint(msg,color,end='\n'):
    if color=='1':
        print(Fore.RED + msg, end=end)
    elif color=='2':
        print(Back.GREEN + msg, end=end)
    elif color=='3':
        print(Style.DIM + msg, end=end)
    elif color == "4":
        print("\033[33m" + msg + "\033[39m", end=end)
    elif color == "5":
        print("\033[36m" + msg + "\033[39m", end=end)

def Rjson(json_file):
    """
    读取JSON文件
    :param json_file: JSON文件路径
    :return: JSON数据
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def Wjson(json_file, data):
    """
    写入JSON文件
    :param json_file: JSON文件路径
    :param data: 要写入的数据
    """
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 读取配置文件
def read_config():
    config = json.loads(requests.get("http://124.221.67.43/adofai/config.json").text)
    return config

def download_file(url, output_path):
    # 获取响应对象并设置流式下载
    response = requests.get(url, stream=True)
    
    # 获取文件总大小（字节）
    total_size = int(response.headers.get('content-length', 0))
    
    # 设置进度条
    with open(output_path, 'wb') as file, tqdm(
        desc=output_path,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

cfg=read_config()

logger.info("读取配置文件成功")

print(cfg['msg'])

# 检查目录下是否存在游戏主程序文件
if not os.path.exists(GAME_FILE):
    logger.error(f"未找到游戏主程序文件：{GAME_FILE}")
    colorprint("请确保程序在游戏安装目录下",color='1')
    exit(1)

colorprint("以下是支持的游戏版本：",color='5')
for i in range(len(cfg['version'])):
    colorprint(str(i)+" ",color='2',end='')
    colorprint(" "+str(cfg['version'][i]),color='5')

    
print()
colorprint("请输入你已安装的游戏版本的编号：",color='5')

v=input()
while True:
    if v.isdigit() and int(v) in range(len(cfg['version'])):
        break
    else:
        colorprint("输入错误，请重新输入：",color='1')
        print("提示：编号是前面版本号列表的绿底数字，根据你的游戏版本输入对应的编号，编号从0开始")
        v = input()

colorprint(f"确定你的游戏版本是{cfg['version'][int(v)]}吗？\n选择错误会导致游戏无法启动\n请提前关闭游戏\n回车键继续",color='4')
input()
vname = cfg['version'][int(v)]

# 备份\A Dance of Fire and Ice_Data\Managed\Assembly-CSharp.dll
# if os.path.exists("A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll.bak"):
#     os.remove("A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll.bak")
#     logger.info("删除旧备份成功")
# else:
#     logger.info("没有旧备份，跳过删除")

try:
    os.rename("A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll", "A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll.bak")
    logger.info("备份游戏文件成功")
except FileNotFoundError:
    logger.warning("备份游戏文件失败，未找到原文件")
# 存在旧备份
except FileExistsError:
    logger.warning("备份游戏文件失败，已存在旧备份，如你已经备份过，请手动删除/A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll.bak")
    
# 选择下载服务器
for i in range(len(cfg['downloadServer'])):
    # 获取服务器地址/test.json
    url = cfg['downloadServer'][i]+"/test.json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logger.info(f"选择下载服务器：{cfg['downloadServer'][i]}")
            downserver = cfg['downloadServer'][i]
            break
        else:
            logger.error(f"选择下载服务器失败：{cfg['downloadServer'][i]}")
    except requests.exceptions.RequestException as e:
        logger.error(f"选择下载服务器失败：{cfg['downloadServer'][i]}，错误信息：{e}")
    except requests.exceptions.Timeout as e:
        logger.error(f"选择下载服务器超时：{cfg['downloadServer'][i]}，错误信息：{e}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"选择下载服务器连接失败：{cfg['downloadServer'][i]}，错误信息：{e}")
    
        

logger.info("开始下载游戏文件")
download_file(downserver+"/DLL/"+"Assembly-CSharp.dll"+"."+cfg['version'][int(v)], "A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll")

#检查dlc文件夹是否存在
if vname=='v2.8.1':
    # 2.8.1版本的dlc路径是NeoCosmos/StandaloneWindows64
    if not os.path.exists("NeoCosmos/StandaloneWindows64"):
        os.makedirs("NeoCosmos/StandaloneWindows64", exist_ok=True)
        logger.info("创建dlc文件夹成功")
else:
    if not os.path.exists(cfg[vname]['dlcpath']):
        os.mkdir(cfg[vname]['dlcpath'])
        logger.info("创建dlc文件夹成功") 
    else:
        logger.info("dlc文件夹已存在，跳过创建")
# 继续检查dlc文件夹里面是否有dlc文件
for i in cfg[vname]['dlcFiles']:
    if os.path.exists(cfg[vname]['dlcpath']+"/"+i):
        logger.info(f"dlc文件夹内已存在{i}，跳过下载")
    else:
        logger.info(f"dlc文件夹内不存在{i}，开始下载")
        print(downserver+i)
        download_file(downserver+i, cfg[vname]['dlcpath']+"/"+i)
        
logger.info("处理完成，可以启动游戏使用dlc了")
input("按回车键退出")