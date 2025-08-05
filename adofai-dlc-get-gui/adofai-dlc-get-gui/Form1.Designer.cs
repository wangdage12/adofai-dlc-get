namespace adofai_dlc_get_gui
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <summary>
        /// Releases the resources used by the form.
        /// </summary>
        /// <param name="disposing">true to release both managed and unmanaged resources; false to release only unmanaged resources.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// <summary>
        /// Initializes and configures all UI components and layout for the main form of the adofai DLC acquisition tool.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            comboBox1 = new ComboBox();
            label4 = new Label();
            label5 = new Label();
            checkBox1 = new CheckBox();
            checkBox2 = new CheckBox();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            label6 = new Label();
            label7 = new Label();
            linkLabel1 = new LinkLabel();
            button4 = new Button();
            checkBox3 = new CheckBox();
            label8 = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.BackColor = SystemColors.ControlLightLight;
            label1.Font = new Font("Microsoft YaHei UI", 10.5F, FontStyle.Bold, GraphicsUnit.Point, 134);
            label1.ForeColor = SystemColors.MenuHighlight;
            label1.Location = new Point(3, 4);
            label1.Name = "label1";
            label1.Size = new Size(65, 19);
            label1.TabIndex = 0;
            label1.Text = "游戏版本";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.ForeColor = SystemColors.MenuHighlight;
            label2.Location = new Point(-2, 21);
            label2.Name = "label2";
            label2.Size = new Size(710, 17);
            label2.TabIndex = 1;
            label2.Text = "——————————————————————————————————————————————————————";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(5, 42);
            label3.Name = "label3";
            label3.Size = new Size(184, 17);
            label3.TabIndex = 2;
            label3.Text = "你当前安装的游戏版本(请选择)：";
            // 
            // comboBox1
            // 
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "v2.8.1", "v2.9.5" });
            comboBox1.Location = new Point(182, 39);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(121, 25);
            comboBox1.TabIndex = 3;
            comboBox1.SelectedIndexChanged += comboBox1_SelectedIndexChanged;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.BackColor = SystemColors.ControlLightLight;
            label4.Font = new Font("Microsoft YaHei UI", 10.5F, FontStyle.Bold, GraphicsUnit.Point, 134);
            label4.ForeColor = SystemColors.MenuHighlight;
            label4.Location = new Point(3, 71);
            label4.Name = "label4";
            label4.Size = new Size(65, 19);
            label4.TabIndex = 4;
            label4.Text = "安装选项";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.ForeColor = SystemColors.MenuHighlight;
            label5.Location = new Point(-2, 90);
            label5.Name = "label5";
            label5.Size = new Size(710, 17);
            label5.TabIndex = 5;
            label5.Text = "——————————————————————————————————————————————————————";
            // 
            // checkBox1
            // 
            checkBox1.AccessibleDescription = "";
            checkBox1.AutoSize = true;
            checkBox1.CheckAlign = ContentAlignment.MiddleRight;
            checkBox1.Checked = true;
            checkBox1.CheckState = CheckState.Checked;
            checkBox1.Enabled = false;
            checkBox1.Location = new Point(5, 110);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(74, 21);
            checkBox1.TabIndex = 7;
            checkBox1.Text = "启用DLC";
            checkBox1.UseVisualStyleBackColor = true;
            // 
            // checkBox2
            // 
            checkBox2.AccessibleDescription = "";
            checkBox2.AutoSize = true;
            checkBox2.CheckAlign = ContentAlignment.MiddleRight;
            checkBox2.Location = new Point(5, 137);
            checkBox2.Name = "checkBox2";
            checkBox2.Size = new Size(126, 21);
            checkBox2.TabIndex = 8;
            checkBox2.Text = "启用游戏的DeBug";
            checkBox2.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            button1.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button1.FlatAppearance.MouseDownBackColor = Color.LightBlue;
            button1.FlatStyle = FlatStyle.Flat;
            button1.Location = new Point(609, 286);
            button1.Name = "button1";
            button1.Size = new Size(84, 29);
            button1.TabIndex = 9;
            button1.Text = "开始";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button2.FlatAppearance.MouseDownBackColor = Color.LightBlue;
            button2.FlatStyle = FlatStyle.Flat;
            button2.Location = new Point(330, 286);
            button2.Name = "button2";
            button2.Size = new Size(84, 29);
            button2.TabIndex = 10;
            button2.Text = "退出";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // button3
            // 
            button3.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button3.FlatAppearance.MouseDownBackColor = Color.LightBlue;
            button3.FlatStyle = FlatStyle.Flat;
            button3.Location = new Point(510, 286);
            button3.Name = "button3";
            button3.Size = new Size(93, 29);
            button3.TabIndex = 11;
            button3.Text = "恢复游戏DLL";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.ForeColor = SystemColors.MenuHighlight;
            label6.Location = new Point(642, 6);
            label6.Name = "label6";
            label6.Size = new Size(59, 17);
            label6.TabIndex = 12;
            label6.Text = "GUI V1.0";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(3, 250);
            label7.Name = "label7";
            label7.Size = new Size(247, 51);
            label7.TabIndex = 13;
            label7.Text = "警告：本工具仅限研究DLC和游戏的各种功能\r\n对于超出工具预期用途使用的，后果自负\r\n工具不收取任何费用";
            // 
            // linkLabel1
            // 
            linkLabel1.AutoSize = true;
            linkLabel1.LinkColor = SystemColors.MenuHighlight;
            linkLabel1.Location = new Point(3, 301);
            linkLabel1.Name = "linkLabel1";
            linkLabel1.Size = new Size(163, 17);
            linkLabel1.TabIndex = 14;
            linkLabel1.TabStop = true;
            linkLabel1.Text = "请先点此购买正版游戏和DLC";
            linkLabel1.LinkClicked += linkLabel1_LinkClicked;
            // 
            // button4
            // 
            button4.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button4.FlatAppearance.MouseDownBackColor = Color.LightBlue;
            button4.FlatStyle = FlatStyle.Flat;
            button4.Location = new Point(420, 286);
            button4.Name = "button4";
            button4.Size = new Size(84, 29);
            button4.TabIndex = 15;
            button4.Text = "Github仓库";
            button4.UseVisualStyleBackColor = true;
            button4.Click += button4_Click;
            // 
            // checkBox3
            // 
            checkBox3.AccessibleDescription = "";
            checkBox3.AutoSize = true;
            checkBox3.CheckAlign = ContentAlignment.MiddleRight;
            checkBox3.Location = new Point(5, 164);
            checkBox3.Name = "checkBox3";
            checkBox3.Size = new Size(159, 21);
            checkBox3.TabIndex = 16;
            checkBox3.Text = "测试新下载服务器的速度";
            checkBox3.UseVisualStyleBackColor = true;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.ForeColor = Color.Red;
            label8.Location = new Point(309, 42);
            label8.Name = "label8";
            label8.Size = new Size(116, 17);
            label8.TabIndex = 17;
            label8.Text = "请选择你的游戏版本";
            label8.Visible = false;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.ControlLightLight;
            ClientSize = new Size(705, 327);
            Controls.Add(label8);
            Controls.Add(checkBox3);
            Controls.Add(button4);
            Controls.Add(linkLabel1);
            Controls.Add(label7);
            Controls.Add(label6);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(checkBox2);
            Controls.Add(checkBox1);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(comboBox1);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Form1";
            Text = "adofai DLC获取工具";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private ComboBox comboBox1;
        private Label label4;
        private Label label5;
        private CheckBox checkBox1;
        private CheckBox checkBox2;
        private Button button1;
        private Button button2;
        private Button button3;
        private Label label6;
        private Label label7;
        private LinkLabel linkLabel1;
        private Button button4;
        private CheckBox checkBox3;
        private Label label8;
    }
}
