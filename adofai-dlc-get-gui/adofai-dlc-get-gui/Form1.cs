using System.Diagnostics;
using System.Windows.Forms;

namespace adofai_dlc_get_gui
{
    public partial class Form1 : Form
    {

        // comboBox1:��Ϸ�汾ѡ��
        // checkBox1:�Ƿ�����DLC��Ĭ�Ͽ���Ԥ��
        // checkBox2:�Ƿ�������Ϸ��debugģʽ
        // checkBox3:���������ط������ٶ�
        // button3:�ָ���Ϸ�ļ�
        // button1:��ʼ��ȡDLC
        // label8:ûѡ����Ϸ�汾ʱ��ʾ�Ĵ�����Ϣ��Ĭ�����أ���Ҫ��ʱ����ʾ

        public Form1()
        {
            // ���ڴ�С���ɸ���
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.FormBorderStyle = FormBorderStyle.FixedSingle;

            InitializeComponent();

            // checkBox1Ĭ����ѡ��״̬
            this.checkBox1.Checked = true;
        }


        private void button2_Click(object sender, EventArgs e)
        {
            // �˳�����
            Application.Exit();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // ����Ϸ����
            System.Diagnostics.Process.Start(new ProcessStartInfo
            {
                FileName = "https://store.steampowered.com/app/977950/_A_Dance_of_Fire_and_Ice/",
                UseShellExecute = true
            });
        }

        private void button4_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start(new ProcessStartInfo
            {
                FileName = "https://github.com/wangdage12/adofai-dlc-get",
                UseShellExecute = true
            });
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //usage: GetDLC.exe [-h] [-c] [-t] [-r] [-d] [--v V]

            //A Dance of Fire and Ice DLC��ȡ����

            //options:
            //  -h, --help  show this help message and exit
            //  -c          ʹ�������в���
            //  -t          �����ٶȲ���
            //  -r          ��ԭ��Ϸ�ļ�
            //  -d          ������Ϸ��debugģʽ
            //  --v V       ��Ϸ�汾��

            // ����Ƿ�ѡ������Ϸ�汾
            if (comboBox1.SelectedItem == null)
            {
                label8.Visible = true;
                return;
            }

            DialogResult result = MessageBox.Show("ȷ����Ϸ�汾��" + comboBox1.SelectedItem.ToString() + "��\nѡ�����ᵼ����Ϸ�޷�����\n�粻ȷ�������Ϸ����esc�鿴���½ǰ汾��\n����ǰ�ر���Ϸ\n��ʼ����һ�������д��ڣ���ת���ô��ڲ���", "ȷ����Ϸ�汾", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.No)
            {
                return;
            }
            // ��ȡ������ִ��������
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
            // �����Ϸ�汾��
            args += "--v " + comboBox1.SelectedItem.ToString();

            // ִ��������
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

            //�رճ���
            Application.Exit();

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            label8.Visible = false;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // ��ԭ��Ϸ�ļ�
            // ����Ƿ�ѡ������Ϸ�汾
            if (comboBox1.SelectedItem == null)
            {
                label8.Visible = true;
                return;
            }

            DialogResult result = MessageBox.Show("�ù��ܽ���ԭ��Ϸ�ļ������������޸��Ժ��޷�������Ϸ�����\n����ɾ�������ص�DLC�ļ�\nȷ����ʼ��", "ȷ�ϲ���", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.No)
            {
                return;
            }
            // ��ȡ������ִ��������
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

            // ��ԭ��Ϸ�ļ�
            args += "-r ";

            // �����Ϸ�汾��
            args += "--v " + comboBox1.SelectedItem.ToString();

            // ִ��������
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

            //�رճ���
            Application.Exit();
        }
    }
}
