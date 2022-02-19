using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace Mouse_Position
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           Thread positionThread = new Thread(Position);
           positionThread.Start();
        }
        private void Position()
        {
            while (true)
            {
                int x = MousePosition.X;
                int y = MousePosition.Y;

                labelx.Text = x.ToString();
                labely.Text = y.ToString();


            }
            
        }
    }
}
