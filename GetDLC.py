import sentry_sdk
sentry_sdk.init(
    dsn="https://b284ddce1d7e7dac6e25a2a8b869581e@o4507525750521856.ingest.us.sentry.io/4509116221685760",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    _experiments={
        "enable_logs": True,
    },
)
import json
import os
import requests
import logging
import coloredlogs
import time
import sys
import argparse
from tqdm import tqdm
from colorama import init, Fore, Back, Style
from sentry_sdk import logger as sentry_logger

# 创建日志记录器
logger = logging.getLogger(__name__)
# 配置 coloredlogs
coloredlogs.install(level='DEBUG', logger=logger)

APP_VERSION = '2.1.0'  # 应用版本
GAME_FILE = 'A Dance of Fire and Ice.exe'  # 游戏主程序文件名
GUI_FILE = 'adofai-dlc-get-gui.exe'  # GUI程序文件名

logger.info(f"工具版本：{APP_VERSION}")

sentry_logger.info('工具启动',version=APP_VERSION)

print("本工具仅用来学习研究adofai中的dlc文件，使用该脚本下载的dlc文件仅共学习使用，作为其他用途使用的后果自负\n官方仓库：https://github.com/wangdage12/adofai-dlc-get")

parser = argparse.ArgumentParser(description='A Dance of Fire and Ice DLC获取工具')
parser.add_argument('-c', action='store_true', help='使用命令行参数')
parser.add_argument('-t', action='store_true', help='运行速度测试')
parser.add_argument('-r', action='store_true', help='还原游戏文件')
parser.add_argument('-d', action='store_true', help='启用游戏的debug模式')
parser.add_argument('--v', type=str, help='游戏版本号')
args = parser.parse_args()

gameDebug = ""  # 是否启用游戏的debug模式

if args.c:
    logger.info("使用命令行参数参数自动运行，选择的游戏版本号为：" + args.v)

if args.d:
    gameDebug = ".debug"
    logger.info("启用游戏的debug模式")


init(autoreset=True)
def colorprint(msg,color,end='\n') -> None:
    """打印带颜色的文本

    Args:
        msg (str): 要打印的消息
        color (str): 颜色编号（1: 红色, 2: 绿色, 3: 灰色, 4: 黄色, 5: 蓝色）
        end (str, optional): 结束符。 Defaults to '\n'.
    """
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

