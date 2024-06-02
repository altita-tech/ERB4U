# ERB API & 例程代码
* **ERB4U系列是一款可通过USART串口程控的继电器模块** 
* **PC端仅需1根USB Type-C线，即可同时读取/控制多个串联的继电器模块** 
* **每路继电器输出：** 最大30VDC/10A，1NO + 1NC
* **继电器总输出：** 最大30VDC/32A
* **工作原理：** ERB4U设备从USB或J1连接器（USART1）接收指令，并把原指令通过J6连接器（USART2）传递给下游ERB4U设备，实现可扩展功能。当接收到指令后，ERB4U会检查本机地址，只有当地址正确时，才会执行动作。
* **USART功能** 
    - **USART参数：** 115200波特率，8数据位，1停止位，奇校验，无流控制
    - **读取：** 单个/多个ERB4U的温度，继电器状态，PN/SN等信息
    - **控制：** 单个/多个继电器状态
* **地址设定：** 4位拨码开关设定地址0 – 15，多个ERB4U可同时使用一个地址
* **保护电路** 
    - 输入PMOS防反接
    - MCU与继电器光耦隔离
    - 可接阻性（R）或感性（L）负载
* **API & 例程代码：** Python API，完整例程代码
* **工作温度：** -40 to 85 ℃


<div style="text-align: center; margin: 10px;">
    <img src="Images/ERB4U%20功能介绍.png" alt="alt text" style="width: 100%;">
</div>

<div style="text-align: center; margin: 10px;">
    <img src="Images/ERB4U%20USART通讯原理.png" alt="alt text" style="width: 100%;">
</div>

<table>
  <tr>
    <td style="text-align: center;">
      <img src="Images/ERB4U-8%20产品正面.png" alt="ERB4U-8 产品正面" height="300">
    </td>
    <td style="text-align: center;">
      <img src="Images/ERB4U-8%20产品反面.png" alt="ERB4U-8 产品反面" height="300">
    </td>
  </tr>
</table>


## 通讯协议
### 读指令
<div style="text-align: center; margin: 10px;">
    <img src="Images/ERB4U%20读指令.png" alt="alt text" style="width: 100%;">
</div>




### 写指令
<div style="text-align: center; margin: 10px;">
    <img src="Images/ERB4U%20写指令.png" alt="alt text" style="width: 100%;">
</div>



### 故障信息
<div style="text-align: center; margin: 10px;">
    <img src="Images/ERB4U%20故障信息.png" alt="alt text" style="width: 100%;">
</div>


## 图纸
### 2D图纸
[2D图纸：下载链接](https://example.com/path/to/2D_drawing.zip)

<div style="text-align: center; margin: 10px;">
    <img src="Images/ERB4U%202D图纸.png" alt="alt text" style="width: 100%;">
</div>



### 3D模型
[3D模型：下载链接](https://example.com/path/to/2D_drawing.zip)
<table>
  <tr>
    <td style="text-align: center;">
      <img src="Images/ERB4U%203D模型%201.png" alt="ERB4U-8 产品正面" height="300">
    </td>
    <td style="text-align: center;">
      <img src="Images/ERB4U%203D模型%202.png" alt="ERB4U-8 产品反面" height="300">
    </td>
  </tr>
</table>




## 功能方框图

<div style="text-align: center; margin: 10px;">
  <img src="Images/ERB4U%20继电器电路.png" alt="alt text" style="width: 100%;">
</p>


<div style="text-align: center; margin: 10px;">
  <img src="Images/ERB4U%20功能方块图.png" alt="alt text" style="width: 100%;">
</p>




## 联系我们
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <div>
    <ul style="list-style-type: disc; padding-left: 20px; margin: 0;">
      <li><strong>公司官网：</strong> <a href="https://altita-tech.com/">https://altita-tech.com/</a></li>
      <li><strong>销售：</strong> <a href="mailto:sales@altita-tech.com">sales@altita-tech.com</a></li>
      <li><strong>技术支持：</strong> <a href="mailto:tech@altita-tech.com">tech@altita-tech.com</a></li>
    </ul>
  </div>
  <div>
    <img src="Images/Altita文字%20&%20Logo.png" alt="alt text" height="80">
  </div>
</div>


