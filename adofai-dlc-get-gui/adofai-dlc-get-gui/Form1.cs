using System.Diagnostics;
using System.Windows.Forms;

namespace adofai_dlc_get_gui
{
    public partial class Form1 : Form
    {

        // comboBox1:游戏版本选择
        // checkBox1:是否启用DLC，默认开，预留
        // checkBox2:是否启用游戏的debug模式
        // checkBox3:测试新下载服务器速度
        // button3:恢复游戏文件
        // button1:开始获取DLC
        /// <summary>
        /// Initializes the main form for the DLC management tool, setting a fixed window size and default control states.
        /// </summary>

        public Form1()
        {
            // 窗口大小不可更改
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;

            InitializeComponent();

            // checkBox1默认是选中状态
            this.checkBox1.Checked = true;
        }


        /// <summary>
        /// Closes the application when the exit button is clicked.
        /// </summary>
        private void button2_Click(object sender, EventArgs e)
        {
            // 退出程序
            Application.Exit();
        }

        /// <summary>
        /// Opens the official game store page in the default web browser when the link label is clicked.
        /// </summary>
        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // 打开游戏官网
            System.Diagnostics.Process.Start(new ProcessStartInfo
            {
                FileName = "https://store.steampowered.com/app/977950/_A_Dance_of_Fire_and_Ice/",
                UseShellExecute = true
            });
        }

        /// <summary>
        /// Opens the DLC tool's GitHub repository page in the default web browser.
        /// </summary>
        private void button4_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start(new ProcessStartInfo
            {
                FileName = "https://github.com/wangdage12/adofai-dlc-get",
                UseShellExecute = true
            });
        }

        /// <summary>
        /// Handles the "Start DLC acquisition" button click by validating the selected game version, prompting for user confirmation, and launching the external DLC tool with appropriate command-line arguments based on user selections. Closes the application after starting the process.
        /// </summary>
        private void button1_Click(object sender, EventArgs e)
        {
            //usage: GetDLC.exe [-h] [-c] [-t] [-r] [-d] [--v V]

            //A Dance of Fire and Ice DLC获取工具

            //options:
            //  -h, --help  show this help message and exit
            //  -c          使用命令行参数
            //  -t          运行速度测试
            //  -r          还原游戏文件
            //  -d          启用游戏的debug模式
            //  --v V       游戏版本号

            // 检查是否选择了游戏版本
            if (comboBox1.SelectedItem == null)
            {
                label8.Visible = true;
                return;
            }

            DialogResult result = MessageBox.Show("确定游戏版本是" + comboBox1.SelectedItem.ToString() + "吗？\n选择错误会导致游戏无法启动\n如不确定请打开游戏，按esc查看左下角版本号\n请提前关闭游戏\n开始后会打开一个命令行窗口，请转到该窗口操作", "确认游戏版本", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.No)
            {
                return;
            }
            // 获取参数并执行命令行
            string args = "";

            args += "-c ";

            if (checkBox2.Checked)
            {
                args += "-d ";
            }
            if (checkBox3.Checked)
            {
                args += "-t ";
            }
            // 添加游戏版本号
            args += "--v " + comboBox1.SelectedItem.ToString();

            // 执行命令行
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = "GetDLC.exe",
                Arguments = args,
                UseShellExecute = true,
                CreateNoWindow = false,
                RedirectStandardOutput = false,
                RedirectStandardError = false,

            };
            Process process = new Process
            {
                StartInfo = startInfo
            };
            process.Start();

            //关闭程序
            Application.Exit();

        }

        /// <summary>
        /// Hides the error label when the selected game version in the combo box changes.
        /// </summary>
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label8.Visible = false;
        }

        /// <summary>
        /// Handles the restore operation for game files when the corresponding button is clicked.
        /// </summary>
        /// <remarks>
        /// Validates that a game version is selected, prompts the user for confirmation, and then launches the external "GetDLC.exe" process with arguments to restore original game files for the selected version. The application exits after starting the process.
        /// </remarks>
        private void button3_Click(object sender, EventArgs e)
        {
            // 还原游戏文件
            // 检查是否选择了游戏版本
            if (comboBox1.SelectedItem == null)
            {
                label8.Visible = true;
                return;
            }

            DialogResult result = MessageBox.Show("该功能将还原游戏文件，适用于在修改以后无法启动游戏的情况\n不会删除已下载的DLC文件\n确定开始吗？", "确认操作", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.No)
            {
                return;
            }
            // 获取参数并执行命令行
            string args = "";

            args += "-c ";

            if (checkBox2.Checked)
            {
                args += "-d ";
            }
            if (checkBox3.Checked)
            {
                args += "-t ";
            }

            // 还原游戏文件
            args += "-r ";

            // 添加游戏版本号
            args += "--v " + comboBox1.SelectedItem.ToString();

            // 执行命令行
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = "GetDLC.exe",
                Arguments = args,
                UseShellExecute = true,
                CreateNoWindow = false,
                RedirectStandardOutput = false,
                RedirectStandardError = false,

            };
            Process process = new Process
            {
                StartInfo = startInfo
            };
            process.Start();

            //关闭程序
            Application.Exit();
        }
    }
}