def Rjson(json_file) -> dict:
    """读取JSON文件

    Args:
        json_file (str): JSON文件路径

    Returns:
        dict: 读取的JSON数据
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def Wjson(json_file, data) -> None:
    """写入JSON文件

    Args:
        json_file (str): JSON文件路径
        data (dict): 要写入的数据
    """
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

CONFIG_URLS = [
    "https://afilecdn.wdg.cloudns.ch/config.json",
    "http://server.wdg.cloudns.ch:8002/adofai/config.json",
]

def read_config() -> dict:
    """
    从服务器读取配置文件
    Returns:
        dict: 读取的配置数据，如果都失败返回空字典
    """
    for url in CONFIG_URLS:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # 状态码 >=400 会抛异常
            config = response.json()
            logger.info(f"成功从 {url} 读取配置")
            return config
        except requests.RequestException as e:
            logger.error(f"获取配置文件失败: {url}, 错误: {e} ，请稍等以便自动尝试其他服务器")
        except json.JSONDecodeError as e:
            logger.error(f"解析配置文件 JSON 出错: {url}, 错误: {e} ，请稍等以便自动尝试其他服务器")

    logger.error("所有配置文件都获取失败，请检查网络或联系开发者，或者尝试在windows设置中更改DNS为8.8.8.8 备用DNS为114.114.114.114")
    return {}

def download_file(url, output_path) -> None:
    """下载文件，显示下载进度条

    Args:
        url (str): 文件下载链接
        output_path (str): 文件保存路径
    """
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

sentry_logger.debug('获取配置中', version=APP_VERSION)

cfg=read_config()# cfg是服务器返回的json配置

logger.info("读取配置文件成功")

sentry_logger.debug('已获取配置文件', version=APP_VERSION)

print(cfg['msg'])# 提示信息

# 检查目录下是否存在游戏主程序文件
if not os.path.exists(GAME_FILE):
    logger.error(f"未找到游戏主程序文件：{GAME_FILE}")
    colorprint("请确保程序在游戏安装目录下",color='1')
    sentry_logger.error('找不到游戏主程序文件', version=APP_VERSION)
    input("按回车键退出")
    sys.exit(1)

def test_download_speed(url, duration=10):
    """测试下载速度

    Args:
        url (str): 下载链接
        duration (int, optional): 测试持续时间（秒）。 Defaults to 10.

    Returns:
       elapsed (float): 下载耗时（秒）
       speed_mbps (float): 下载速度（Mbps）
       error (str, optional): 错误信息
    """
    try:
        headers = {'Range': 'bytes=0-'}
        response = requests.get(url, stream=True, headers=headers, timeout=duration + 5)
        
        if response.status_code not in [200, 206]:
            print(f"请求失败，状态码：{response.status_code}")
            return None, None, f"请求失败，状态码：{response.status_code}"

        downloaded = 0
        start_time = time.time()

        for chunk in response.iter_content(chunk_size=8192):
            if not chunk:
                break
            downloaded += len(chunk)
            elapsed = time.time() - start_time
            if elapsed >= duration:
                break

        speed_bps = downloaded / elapsed  # Bytes per second
        speed_mbps = speed_bps * 8 / 1_000_000  # Convert to Mbps
    except Exception as e:
        return None, None , str(e)
    return elapsed, speed_mbps , None

def speed_test():
    logger.info("开始速度测试")
    speedTestText=""""""# 速度测试结果
    speedTestText += "[速度测试报告]\n"
    sentry_logger.info('开始速度测试', version=APP_VERSION)
    ip_data = {'ip': '未知'}  # 初始化IP数据
    try:
        ip_response = requests.get("https://ipinfo.io/json", timeout=10)
        ip_data = ip_response.json()
        logger.info(f"当前IP地址：{ip_data['ip']}")
        sentry_logger.info('获取IP地址', version=APP_VERSION, ip=ip_data['ip'])
        speedTestText += f"当前IP地址：{ip_data['ip']}\n"
    except Exception as e:
        logger.error(f"获取IP地址失败，错误信息：{e}")
        sentry_logger.error('获取IP地址失败', version=APP_VERSION, error=str(e))
        speedTestText += f"获取IP地址失败，错误信息：{e}\n"
    sentry_logger.info('ip地址获取完成', version=APP_VERSION, ip=ip_data['ip'])
    logger.info("开始进行服务器连接测试")
    # 测试downloadTest中的各服务器，超时5秒
    speedTestText += "\n服务器连通性测试开始\n=========================\n"
    for i in range(len(cfg['downloadTest'])):
        # name是服务器名称，url是连接测试地址
        name = cfg['downloadTest'][i]['name']
        url = cfg['downloadTest'][i]['url']
        logger.info(f"正在测试服务器：{name}，地址：{url}")
        sentry_logger.info('测试下载服务器', version=APP_VERSION, name=name, url=url, ip=ip_data['ip'])
        speedTestText += f"\n测试服务器：{name}，地址：{url}：\n"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logger.info(f"服务器连接成功：{name}，地址：{url}")
                sentry_logger.info('下载服务器连接成功', version=APP_VERSION, name=name, url=url, ip=ip_data['ip'])
                speedTestText += f"服务器连接成功\n\n"
            else:
                logger.error(f"服务器连接失败：{name}，地址：{url}，状态码：{response.status_code}")
                sentry_logger.error('下载服务器连接失败', version=APP_VERSION, name=name, url=url, status_code=response.status_code, ip=ip_data['ip'])
                speedTestText += f"服务器连接失败，状态码：{response.status_code}\n\n"
        except Exception as e:
            logger.error(f"服务器连接失败：{name}，地址：{url}，错误信息：{e}")
            sentry_logger.error('下载服务器连接异常', version=APP_VERSION, name=name, url=url, error=str(e), ip=ip_data['ip'])
            speedTestText += f"服务器连接失败，错误信息：{e}\n\n"
    speedTestText += "=========================\n服务器连通性测试结束\n"
    logger.info("服务器连接测试完成")
    sentry_logger.info('服务器连接测试完成', version=APP_VERSION)
    # 测试下载速度 downloadSpeedTest
    speedTestText += "\n下载速度测试开始\n=========================\n"
    for i in range(len(cfg['downloadSpeedTest'])):
        url = cfg['downloadSpeedTest'][i]['url']
        name = cfg['downloadSpeedTest'][i]['name']
        logger.info(f"正在测试下载速度：{name}，地址：{url}")
        sentry_logger.info('测试下载速度', version=APP_VERSION, name=name, url=url, ip=ip_data['ip'])
        speedTestText += f"\n测试下载速度：{name}，地址：{url}："
        elapsed, speed_mbps, error = test_download_speed(url)
        if error:
            speedTestText += f"测试失败，错误信息：{error}\n"
            sentry_logger.error('测速失败', version=APP_VERSION, name=name, url=url, ip=ip_data['ip'], error=error)
        else:
            speedTestText += f"测试成功，耗时：{elapsed:.2f}秒，速度：{speed_mbps:.2f} Mbps\n"
            sentry_logger.info('测速成功', version=APP_VERSION, name=name, url=url, ip=ip_data['ip'], elapsed=str(elapsed), speed_mbps=str(speed_mbps))
    speedTestText += "=========================\n下载速度测试结束\n"
    logger.info("下载速度测试完成")
    sentry_logger.info('下载速度测试完成', version=APP_VERSION, ip=ip_data['ip'], speedTestText=speedTestText)
    print(speedTestText)

def Test_download_server():
    # 选择下载服务器
    for i in range(len(cfg['downloadServer'])):
        # 获取服务器地址/test.json
        url = cfg['downloadServer'][i]+"/test.json"
        sentry_logger.info('测试下载服务器', version=APP_VERSION, url=url)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logger.info(f"选择下载服务器：{cfg['downloadServer'][i]}")
                _downserver = cfg['downloadServer'][i]
                sentry_logger.info('选择下载服务器成功', version=APP_VERSION, downserver=_downserver)
                return _downserver
            else:
                logger.error(f"下载服务器连接失败：{cfg['downloadServer'][i]}[{response.status_code}]")
                sentry_logger.error('下载服务器异常', version=APP_VERSION, url=url, status_code=response.status_code)
        except Exception as e:
            logger.error(f"下载服务器连接失败：{cfg['downloadServer'][i]}，错误信息：{e}")
            sentry_logger.error('下载服务器连接失败', version=APP_VERSION, url=url, error=str(e))
    return None

if cfg['speedTest'] and not args.c:
    colorprint("注意：我们需要收集各地区的下载服务器连接情况，邀请你进行速度测试\n速度测试将收集你的ip和测试报告，最多需要2分钟并消耗最多1GB流量\n输入y并回车开始测试，直接回车跳过测试",color='2')
    input_str = input("是否开始速度测试？(y/n): ").strip().lower()
    if input_str == 'y':
        speed_test()
if cfg['speedTest'] and args.t:
    logger.info("命令行参数触发了速度测试")
    speed_test()
    
if not args.c:
    # 检查是否存在GUI程序
    if os.path.exists(GUI_FILE):
        logger.info(f"检测到GUI程序，建议使用GUI程序{GUI_FILE}运行本工具")
    else:
        colorprint(f"提示：新推出图形界面工具，更方便功能更多，输入y安装，直接回车取消", color='2')
        input_str = input("是否安装GUI程序？(y/n): ").strip().lower()
        if input_str == 'y':
            logger.info("安装GUI程序中")
            logger.info("正在下载GUI程序，请稍等...")
            sentry_logger.info('下载GUI程序', version=APP_VERSION)
            downserver = Test_download_server()
            download_file(downserver+GUI_FILE, GUI_FILE)
            colorprint(f"GUI程序下载完成，文件名为{GUI_FILE}，请双击运行\n注意：该工具只是个ui界面，请勿删除安装工具GetDLC.exe", color='5')
            input("按回车键退出")
            sys.exit(0)
        else:
            logger.info("不安装GUI程序")

colorprint("以下是支持的游戏版本：",color='5')
for i in range(len(cfg['version'])):
    colorprint(str(i)+" ",color='2',end='')
    colorprint(" "+str(cfg['version'][i]),color='5')
    
if not args.c:
    print()
    colorprint("请输入你已安装的游戏版本的编号：",color='5')
    v=input()
    while True:
        if v.isdigit() and int(v) in range(len(cfg['version'])): # 判断输入是否为数字且在范围内
            break
        else:
            colorprint("输入错误，请重新输入：",color='1')
            print("提示：编号是前面版本号列表的绿底数字，根据你的游戏版本输入对应的编号，编号从0开始")
            v = input()

    colorprint(f"确定你的游戏版本是{cfg['version'][int(v)]}吗？\n选择错误会导致游戏无法启动\n请提前关闭游戏\n回车键继续",color='4')
    input()
    vname = cfg['version'][int(v)]# 版本号
else:
    logger.info(f"命令行参数已指定游戏版本为：{args.v}")
    vname= args.v
    # 获取版本号在cfg['version']中的索引
    v = cfg['version'].index(vname) if vname in cfg['version'] else None
    
sentry_logger.info('已确认游戏版本', version=APP_VERSION,vname=vname)

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
    
sentry_logger.info('下载服务器列表', version=APP_VERSION, downloadServer=cfg['downloadServer'])
    
if args.r:
    # 还原游戏文件：1.检查是否存在备份文件，2.如果存在则删除Assembly-CSharp.dll再将备份文件重命名为Assembly-CSharp.dll
    if os.path.exists("A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll.bak"):
        logger.info("还原游戏文件")
        try:
            try:
                os.remove("A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll")
            except:
                pass
            os.rename("A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll.bak", "A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll")
            logger.info("还原游戏文件成功")
            sentry_logger.info('还原游戏文件成功', version=APP_VERSION)
        except Exception as e:
            logger.error(f"还原游戏文件失败，错误信息：{e}")
            sentry_logger.error('还原游戏文件失败', version=APP_VERSION, error=str(e))
    else:
        logger.error("还原游戏文件失败，未找到备份文件")
        sentry_logger.error('还原游戏文件失败', version=APP_VERSION, error='未找到备份文件')

else:
    downserver = Test_download_server()
    
    logger.info("开始下载游戏文件")

    sentry_logger.info('开始下载游戏文件', version=APP_VERSION, downserver=downserver,file=downserver+"/DLL/"+"Assembly-CSharp.dll"+"."+cfg['version'][int(v)]+gameDebug)
    download_file(downserver+"/DLL/"+"Assembly-CSharp.dll"+"."+cfg['version'][int(v)]+gameDebug, "A Dance of Fire and Ice_Data/Managed/Assembly-CSharp.dll")

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
            sentry_logger.info('下载dlc文件', version=APP_VERSION, url=downserver+i)
            download_file(downserver+i, cfg[vname]['dlcpath']+"/"+i)
            
    logger.info("处理完成，可以启动游戏使用dlc了")
sentry_logger.info('处理完成', version=APP_VERSION, vname=vname)
input("按回车键退出")